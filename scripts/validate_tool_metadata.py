#!/usr/bin/env python3
"""Validate normalized YAML metadata while allowing legacy pages during migration."""
from datetime import date
from pathlib import Path
import sys
from urllib.parse import urlparse
import yaml

ROOT = Path(__file__).resolve().parents[1]
ENUMS = {'status': {'active', 'degraded', 'broken', 'discontinued', 'unknown'},
         'account_required': {'no', 'yes', 'optional', 'third-party'},
         'open_source': {'true', 'false', 'unknown'}}
ACCESS = {'online-web', 'cli', 'python-script', 'desktop-app', 'browser-extension', 'mobile-app', 'api'}
PRICING = {'free', 'freemium', 'paid', 'enterprise', 'unknown'}
REQUIRED = {'name', 'url', 'status', 'categories', 'inputs', 'capabilities', 'pricing',
            'account_required', 'access_methods', 'implementation', 'open_source', 'geographic_scope', 'last_verified'}

def validate_text(text):
    if not text.startswith('---\n') or '\n---' not in text[4:]:
        return False, []  # Legacy Markdown is allowed until it opts into tool metadata.
    try:
        meta = yaml.load(text[4:].split('\n---', 1)[0], Loader=yaml.BaseLoader)
    except yaml.YAMLError as exc:
        return False, [f'invalid YAML: {exc}']
    if not isinstance(meta, dict) or 'tool' not in meta: return False, []
    t = meta['tool']; errors = []
    if not isinstance(t, dict): return True, ['tool must be a mapping']
    for field in sorted(REQUIRED - t.keys()): errors.append(f'missing field: {field}')
    if not isinstance(meta.get('description'), str) or not meta['description'].strip(): errors.append('description must be nonempty')
    for field in ('name', 'geographic_scope'):
        if not isinstance(t.get(field), str) or not t[field].strip(): errors.append(f'{field} must be nonempty')
    for field, allowed in ENUMS.items():
        if t.get(field) not in allowed: errors.append(f'invalid {field}: {t.get(field)}')
    url = urlparse(t.get('url', '') if isinstance(t.get('url', ''), str) else '')
    if url.scheme not in {'http', 'https'} or not url.netloc: errors.append('url must be an HTTP(S) URL')
    for field in ('categories', 'inputs', 'capabilities', 'access_methods', 'implementation'):
        values = t.get(field)
        if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v.strip() for v in values):
            errors.append(f'{field} must be a nonempty list of strings')
        elif field == 'access_methods' and not set(values) <= ACCESS: errors.append('invalid access_methods value')
    pricing = t.get('pricing')
    if not isinstance(pricing, dict): errors.append('pricing must be a mapping')
    else:
        if pricing.get('model') not in PRICING: errors.append('invalid pricing.model')
        if not isinstance(pricing.get('free_tier'), str) or not pricing['free_tier'].strip(): errors.append('pricing.free_tier must be nonempty')
        paid = pricing.get('paid_unlocks')
        if not isinstance(paid, list) or any(not isinstance(v, str) or not v.strip() for v in paid): errors.append('pricing.paid_unlocks must be a list of strings')
    verified = t.get('last_verified')
    if verified in (None, '', 'null', '~'):
        if not t.get('verification_notes'): errors.append('unverified tools require verification_notes')
    else:
        try:
            parsed = date.fromisoformat(verified)
            if parsed.isoformat() != verified or parsed > date.today(): raise ValueError()
        except (ValueError, TypeError): errors.append('last_verified must be a real YYYY-MM-DD date, not in the future, or null')
    return True, errors

def main():
    structured = legacy = failures = 0
    for path in sorted((ROOT / 'osint-tools').glob('*.md')):
        is_structured, errors = validate_text(path.read_text())
        structured += is_structured; legacy += not is_structured
        if errors:
            failures += 1; print(str(path.relative_to(ROOT)) + ': ' + '; '.join(errors))
    print(f'Structured entries: {structured}; legacy entries: {legacy}')
    print('Metadata validation failed.' if failures else 'Metadata validation passed.')
    return int(bool(failures))

if __name__ == '__main__': raise SystemExit(main())
