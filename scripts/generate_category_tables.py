#!/usr/bin/env python3
"""Generate marked category comparisons from structured tool frontmatter."""
import argparse
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
ACCESS = {'online-web': 'Online/Web', 'cli': 'CLI', 'python-script': 'Python',
          'desktop-app': 'Desktop app', 'browser-extension': 'Browser extension',
          'mobile-app': 'Mobile app', 'api': 'API'}
ACCOUNT = {'no': 'No', 'yes': 'Yes', 'optional': 'Optional / feature-dependent', 'third-party': 'Third-party account'}
START = '<!-- generated-tools: '
END = '<!-- /generated-tools -->'

def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ').replace('<', '&lt;').replace('>', '&gt;')

def load_tools():
    tools = []
    for path in sorted((ROOT / 'osint-tools').glob('*.md')):
        text = path.read_text()
        if not text.startswith('---\n') or '\n---' not in text[4:]:
            continue
        # BaseLoader keeps YAML's yes/no and dates as strings consistently.
        meta = yaml.load(text[4:].split('\n---', 1)[0], Loader=yaml.BaseLoader)
        if isinstance(meta, dict) and 'tool' in meta:
            tools.append((path, meta))
    return tools

def table(category, tools):
    rows = ['| Tool | Best for | Access | Inputs | Cost | What is free? | Paid unlocks | Account | Verification |',
            '| --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    selected = sorted(((p, m) for p, m in tools if category in m['tool']['categories']), key=lambda item: item[1]['tool']['name'].casefold())
    if not selected:
        raise ValueError(f'No structured tools for category {category}')
    for path, meta in selected:
        t = meta['tool']; pricing = t['pricing']
        verified = t.get('last_verified')
        values = [f"[{cell(t['name'])}](../osint-tools/{path.name})", cell(meta['description']),
                  cell(' · '.join(ACCESS[a] for a in t['access_methods'])), cell(', '.join(t['inputs'])),
                  cell(pricing['model'].capitalize()), cell(pricing['free_tier']),
                  cell('; '.join(pricing['paid_unlocks']) if pricing['paid_unlocks'] else 'None documented'),
                  cell(ACCOUNT[t['account_required']]), cell(verified if verified and verified != 'null' else 'Pending')]
        rows.append('| ' + ' | '.join(values) + ' |')
    return '\n'.join(rows)

def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--check', action='store_true'); args = parser.parse_args()
    tools = load_tools(); stale = []
    for path in sorted((ROOT / 'tool-categories').rglob('*.md')):
        text = path.read_text(); updated = text
        if START not in text: continue
        before, rest = text.split(START, 1)
        category, rest = rest.split(' -->', 1)
        _, after = rest.split(END, 1)
        updated = before + START + category + ' -->\n' + table(category, tools) + '\n' + END + after
        if updated != text:
            stale.append(str(path.relative_to(ROOT)))
            if not args.check: path.write_text(updated)
    if args.check and stale:
        print('Outdated category tables: ' + ', '.join(stale), file=sys.stderr); return 1
    print('Category tables are current.' if args.check else f'Updated {len(stale)} category table(s).'); return 0

if __name__ == '__main__':
    raise SystemExit(main())
