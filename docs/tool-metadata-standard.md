# Tool Metadata Standard

This document defines the structured metadata used by the redesigned OSINT Tools Library.

The goal is to make tools easy to compare **before** opening the full tool page and to make category pages/filtering automatable later.

## Required metadata

Add this YAML frontmatter to each tool page:

```yaml
---
description: Short plain-language description of the tool.
tool:
  name: Epieos
  url: https://epieos.com/
  status: active
  categories:
    - email
    - phone
  inputs:
    - email
    - phone-number
  capabilities:
    - linked-accounts
    - breach-data
    - username-correlation
  pricing:
    model: freemium
    free_tier: Basic email/phone searches with limited results.
    paid_unlocks:
      - deeper linked-account results
      - additional platform data
    price: unknown
  account_required: optional
  access_methods:
    - online-web
  implementation:
    - hosted-service
  open_source: false
  geographic_scope: global
  last_verified: 2026-10-06
---
```

## Allowed values

### Pricing model

Use one of:

- `free`
- `freemium`
- `paid`
- `enterprise`
- `unknown`

Do not use **freemium** by itself as the explanation. The `free_tier` field should say what an investigator actually gets without paying, and `paid_unlocks` should list the important capabilities behind the paywall.

### Account requirement

Use one of:

- `no`
- `yes`
- `optional`
- `third-party`

`third-party` means the tool itself may not require an account but a connected service does.

### Status

Use one of:

- `active`
- `degraded`
- `broken`
- `discontinued`
- `unknown`

### Access method

Use one or more values so investigators can tell whether a tool opens directly in a browser or needs local installation:

- `online-web` — accessible as a hosted website/web application
- `cli` — command-line program
- `python-script` — Python script or Python-first package intended to be run locally
- `desktop-app` — installed graphical desktop application
- `browser-extension` — browser add-on
- `mobile-app` — installed mobile application
- `api` — directly usable through an API

A tool may have multiple access methods. For example, a project can provide both an online web interface and an API.

### Implementation

Use this separately from access method when useful. Common values include:

- `hosted-service`
- `python`
- `javascript`
- `go`
- `rust`
- `native-app`
- `unknown`

This prevents ambiguous labels such as “CLI” from hiding whether the downloadable tool is actually a Python script/package or a compiled executable.

## Category-page display

Category pages should expose the information needed to choose a tool without opening every entry:

| Tool | Best for | Access | Inputs | Cost | What is free? | Account |
| ---- | -------- | ------ | ------ | ---- | ------------- | ------- |
| Example | Short investigative use case | Online/Web | Email, phone | Freemium | Basic lookup | Optional |

The full tool page remains the place for instructions, screenshots, limitations, ownership, ethical considerations, and sources.

## Verification

`last_verified` records when pricing/access/capability information was last checked. Pricing and feature availability change frequently, so stale entries should be rechecked rather than silently treated as current.

## Design principle

A user should be able to answer these questions from a category page:

1. What does this tool help me find?
2. What can I search with it?
3. Can I use it for free?
4. If not, what requires payment?
5. Do I need an account?
6. Can I use it online, or do I need to install/run something locally?
7. If local, is it a CLI, Python script/package, desktop app, or something else?
8. Is the tool currently usable?

## Generated comparisons and migration provenance

Install dependencies with `python -m pip install -r requirements.txt`, run `python scripts/validate_tool_metadata.py`, then `python scripts/generate_category_tables.py`. CI checks the metadata and runs the generator with `--check` to reject stale tables.

Opt a category into generation using `<!-- generated-tools: archiving -->` and `<!-- /generated-tools -->` markers around its comparison table. The generator selects tools by their `tool.categories` value and preserves text outside the marked block. Categories without markers remain unchanged during migration.

Use `last_verified: null` and a nonempty `verification_notes` when importing existing descriptions without independently checking the vendor. `metadata_reviewed` may record the migration date, but is not a vendor verification date. Use `status: unknown` until availability is checked; `open_source: unknown` is allowed when licensing has not been established. Do not treat a free trial as a permanent free tier. The Access field may cover different operations: explain when a CLI only verifies evidence while an extension creates captures.

