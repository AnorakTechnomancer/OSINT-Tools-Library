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
  platform:
    - web
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

### Platform

Common values:

- `web`
- `cli`
- `desktop`
- `browser-extension`
- `api`
- `mobile`

## Category-page display

Category pages should expose the information needed to choose a tool without opening every entry:

| Tool | Best for | Inputs | Cost | What is free? | Account |
| ---- | -------- | ------ | ---- | ------------- | ------- |
| Example | Short investigative use case | Email, phone | Freemium | Basic lookup | Optional |

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
6. Is the tool currently usable?
