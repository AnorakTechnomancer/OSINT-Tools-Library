---
description: >-
  Tool Description: A community-powered cyber threat intelligence platform that
  collects, shares and analyses IOCs, malware info, threat actors, domains, IP
  addresses, URLs and other threat data.
---

# Alien Vault OTX

| **Alien Vault OTX** | **Quick Overview**                                                                                                                                                                                       |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URL                 | [https://otx.alienvault.com/](https://otx.alienvault.com/)                                                                                                                                               |
| What it does        | Provides open, community-generated cyber threat intelligence and searchable information about IOCs, malware, infrastructure and threats.                                                                 |
| How to use it       | Search an IP address, domain, hostname, URL, file hash or other indicator and examine associated Pulses, reputation and technical intelligence.                                                          |
| Cost                | Free for end users for non-commercial use.                                                                                                                                                               |
| Account required    | Yes for full functionality.                                                                                                                                                                              |
| Cookies             | Mainly advertising/analytics, session/measurement, and functional application cookies.                                                                                                                   |
| Ownership           | It’s part of LevelBlue's cybersecurity/threat-intelligence ecosystem.                                                                                                                                    |
| Use in Reporting    | Useful for investigating domains, IPs, hashes and other technical indicators, identifying links to malware or threat activity, corroborating cyber incidents, and developing threat-intelligence leads.  |

### What does Alien Vault OTX do?

AlienVault OTX is an open cyber threat-intelligence sharing platform. It aggregates and shares threat data contributed by security researchers and organisations, allowing investigators to search indicators and investigate their relationships with known threats.

Its central concept is the Pulse: a collection of related indicators and contextual information describing a threat, campaign, malware family, actor or other security event.

OTX can be queried for indicators such as IP addresses, domains, hostnames, URLs, file hashes, malware indicators, threat actors, campaigns, and IOCs.

**The lowdown:** Its greatest value is allowing you to take a technical indicator discovered elsewhere and determine whether it has known associations with other suspicious activity.&#x20;

### How to Use:

**1. Open AlienVault OTX and search for an indicator such as an IP address, domain, URL or file hash.**

<img src="../.gitbook/assets/unknown (590).png" alt="" height="73" width="382">

**2. Examine the resulting threat information, including associated Pulses, indicators, malware references, reputation information and other technical context.**

<img src="../.gitbook/assets/unknown (591).png" alt="" height="272" width="602">

**3. Follow relevant Pulses and associated indicators, then corroborate significant findings using independent sources such as malware-analysis reports, vendor research, WHOIS/RDAP, passive DNS, VirusTotal or other threat-intelligence platforms.**

### Cost

* [x] Free
* [ ] Partially Free
* [ ] Paid

Free for end users for non-commercial use.

## Data Processing

### Account Required:

* [x] Yes
* [ ] No

An account is required for full participation and features such as submitting intelligence. Public threat information can also be viewed through the platform.

### Cookies:&#x20;

Advertising/analytics, session/measurement, and functional application cookies were observed during our site session on 15 September 2026 although most were linked to LinkedIn rather than to Alien Vault itself.

### Use in Reporting

AlienVault OTX can be used to:

* Investigate suspicious IP addresses, domains, URLs and file hashes.
* Identify whether an indicator has previously been associated with known malicious activity.
* Identify relationships between indicators, malware, campaigns and threat actors.
* Investigate community-created Pulses relating to a particular cyber threat.
* Corroborate technical indicators discovered during a cyber investigation.
* Develop leads about malware infrastructure and command-and-control infrastructure.
* Support technical timelines by identifying when indicators were reported or associated with particular Pulses.
* Research cyber incidents and campaigns for background information in investigative or academic reporting.
* Provide machine-readable threat intelligence through OTX's API and STIX/TAXII functionality.
* Support threat-hunting investigations by identifying known indicators that can be checked against network or endpoint data.

As a real-world example, [Allegretta et al](https://pdf.core.ac.uk/corefilesystem/pdf/681/586722650.pdf?se=2026-09-15T11%3A59%3A03Z\&sp=r\&sv=2026-06-06\&sr=b\&rscd=inline%3B%20filename%3D%22586722650.pdf%22\&rsct=application/pdf\&sig=B2FekSB0/ZsNaZCDg0%2BvnizA04LGl8nRo/L7ddLnlSY%3D). used AlienVault OTX as a major public CTI source, collecting more than 115,000 attack reports/Pulses to study the quality of crowdsourced cyber-threat intelligence. The research was motivated partly by the increase in cyberattacks following Russia's invasion of Ukraine.&#x20;

| **Capabilities**                                                               | **Limitations**                                                                        |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| Searchable database of cyber-threat indicators and intelligence.               | Community-contributed information can vary considerably in quality and reliability.    |
| Investigate IP addresses, domains, URLs, hashes and other IOCs.                | Presence of an indicator in OTX does not by itself prove that it is malicious.         |
| Pulses group related indicators and contextual threat information.             | Pulses can contain incomplete, outdated or incorrectly attributed information.         |
| Community intelligence can provide early indications of emerging threats.      | Rapidly emerging information may not yet have been independently verified.             |
| API and STIX/TAXII functionality allows automated collection and integration.  | Technical integration requires additional knowledge and configuration                  |
| Can reveal relationships between indicators, malware and campaigns.            | Attribution to a specific actor or organisation requires substantially more evidence.  |

### Summary

OTX has been used AlienVault OTX provides access to community-generated information about malicious infrastructure, malware, campaigns and other cyber threats and has been used as a significant source of public cyber-threat intelligence in academic research, including research analysing more than 115,000 OTX attack reports/Pulses.

Its strongest role in an OSINT investigation is collection, verification and analysis as you can collect an IOC from another source, search it in OTX, identify related intelligence, then verify those findings against independent technical and documentary evidence.

### Ownership

AlienVault OTX was created by AlienVault and is now operated within the[ LevelBlue cybersecurity ecosystem. ](https://www.levelblue.com/blogs/levelblue-blog/introducing-levelblue-elevating-business-confidence-by-simplifying-security)The majority owner is WillJam Ventures; a cybersecurity-focused investment firm founded by [Bob McCullen](https://www.levelblue.com/company/leadership/bob-mccullen). AT\&T retains an ownership stake and board representation.

### Ethical Considerations

* Treat community-generated intelligence as leads rather than automatically verified facts.
* Do not assume that an OTX indicator proves criminal activity or malicious intent.
* Be particularly cautious when attributing infrastructure to a specific threat actor.
* Do not upload confidential, personal or sensitive material without first checking the applicable terms and permissions.
* Preserve the Pulse/indicator URL, observation date and relevant context when documenting findings.
* Distinguish between information supplied by OTX contributors and independently verified evidence.

### Related Tools:

* [VirusTotal](virustotal.md)
* [urlscan.io](urlscan.md)
* AbuseIPDB
* [Shodan](shodan.md)
* [Censys](censys.md)
* MalwareBazaar

#### Sources

[https://otx.alienvault.com/](https://otx.alienvault.com/)&#x20;

[https://pdf.core.ac.uk/corefilesystem/pdf/681/586722650.pdf?se=2026-09-15T11%3A59%3A03Z\&sp=r\&sv=2026-06-06\&sr=b\&rscd=inline%3B%20filename%3D%22586722650.pdf%22\&rsct=application/pdf\&sig=B2FekSB0/ZsNaZCDg0%2BvnizA04LGl8nRo/L7ddLnlSY%3D](https://pdf.core.ac.uk/corefilesystem/pdf/681/586722650.pdf?se=2026-09-15T11%3A59%3A03Z\&sp=r\&sv=2026-06-06\&sr=b\&rscd=inline%3B%20filename%3D%22586722650.pdf%22\&rsct=application/pdf\&sig=B2FekSB0/ZsNaZCDg0%2BvnizA04LGl8nRo/L7ddLnlSY%3D)&#x20;

[https://www.levelblue.com/blogs/levelblue-blog/introducing-levelblue-elevating-business-confidence-by-simplifying-security](https://www.levelblue.com/blogs/levelblue-blog/introducing-levelblue-elevating-business-confidence-by-simplifying-security)&#x20;

[https://www.levelblue.com/company/leadership/bob-mccullen](https://www.levelblue.com/company/leadership/bob-mccullen)
