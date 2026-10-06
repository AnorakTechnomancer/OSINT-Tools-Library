---
description: >-
  Standard template for adding or updating an OSINT tool in the library.
tool:
  name: Tool Name
  url: https://example.com/
  status: unknown
  categories:
    - category-name
  inputs:
    - input-type
  capabilities:
    - capability
  pricing:
    model: unknown
    free_tier: Describe exactly what is available without paying.
    paid_unlocks:
      - Describe the important capabilities that require payment.
    price: unknown
  account_required: optional
  access_methods:
    - online-web
  implementation:
    - hosted-service
  open_source: false
  geographic_scope: global
  last_verified: YYYY-MM-DD
---

# Tool Name

> **At a glance:** One sentence explaining why an investigator would choose this tool.

| **Tool Name** | **Quick Overview** |
| --- | --- |
| URL | https://example.com/ |
| Best for | The primary investigative task this tool solves. |
| Inputs | Email, phone number, username, image, domain, etc. |
| Outputs | Linked accounts, breach data, metadata, locations, records, etc. |
| Cost | Free / Freemium / Paid / Enterprise |
| Free access | Describe exactly what works without payment. |
| Paid unlocks | Describe the meaningful features behind payment. |
| Account required | No / Yes / Optional / Third-party account |
| Access method | Online/Web / CLI / Python script/package / desktop app / browser extension / mobile / API |
| Implementation | Hosted service / Python / JavaScript / Go / Rust / native app / unknown |
| Open source | Yes / No |
| Geographic scope | Global / country / region |
| Last verified | YYYY-MM-DD |

### What does the Tool Do?

Describe what the tool does and what problem it solves. Focus on investigator outcomes rather than marketing language.

### How to Use

Provide concise steps or link to a maintained guide.

### Pricing and Access

Do not stop at “freemium.” Document:

- what can be done for free;
- important limits on the free tier;
- what payment unlocks;
- published pricing when available;
- whether pricing requires contacting sales.

### Data Processing

#### Account Required

Explain whether the tool requires its own account, a third-party account, authentication cookies, or API credentials.

#### Cookies / Authentication

Summarise relevant cookies, tokens, or authentication requirements and what they mean for analysts.

### Use in Reporting

Explain where the tool fits in an investigation and what findings should be independently verified.

| **Capabilities** | **Limitations** |
| --- | --- |
| Capability | Limitation |
| Capability | Limitation |

### Summary

Summarise the strongest use cases, tradeoffs, and where the tool fits in an OSINT workflow.

### Ownership

Explain who owns or maintains the tool and any context relevant to trust, jurisdiction, or conflicts of interest.

### Ethical Considerations

- Use tools lawfully and within authorisation.
- Verify findings before attribution or publication.
- Minimise unnecessary collection or exposure of personal data.
- Add tool-specific considerations here.

### Related Tools

- Similar tool

#### Sources

- Primary tool URL
- Pricing/access source
- Documentation or repository
- Other authoritative sources

---

See [Tool Metadata Standard](../docs/tool-metadata-standard.md) for the normalized fields used by category pages and future filtering.
