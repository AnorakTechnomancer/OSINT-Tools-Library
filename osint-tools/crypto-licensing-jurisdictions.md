---
description: >-
  Tool Description : An open, versioned dataset from Jagelski & Partners
  containing structured information on crypto-asset licensing regimes across 50
  jurisdictions.
---

# Crypto Licensing Jurisdictions

| **Crypto Licensing Jurisdictions** | **Quick Overview**                                                                                                                                                                          |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URL                                | [https://jagelski.com/data/](https://jagelski.com/data/)                                                                                                                                    |
| What it does                       | Publishes the headline crypto-licensing fields for 50 jurisdictions as a dated CSV and JSON release with a field dictionary, checksum and DOI.                                              |
| How to use it                      | Download the CSV or JSON from the page, or filter the same data in the live comparator at [https://jagelski.com/compare-crypto-licensing/](https://jagelski.com/compare-crypto-licensing/)  |
| Cost                               | Free (CC BY 4.0, attribution required).                                                                                                                                                     |
| Account required                   | No.                                                                                                                                                                                         |
| Cookies                            | Google Analytics, Microsoft Clarity, its own attribution tracking, and a consent-management cookie.                                                                                         |
| Ownership                          | Jagelski & Partners OÜ (Estonia, registry code 17569307).                                                                                                                                   |
| Use in Reporting                   | Useful for researching and comparing crypto licensing, regulatory frameworks, taxation, capital requirements and market-access conditions.                                                  |

### What does Crypto Licensing Jurisdictions do?

Crypto Licensing Jurisdiction is a regulatory and corporate OSINT dataset that has one record per jurisdiction covered by the Jagelski & Partners crypto-licensing guides (50 records, worldwide), including jurisdictions whose recorded position is that no licensing regime exists.&#x20;

The fields include the regime name and model, the competent regulator, the legal framework, the minimum capital in the native currency, the licence term, the application timeline in months, the corporate-tax headline rate and model, the FATF status, the FATF-style regional body, retail access, EU passporting and a Year-1 cost band.

Each release is a dated CSV and JSON file with a checksum, a field dictionary and a citation line, and carries a Zenodo DOI (10.5281/zenodo.22334373 for the 2026-09-05 release; the concept DOI 10.5281/zenodo.22334372 always resolves to the newest version). Six columns are the publisher's own classifications (region, legal system, licence model, capital basis, corporate-tax model, retail access); EU passporting is a legal conclusion.

Each record comes from a jurisdiction guide on the same site that cites the operative instrument and the regulator's own register. A live comparator filters the same data and is updated continuously, so it may be ahead of the latest file.

**The lowdown:** It can help an investigator quickly compare the regulatory environment surrounding crypto businesses across multiple jurisdictions without manually extracting the same information from dozens of jurisdiction pages.&#x20;

### How to Use:

**1. Open https://jagelski.com/data/ and download the CSV or JSON of the current release.**

<img src="../.gitbook/assets/unknown (623).png" alt="" height="763" width="602">

**2. Find the jurisdiction in question and read the regime, the competent regulator and the legal framework.**

<img src="../.gitbook/assets/unknown (624).png" alt="" height="189" width="602">



**3. Open the jurisdiction guide on the site for the cited instrument and the link to the regulator's register. Check the company in that official register; the dataset tells you where to look, the register is the authoritative record.**

<img src="../.gitbook/assets/unknown (625).png" alt="" height="311" width="602">

<img src="../.gitbook/assets/unknown (626).png" alt="" height="201" width="602">

**Note:** To compare several jurisdictions, use the live comparator at [https://jagelski.com/compare-crypto-licensing/](https://jagelski.com/compare-crypto-licensing/)  and filter by capital, timeline, tax or FATF status.

**Additional Note:** When citing, quote the release date and DOI.

### Cost

* [x] Free
* [ ] Partially Free
* [ ] Paid

(CC BY 4.0, attribution required).

## Data Processing

### Account Required:

* [ ] Yes
* [x] No

### Cookies:&#x20;

The site uses Google Analytics and Microsoft Clarity for website analytics, together with first-party attribution cookies.

&#x20;\_ga and \_ga\_8WHEQZDKNM are Google Analytics cookies used to measure visitor and session activity, while \_clsk is associated with Microsoft Clarity and helps analyse browsing sessions and user interactions. The first-party jag\_attr\_first and jag\_attr\_last cookies record referral, landing-page and timestamp information for first- and last-touch attribution. jagelski\_consent stores the visitor's cookie-consent choices. The MUID cookie, set on clarity.ms, is a Microsoft identifier associated with advertising/measurement and has greater cross-site tracking relevance.&#x20;

### Use in Reporting

Crypto Licensing Jurisdiction can be used for

* Checking whether a crypto business that claims to be licensed or registered is dealing with the right regulator, before searching that regulator's own register.
* Comparing minimum capital, application timelines and FATF status across jurisdictions for a story on where crypto firms choose to incorporate.
* Identifying jurisdictions that record no licensing regime for crypto-asset services.
* Citing a stable, versioned source with a DOI instead of a screenshot.

| **Capabilities**                                                                  | **Limitations**                                                                                               |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 50 jurisdictions, one record each, 21 columns defined in a field dictionary.      | Headline fields only; not legal advice and not a register of licensed firms.                                  |
| Names the competent regulator and legal framework for each jurisdiction.          | Each file is a snapshot: the release date is not a verification date.                                         |
| Minimum capital in native currency, licence term, application timeline in months. | The live comparator may be ahead of the latest file.                                                          |
| FATF status, FATF-style regional body, EU passporting and retail access,          | Six columns are the publisher's own classifications.                                                          |
| CSV and JSON with checksum, citation line and DOI.                                | Year-1 cost is a band, not a figure.                                                                          |
| Live comparator on the same site for filtering.                                   | Covers crypto licensing only; formation and banking comparators on the site are not yet released as datasets. |

### Summary

Crypto Licensing Jurisdictions is an open regulatory-data resource for crypto and financial OSINT, most useful at the orientation and verification stage of the OSINT workflow: working out which regulator and regime apply before checking a company in the official register. However, important findings should be checked against the relevant regulator, legislation or official register.

### Ownership

Jagelski & Partners OÜ, a company registered in Estonia (registry code 17569307), founded in 2026 by [Richard Jagelski](https://www.linkedin.com/in/jagelski/). The firm writes scoping briefs for crypto, fintech and high-risk businesses and introduces each case to an independent specialist; it publishes jurisdiction guides, comparison tools and this open dataset on jagelski.com.

### Ethical Considerations

* The dataset contains no personal data: it describes regulators, laws and requirements, not individuals or firms.
* Verify any claim about a named company in the regulator's own register before publishing; the dataset does not state whether a specific firm is licensed.
* Regulatory positions change: quote the release date and DOI and check the current guide or regulator before relying on a value.
* The publisher is a commercial consultancy; treat its classification columns as its own judgement.

### Related Tools:

* Business registers in EU countries (European e-Justice Portal)
* ESMA interim MiCA register of crypto-asset service providers
* FATF lists of high-risk and other monitored jurisdictions
* [OpenSanctions](open-sanctions.md)
* [OpenCorporates](opencorporates.md)

#### Sources

[https://jagelski.com/data/](https://jagelski.com/data/)&#x20;

[https://jagelski.com/](https://jagelski.com/) &#x20;

[https://www.linkedin.com/in/jagelski/](https://www.linkedin.com/in/jagelski/)&#x20;

[https://doi.org/10.5281/zenodo.22334373](https://doi.org/10.5281/zenodo.22334373)&#x20;



_With thanks to Richard Jagelski for submitting this tool to the OSINT Tool Library._
