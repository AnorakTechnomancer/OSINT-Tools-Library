---
description: >-
  Tool Description : A terminal-based email-security auditing and controlled
  email-spoofing assessment toolkit.
---

# Postcard TUI

| Postcard TUI     | Quick Overview                                                                                                                                                                   |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URL              | [https://github.com/m0usem0use/PostcardTUI](https://github.com/m0usem0use/PostcardTUI)                                                                                           |
| What it does     | Combines SPF/DMARC spoofability audit + sending mechanism, portfolio audit, false-confidence detection, interactive compose, live-fire proof, DNS fixes                          |
| How to use it    | In the command line terminal, follow the steps & questions to audit any email & see if endpoints are spoofable, proceeds with crafted delivery of tests.                         |
| Cost             | Free.                                                                                                                                                                            |
| Account required | No.                                                                                                                                                                              |
| Cookies          | N/A                                                                                                                                                                              |
| Ownership        | Public GitHub repository maintained by m0usem0use.                                                                                                                               |
| Use in Reporting | Useful for documenting email-domain security weaknesses, demonstrating whether a spoofing weakness is practically exploitable, and providing before/after remediation evidence.  |

### What does Postcard TUI do?

PostcardTUI is an interactive terminal toolkit for inspecting email security postures (SPF & DMARC) and verifying mail server enforcement.

Most organisations assume their domain is protected from spoofing, but subtle misconfigurations in DNS can leave their brand wide open. POSTCARD automates the entire verification lifecycle: Inspect-->Score-->Validate.

**The lowdown:** It’s an email-security assessment and verification tool rather than a conventional OSINT collection platform.&#x20;

### How to Use:

**1. Obtain the PostcardTUI source from GitHub and run it with Python 3.10+ in the command line:**

<img src="../.gitbook/assets/unknown (641).png" alt="" height="181" width="602">

**2. Start with a passive DNS audit of domains that you own or have explicit permission to assess by choosing ‘Full audit’ from the menu. You can enter one domain or paste a list. Review results:**

<img src="../.gitbook/assets/unknown (642).png" alt="" height="168" width="602">

**3. Where authorised, use the interactive workflow to review a finding and conduct a controlled test against a seed inbox you control. Preserve the audit results, send log and resulting Authentication-Results as evidence, then re-run the audit after remediation to establish a before/after record.**

<img src="../.gitbook/assets/unknown (643).png" alt="" height="103" width="602">

**Note from developer:** Ideally, you want this program to live on a VPS somewhere and ask the hosting provider to open your port 25.  As you may already know, port 25 is mostly closed by default and can't be opened without request.  However, a simple email to the provider or interactive web chat, explaining your plan to host a web server.

### Cost

* [x] Free
* [ ] Partially Free
* [ ] Paid

## Data Processing

### Account Required:

* [ ] Yes
* [x] No

### Cookies:&#x20;

N/A

### Use in Reporting

PostcardTUI can be used to:

* Audit an organisation's SPF, DMARC and DKIM configuration.
* Identify domains with potentially ineffective email-authentication policies.
* Detect configurations that appear secure at first glance but contain weaknesses.
* Compare email-security posture across a portfolio of domains.
* Rank findings by severity for prioritisation.
* Produce CSV and Markdown audit reports.
* Preserve send logs and historical results as part of an assessment record.
* Demonstrate a suspected spoofing weakness through an authorised controlled test.
* Record the actual receiving behaviour of different email providers.
* Document remediation by comparing results before and after DNS changes.
* Provide technical evidence supporting a report about email impersonation risk.

**Note:** This is a brand new tool and the repository specifically describes the output as evidence-oriented: the intended workflow is to identify the weakness, demonstrate it in a controlled environment, and provide the domain owner with the DNS changes needed to remediate it.

| **Capabilities**                                                   | **Limitations**                                                                                                                                  |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Audits SPF, DMARC and DKIM-related configuration.                  | Requires appropriate DNS resolution and access to the relevant domain information.                                                               |
| Supports controlled live-fire validation of suspected weaknesses.  | Strict Port 25 dependency for live verification.                                                                                                 |
| Supports portfolio-scale domain auditing and severity ranking.     | No automated DKIM auditing.                                                                                                                      |
| Safe dry-run mode.                                                 | A DNS configuration finding does not necessarily establish that a particular person or organisation has actually been spoofed.                   |
| Gateway enforcement check.                                         | SMTP delivery behaviour varies between receiving providers and can be affected by reputation, filtering and other factors.                       |
| Controlled pacing.                                                 | The tool focuses on email-authentication/security posture rather than broader OSINT such as identifying people, organisations or relationships.  |
| Zero dependencies.                                                 | <p><br></p>                                                                                                                                      |

### Summary

POSTCARD is an automated, zero-friction terminal toolkit that bridges the gap between passive DNS theory and real-world email gateway enforcement. It transforms complex SPF and DMARC audits into an intuitive, guided workflow that gives administrators and security teams absolute clarity on their email defenses. It fits best in the verification stage of the OSINT workflow and is potentially particularly relevant to cyber investigations, corporate due diligence, phishing investigations, and security reporting.

### Ownership

Public GitHub repository maintained by [m0usem0use.](https://github.com/m0usem0use)

### Ethical Considerations

* Start with passive DNS analysis wherever possible.
* Obtain written authorisation before conducting live-fire tests.
* Send only to controlled test addresses.
* Keep test volume to the minimum necessary.
* Preserve timestamps, DNS records and test results.
* Distinguish a configuration weakness from evidence that an actual attack occurred.
* Avoid testing third-party domains simply because they appear in an investigation.
* Treat receiving-provider behaviour as an observation rather than a universal guarantee.

### Related Tools:

* swaks
* Spoofcheck
* Spoofy
* checkdmarc

#### Sources

[https://github.com/m0usem0use/PostcardTUI](https://github.com/m0usem0use/PostcardTUI)&#x20;

[https://github.com/m0usem0use](https://github.com/m0usem0use)&#x20;



_With thanks to m0usem0use for submitting this tool to the OSINT Tool Library._
