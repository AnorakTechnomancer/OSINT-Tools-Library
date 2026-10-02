---
description: >-
  Tool Description : A free global company lookup covering 479 million+ legal
  entities aggregated from official corporate registries across 309
  jurisdictions in 244 countries.
---

# Registry Lookup

| **Registry Lookup** | **Quick Overview**                                                                                                                              |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| URL                 | [https://registry-lookup.com/](https://registry-lookup.com/)                                                                                    |
| What it does        | Searches official company registry records worldwide by name, registry number, jurisdiction, or tax/VAT identifier.                             |
| How to use it       | Enter a company name or registry number, filter by jurisdiction, then open the entity record to view its registry identifiers and status.       |
| Cost                | Free.                                                                                                                                           |
| Account required    | No (search and browse), Yes (for an API key).                                                                                                   |
| Cookies             | Several different tracking/security technologies, notably Cloudflare, HubSpot and PostHog.                                                      |
| Ownership           | Veridion (Dataworks Research SRL), a business data company based in Bucharest, Romania.                                                         |
| Use in Reporting    | Useful for cross-jurisdiction company identification, registry number verification, and establishing the legal identity behind a trading name.  |

### What does Registry Lookup do?

Registry Lookup is a free search layer over official corporate registry data, aggregating legal entity records from government company registries, corporate filings databases, and open data sources into one normalised, searchable index.

It answers a narrow question well: does this legal entity exist, in which jurisdiction, under what registry number, and is it still active? Rather than working through national registries one at a time, you can search across all of them and get back a consistent record shape regardless of source.

**The lowdown:** It's an identity-resolution and verification tool, not a filings archive. Use it to pin down the correct legal entity and its identifiers, then go to the official registry for documents.

**Note:** The operator states explicitly that it is not an official government registry, and that filings, certificates, or legally conclusive status must be obtained from the relevant official registry.

### How to Use:

**1. Search by company name, registry number, or tax/VAT identifier.** Autocomplete suggests matching entities as you type, which is useful when the exact registered name differs from the trading name.

<img src="../.gitbook/assets/unknown (634).png" alt="" height="456" width="602">

**Note:** You can filter by jurisdiction. Coverage is organised by jurisdiction rather than country, so sub-national registers (US states, Canadian provinces, Swiss cantons) are addressable individually — 309 jurisdictions across 244 countries.

**2. Open the entity record to view legal name, registry number, jurisdiction code, status, incorporation date, legal form, registered address, and tax/VAT identifiers where the source registry publishes them.**

<img src="../.gitbook/assets/unknown (635).png" alt="" height="331" width="602">

**3. Verify against the official registry before using any finding in reporting or evidence.**

### Cost

* [x] Free
* [ ] Partially Free
* [ ] Paid

## Data Processing

### Account Required:

* [x] Yes
* [x] No

No (search and browse), Yes (for an API key).&#x20;

### Cookies:&#x20;

Registry Lookup uses essential security/session cookies and third-party analytics technologies.&#x20;

The captured cookies include Cloudflare's \_\_cf\_bm for bot protection, HubSpot cookies (\_\_hstc, \_\_hssc, \_\_hssrc and hubspotutk) for visitor/session tracking, and a PostHog cookie containing pseudonymous device, visitor and session identifiers. A first-party rl\_tok token is also present and its exact purpose is not publicly documented so should be treated as sensitive.&#x20;

### Use in Reporting

Registry Lookup can be used for:

* Confirming that a named company exists as a registered legal entity.
* Resolving a trading name to its registered legal name and registry number.
* Identifying the jurisdiction of incorporation for a cross-border entity.
* Verifying registry numbers and tax/VAT identifiers cited in documents.
* Checking whether an entity is active, dissolved, or otherwise flagged.
* Building a jurisdiction shortlist before requesting official filings.

The tool was covered by[ Indicator](https://indicator.media/) in its 7 August 2026 Briefing “Grokipedia's edit freeze”, which noted its coverage relative to OpenCorporates and recommended checking both.

| **Capabilities**                                                                         | **Limitations**                                                                  |
| ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Searches 479 million+ entities across 309 jurisdictions in 244 countries.                | Not an official registry; no legally conclusive status or certificates.          |
| Normalises records into a consistent shape across very different source registries.      | Does not host filings, documents, or scanned registry extracts.                  |
| Free to search with no account or paywall.                                               | No officer, shareholder, or beneficial ownership data.                           |
| Free API tier (5,000 calls/month) with search, lookup, autocomplete, and jurisdictions.  | Data quality and freshness depend on the underlying national registry.           |
| Sub-national jurisdictions are individually addressable.                                 | Normalisation across registries can obscure source-specific fields and caveats.  |

### Summary

Registry Lookup sits in the discovery and verification stages of a corporate investigation. It's a fast first stop for establishing that an entity exists and pinning down its registry identifiers across jurisdictions, and it pairs naturally with tools that go deeper on ownership and filings once the correct entity has been identified.

### Ownership

Operated by Veridion, the trading name of Dataworks Research SRL, a business data company based in Bucharest, Romania, with a US presence in New York. The company was founded in 2019 (as Soleadify) by[ Florin Tufan](https://www.linkedin.com/in/florin-tufan-3b0b66173/), Mihai Vinaga, and Sorina Vlasceanu, and rebranded to Veridion in 2022. Registry Lookup is a free release of the legal entity layer of Veridion's commercial database.&#x20;

### Ethical Considerations

* Treat records as a pointer to the official registry, not as evidence in themselves.
* Verify status and identifiers against the source register before publication.
* Be aware that registry data quality and update frequency vary widely by jurisdiction.
* Registered addresses are frequently registered-agent or accountant addresses, not operating premises.
* Records may include personal data where sole traders register under their own name; handle accordingly.
* Do not infer that an active status implies trading activity, or that a dissolved status implies wrongdoing.

### Related Tools:

* [OpenCorporates](opencorporates.md)
* [North Data](north-data.md)
* [Companies House](companies-house.md)
* [Corporation Wiki](corporation-wiki.md)
* Business Registers in EU countries

#### Sources

[https://registry-lookup.com/](https://registry-lookup.com/)&#x20;

[https://registry-lookup.com/about](https://registry-lookup.com/about)&#x20;

[https://indicator.media/](https://indicator.media/)&#x20;

[https://www.linkedin.com/in/florin-tufan-3b0b66173/](https://www.linkedin.com/in/florin-tufan-3b0b66173/)

[https://www.crunchbase.com/organization/soleadify](https://www.crunchbase.com/organization/soleadify)



_With thanks to Github user_ [_mihai-lgtm_](https://github.com/mihai-lgtm) _for submitting this tool to the OSINT Tool LIbrary._
