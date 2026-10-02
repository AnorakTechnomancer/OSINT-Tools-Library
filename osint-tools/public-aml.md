---
description: >-
  Tool Description : A free, non-profit cryptocurrency AML/KYT screening service
  that checks blockchain addresses for sanctions, scam, hack, and other risk
  indicators.
---

# Public AML

| **Public AML**   | **Quick Overview**                                                                                                                                                            |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URL              | [https://publicaml.org/](https://publicaml.org/)                                                                                                                              |
| What it does     | Screens a crypto wallet address for criminal exposure and explains why: sanctions listings, scam and phishing reports, hack attribution and traced exposure to stolen funds.  |
| How to use it    | Paste an address and get a 0-100 risk score with the findings behind it, the entity it belongs to where known, and its counterparties.                                        |
| Cost             | Free - no paid tier, no trial, keyless API.                                                                                                                                   |
| Account required | No.                                                                                                                                                                           |
| Cookies          | A mix of Google Analytics cookies and a PublicAML-specific visitor/session.                                                                                                   |
| Ownership        | PublicAML, a registered US non-profit incorporated in Delaware, United States.                                                                                                |
| Use in Reporting | Useful for screening cryptocurrency addresses, tracing counterparties and identifying potential sanctions, scam, hack or illicit-funds exposure.                              |

### What does Public AML do?

Public AML provides risk scoring for a single address across seven chains, with every finding shown rather than a bare number: sanctions matches, scam and phishing reports, hack and exploit attribution, mixer interaction, and exposure to stolen funds through traced hops.&#x20;

It lists counterparties and known entities (exchanges, bridges, mixers), traces funds forward to where they cashed out, and identifies swap and bridge hops. A public directory of about 200,000 flagged addresses can be browsed by chain and by category (sanctions, mixers, ransomware, hacks, scams, phishing).&#x20;

Investigations are published as case pages with the addresses and transaction hashes involved.

**The lowdown:** It can help establish whether an address has known exposure to sanctions, scams, hacks or other risk categories and provide context about the wallet's counterparties and funding.

### How to Use:

**1. Open https://publicaml.org/ and paste an address into the checker.**

<img src="../.gitbook/assets/unknown (616).png" alt="" height="192" width="602">

**2. Read the score and the findings that produced it; each finding names its source and how many hops away it sits.**

<img src="../.gitbook/assets/unknown (617).png" alt="" height="279" width="602">

**Note:** Open the address page (https://publicaml.org/address///) for a permanent, citable URL.<br>

**3. Browse related addresses through the directory at https://publicaml.org/directory/.**

<img src="../.gitbook/assets/unknown (618).png" alt="" height="385" width="602">

For scripted work, POST to https://intelapi.publicaml.org/v1/enrich with {"addresses":\[{"wallet\_address":"0x...","chain":"ethereum"}]} - no API key needed.&#x20;

To use it inside an AI assistant, add the MCP server at https://mcp.publicaml.org/mcp as a connector.

### Cost

* [x] Free
* [ ] Partially Free
* [ ] Paid

Free - no paid tier, no trial, keyless API.

## Data Processing

### Account Required:

* [ ] Yes
* [x] No

### Cookies:&#x20;

PublicAML uses Google Analytics cookies \_ga and \_ga\_8Q9H3E2XK7 to distinguish visitors and maintain session/activity information for website analytics. It also sets a first-party paml\_vid cookie containing an opaque visitor identifier. paml\_vid is Secure, HttpOnly and SameSite=Lax, indicating that it is designed for protected first-party visitor/session identification.

### Use in Reporting

PublicAML can be used to:

* Screen cryptocurrency addresses for known sanctions exposure.
* Identify wallet addresses associated with known scams, hacks or other risk categories.
* Examine direct versus indirect exposure to sanctioned or high-risk addresses.
* Identify known entities associated with a cryptocurrency address.
* Investigate a wallet's counterparties and transaction relationships.
* Examine reported sources of funds and the provenance of cryptocurrency entering an address.
* Support tracing of funds through multiple blockchain addresses.
* Identify potential links between wallets involved in a suspected scam, hack or illicit-finance investigation.

**Note:** Every address has a permanent public page suitable for citation, showing the score, the findings and their sources.

Published investigations include the full on-chain trace: the Chainflip TRON exploit of 12 Sep 2026, where the attacker and the route of the 749,000 USDT to a Binance deposit were traced ([https://publicaml.org/news/2026-09-12-chainflip/](https://publicaml.org/news/2026-09-12-chainflip/)), plus traces of the Gnosis Safe module exploit (\~$7.8M rsETH, 15 Sep 2026) and the Spiral oracle exploit (14 Sep 2026), both published as replies under the SlowMist alerts from [https://x.com/PublicAML](https://x.com/PublicAML).&#x20;

| **Capabilities**                                                                  | **Limitations**                                                                                      |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Risk score with every contributing finding shown, not just a number.              | Coverage is strongest on Ethereum, TRON and Bitcoin; smaller chains have thinner data.               |
| Seven chains: Bitcoin, Ethereum, TRON, BNB Chain, Polygon, Arbitrum, Base.        | Attribution of an address to a named service is incomplete - many custodial services are unlabelled. |
| Public directory of \~200,000 flagged addresses, browsable by chain and category. | Tracing through mixers ends where the mixer does; the tool says so rather than guessing.             |
| Fund tracing forward to cash-out points, following swaps and bridges.             | Cross-chain hops are reconstructed probabilistically and are marked as such.                         |
| Counterparty listing with known entities (exchanges, mixers, bridges).            | Scores on freshly reported addresses lag until attribution catches up.                               |
| Free keyless API and an MCP server for use inside AI assistants.                  | <p><br></p>                                                                                          |
| Permanent citable address pages and published case write-ups.                     | <p><br></p>                                                                                          |

### Summary

PublicAML is useful in the collection and analysis stages of an investigation, when you have an address and need to know whether it is criminal and where its money went. However, it should be used alongside blockchain explorers and primary sources rather than treated as a standalone determination of criminality or ownership.

### Ownership

PublicAML, a registered US non-profit incorporated in Delaware, United States. It has no paid product and no investors; the project is run by its own team and funded independently. Contact: info@publicaml.org

### Ethical Considerations

* An address is not a person: a high score is exposure, not proof of wrongdoing by its owner.
* Victims often score high because they received funds from an attacker - check direction before drawing conclusions.
* Published accusations can cause real harm, so verify a finding against the source before citing it.
* Avoid linking addresses to identities from other sources without a lawful basis.
* Screening results are advisory; treat them as a lead, not a verdict.

### Related Tools:

* [Arkham Intelligence](arkham.md)
* Breadcrumbs
* [Block Explorer](block-explorer.md)
* [Etherscan](etherscan.md)
* MistTrack (SlowMist)
* Chainalysis and TRM Labs

#### Sources

* [https://publicaml.org/](https://publicaml.org/)&#x20;
* [https://publicaml.org/directory/](https://publicaml.org/directory/)&#x20;
* [https://publicaml.org/api/](https://publicaml.org/api/)&#x20;
* [https://publicaml.org/news/2026-09-12-chainflip/](https://publicaml.org/news/2026-09-12-chainflip/)&#x20;
* [https://x.com/PublicAML](https://x.com/PublicAML)&#x20;



_With thanks to Denys Deputatov for submitting this tool to the OSINT Tool Library._
