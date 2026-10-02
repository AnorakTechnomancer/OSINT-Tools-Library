---
description: >-
  Tool Description: A browser-based defensive reconnaissance suite for blue-team
  operators and authorised penetration testers.
---

# Codename Sonar

| **Codename Sonar** | **Quick Overview**                                                                                                                                                                        |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URL                | [https://codenamesonar.app/](https://codenamesonar.app/)                                                                                                                                  |
| What it does       | Provides permission-first discovery and exposure validation for approved hosts, with TCP/UDP profiling, TLS and web reconnaissance, timing templates, and analyst-style briefing outputs. |
| How to use it      | Enter an approved target, choose a conservative recon profile, run the checks, review findings, and export or share the resulting briefing for remediation.                               |
| Cost               | Partially Free.                                                                                                                                                                           |
| Account required   | No account required to view the public site; access requirements may vary by deployment.                                                                                                  |
| Cookies            | First-party cookies for website functionality and legal/consent preferences.                                                                                                              |
| Ownership          | Artisan Technical Computer Services, LLC (Codename Sonar).                                                                                                                                |
| Use in Reporting   | Can document externally observable network, DNS, web, TLS and security characteristics of authorised infrastructure.                                                                      |

### What does Codename Sonar do?

Codename Sonar supports defensive host discovery and service-exposure review for approved environments. It combines TCP/UDP profiles, TLS and web reconnaissance, timing templates, and concise analyst briefings so blue teams and authorised testers can validate exposure and prioritise remediation.

**The lowdown:** It’s a defensive reconnaissance and attack-surface assessment tool, rather than a conventional passive OSINT search engine.&#x20;

**Important Note:** Targets must be systems the operator owns or has current written permission to test.&#x20;

### How to Use:

**1. Define the authorised scope and target assets then open Codename Sonar and choose a conservative TCP/UDP, TLS, or web recon profile.**

<img src="../.gitbook/assets/unknown (610).png" alt="" height="303" width="602">

**2. Run the checks only against approved systems, then review evidence and analyst briefing output.**

<img src="../.gitbook/assets/unknown (611).png" alt="" height="300" width="602">

**3. Record findings and remediation actions. Never use it for unauthorised scanning.**

### Cost

* [ ] Free
* [x] Partially Free
* [ ] Paid

Free tier available alongside Pro subscription.

## Data Processing

### Account Required:

* [x] Yes
* [x] No

No account required to view the public site; access requirements may vary by deployment.

### Cookies:&#x20;

Codename Sonar uses first-party cookies for website functionality and legal/consent preferences. The 2026\_codename\_sonar\_tos cookie stores the version of the Terms of Service accessed and the associated access timestamp. The captured \_\_cf\_bm cookie belongs to .grok.com and is a Cloudflare Bot Management/security cookie used to help distinguish legitimate browser activity from automated traffic.

### Use in Reporting

Use cases include:

* Authorised attack-surface inventory.
* Service exposure validation.
* TLS/web review.
* Remediation documentation for blue teams.&#x20;

**Example:** Assess approved company assets after a change, then attach the resulting briefing to an internal ticket. Do not scan third-party systems without permission.

| **Capabilities**                                                  | **Limitations**                                                                                         |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Defensive host discovery within approved scope.                   | Requires explicit authorisation and a defined scope.                                                    |
| TCP and UDP service profiling.                                    | Results depend on target configuration and network visibility.                                          |
| TLS and web reconnaissance signals.                               | Not a substitute for a complete penetration test or asset inventory.                                    |
| Conservative timing templates.                                    | Findings should be validated before remediation decisions.                                              |
| Analyst-style exposure briefings.                                 | Running active scans can generate traffic, trigger IDS/IPS alerts or potentially affect target systems. |
| Permission-first workflows for blue teams and authorised testers. | Some reporting, archival and export capabilities are restricted to the paid tier.                       |

### Summary

Codename Sonar best fits the discovery → collection → verification → analysis stages of the OSINT workflow, with particular value for technical reconnaissance and external attack-surface assessment. It can then support reporting by providing structured evidence of publicly observable infrastructure, services, and security characteristics.

### Ownership

Owned and maintained by Artisan Technical Computer Services, LLC for Codename Sonar. Product site: https://codenamesonar.app. It is presented here as a defensive tool for authorized blue-team and assessment workflows.

### Ethical Considerations

* Obtain explicit permission and document scope before use.
* Minimise collection and avoid unnecessary personal data.
* Respect robots, rate limits, terms, and organisational policy.
* Validate findings before attributing exposure.
* Protect reports and redact sensitive details.
* Never use for harassment, intrusion, or unauthorised scanning.

### Related Tools:

* Nmap&#x20;
* Amass
* RustScan
* Httpx
* testssl.sh
* OWASAP Amass

#### Sources

[https://codenamesonar.app/ ](https://codenamesonar.app/)



_With thanks to Kent Borgos for submitting this tool to the OSINT Tool Library._
