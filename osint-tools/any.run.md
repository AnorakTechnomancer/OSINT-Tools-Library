---
description: >-
  Tool Description: An interactive cloud-based malware-analysis sandbox and
  threat-intelligence platform.
---

# ANY.RUN

| **ANY.RUN**      | **Quick Overview**                                                                                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| URL              | [https://app.any.run/](https://app.any.run/)                                                                                                                                         |
| What it does     | Dynamically analyses suspicious files, URLs, and malware in isolated virtual environments and records their behaviour.                                                               |
| How to use it    | Create an analysis, upload a suspicious file/submit a URL, select the appropriate sandbox environment, then observe the results.                                                     |
| Cost             | Partially Free.                                                                                                                                                                      |
| Account required | Yes for creating analyses and full platform functionality.                                                                                                                           |
| Cookies          | Google Analytics/advertising measurement, consent management, and session/marketing attribution cookies.                                                                             |
| Ownership        | ANYRUN FZCO, a privately held cybersecurity company headquartered in Dubai Silicon Oasis. Founder and CEO is Aleksey Lapshin.                                                        |
| Use in Reporting | Analyse suspicious files and URLs, identify malware behaviour and IOCs, investigate phishing and malicious infrastructure, and produce technical evidence for cyber investigations.  |

### What does ANY.RUN do?

ANY.RUN provides an interactive malware sandbox in which suspicious files, URLs, and other content can be executed in controlled virtual environments.

Unlike a purely automated sandbox, you can interact with the virtual machine while the analysis is running and observe processes, network traffic, files, screenshots, and other activity. The platform can also map observed behaviour to MITRE ATT\&CK techniques and generate analysis reports, alongside providing a large public database of malware-analysis submissions.&#x20;

**The lowdown:** It’s ideal for quickly identifying and analysing suspicious files, URLs, malware behaviour and associated IOCs in a safe sandbox.

### How to Use:

**1. Create an ANY.RUN account and start a new analysis.** (Note: You’ll need a business email address to sign up). **Upload the suspicious file or enter the URL you want to investigate, then select the appropriate virtual environment, such as Windows, Linux or Android.**

<img src="../.gitbook/assets/unknown (592).png" alt="" height="763" width="602">

**2. Examine the resulting IOCs, process tree, network activity and other findings.**

<img src="../.gitbook/assets/unknown (593).png" alt="" height="293" width="602">

**3. Save or export the relevant report and independently investigate important indicators using additional sources such as VirusTotal, URLScan, OTX, WHOIS/RDAP, passive DNS and malware-analysis reports.**

<img src="../.gitbook/assets/unknown (594).png" alt="" height="417" width="602">

### Cost

* [ ] Free
* [x] Partially Free
* [ ] Paid

Free Community plan with paid Hunter and Enterprise plans providing additional functionality and private analysis.

## Data Processing

### Account Required:

* [x] Yes
* [ ] No

Yes for creating analyses and full platform functionality.

### Cookies:&#x20;

The site uses a combination of consent, analytics, advertising and referral/measurement cookies.

\_ga, \_ga\_53KB74YDZR and FPGSID are associated with Google Analytics and support visitor/session activity measurement. \_gcl\_au is associated with Google's advertising/conversion-measurement infrastructure. cc\_cookie stores cookie-consent preferences and timestamps. gbuuid is a pseudonymous session/visitor identifier, although its precise function cannot be established from the cookie name alone. utm\_parameters records referral information; in this capture it identifies Google as the traffic source.&#x20;

### Use in Reporting

ANY.RUN can be used to:

* Analyse suspicious files, documents, scripts and executables in an isolated environment.
* Investigate suspicious URLs and phishing pages.
* Identify malware behaviour that is not obvious from static inspection.
* Identify domains, IP addresses, URLs and file hashes associated with malicious activity.
* Investigate process trees and relationships between executed programs.
* Examine DNS, HTTP/HTTPS and other network activity generated by a suspicious sample.
* Identify persistence mechanisms, dropped files and other system changes.
* Map observed behaviour to MITRE ATT\&CK techniques where available.
* Investigate malware families and compare new samples with previous public submissions.
* Search historical public analyses using hashes, domains, IP addresses or MITRE ATT\&CK techniques.
* Produce technical reports containing screenshots, IOCs and behavioural information.

As a working example, researchers used ANY.RUN sandbox environments to record and analyse the activity of [suspected DPRK IT workers ](https://any.run/cybersecurity-blog/lazarus-group-it-workers-investigation-part-two/)during a covert investigation.&#x20;

Further use cases can be found [here. ](https://www.socinvestigation.com/malware-analysis-use-cases-with-any-run-sandbox/)

| **Capabilities**                                                                    | **Limitations**                                                                 |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Analyses suspicious files, URLS, and malware in a controlled sandbox.               | Sandbox behaviour may differ from what occurs on a real victim system.          |
| Captures processes, network connections, DNS requests, and dropped files.           | Malware can detect and evade sandbox environments.                              |
| Extracts useful IOCs including IPs, domains, URLs, and file hashes.                 | Automated detections can produce false positives or miss behaviour.             |
| Maps observed behaviour to MITRE ATT\&CK techniques.                                | Public analyses may be incomplete, outdated, or incorrectly classified.         |
| Provides searchable public sandbox reports for comparison and historical research.  | Advanced features, longer analysis, and private submissions require paid plans. |
| Supports screenshots, reports, and technical evidence for investigation workflows.  | A sandbox result alone does not prove attribution, intent, or maliciousness.    |
|                                                                                     |                                                                                 |

### Summary

ANY.RUN’s strongest role within an OSINT investigation is technical analysis and verification, and it’s especially valuable after an investigator has collected a suspicious file, URL, domain, IP address or other technical artefact and needs to establish what it does and what additional indicators it produces.

For cyber investigations, ANY.RUN can therefore sit between initial evidence collection and broader threat-intelligence investigation, with outputs subsequently checked against OTX, VirusTotal, URLScan, passive DNS, WHOIS/RDAP and other sources.

### Ownership

ANYRUN FZCO, a privately held cybersecurity company headquartered in Dubai Silicon Oasis. The Founder and CEO is [Aleksey Lapshin](https://www.linkedin.com/in/aleksey-lapshin/).

### Ethical Considerations

* Never upload confidential or sensitive material to a public analysis as public submissions and their reports can be accessed by other users.
* Treat malware samples as potentially dangerous even when analysing them in a sandbox.
* Do not interact with live malicious infrastructure outside the controlled environment unless you have appropriate authorisation.
* Do not assume that a sandbox verdict alone proves attribution to a particular threat actor.
* Be aware that malware may behave differently depending on the sandbox environment and may employ anti-analysis techniques.
* When using public reports as evidence, distinguish between ANY.RUN's observed behaviour, the contributor's interpretation and your own conclusions.

### Related Tools:

* [AlienVault OTX](alien-vault-otx.md)
* [VirusTotal](virustotal.md)
* [urlscan.io](urlscan.md)
* MalwareBazaar
* Abuse.ch

#### Sources

[https://app.any.run/](https://app.any.run/)&#x20;

[https://any.run/cybersecurity-blog/lazarus-group-it-workers-investigation-part-two/](https://any.run/cybersecurity-blog/lazarus-group-it-workers-investigation-part-two/)&#x20;

[https://www.socinvestigation.com/malware-analysis-use-cases-with-any-run-sandbox/](https://www.socinvestigation.com/malware-analysis-use-cases-with-any-run-sandbox/)&#x20;

[https://www.linkedin.com/in/aleksey-lapshin/](https://www.linkedin.com/in/aleksey-lapshin/)&#x20;
