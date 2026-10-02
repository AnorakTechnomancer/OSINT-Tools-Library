---
description: >-
  Tool Description: A reference database of file extensions commonly associated
  with executable, scripting, phishing, macro, and other potentially risky
  behaviours.
---

# Filesec.io

| **Filesec.io**   | **Quick Overview**                                                                                                                                                |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URL              | [https://filesec.io/](https://filesec.io/)                                                                                                                        |
| What it does     | Catalogues file extensions, their functions, operating systems, and potential security risks.                                                                     |
| How to use it    | Search for a file extension, function or operating system, then review the associated classification.                                                             |
| Cost             | Free.                                                                                                                                                             |
| Account required | No.                                                                                                                                                               |
| Cookies          | Primarily functional/security cookies.                                                                                                                            |
| Ownership        | The site is associated with security researcher mrd0x; its theme credits reference GTFOBins and LOLBAS.                                                           |
| Use in Reporting | Helps investigators explain why a file type may be suspicious, identify potentially dangerous extensions and support analysis of phishing/malware-related files.  |

### What does Filesec.io do?

Filesec.io is an encyclopedia of potentially malicious or abuse-prone file extensions. The current site allows users to search by file extension, function, or operating system.&#x20;

The database classifies extensions using categories including Executable, Script, Phishing, Double Click, Macros and File Archiver.

**The lowdown:** It’s described as a central resource for malicious file extensions, risks, operating systems and mitigations.&#x20;

### How to Use:

**1. Identify the file extension you want to investigate, for example .lnk, .iso, .docm, .hta or .ps1 then search for the extension on the site or search by function/operating system using the site's search syntax.**

<img src="../.gitbook/assets/unknown (604).png" alt="" height="439" width="602">

**You can also use filters such as ‘script’ and ‘phishing’ to pull up results for commonly used extensions:**

<img src="../.gitbook/assets/unknown (605).png" alt="" height="371" width="602">

**2.  Record the extension's classifications and use the information as context when analysing the actual file, campaign or incident. Where possible, corroborate the assessment with malware-analysis or threat-intelligence sources.**&#x20;

### Cost

* [x] Free
* [ ] Partially Free
* [ ] Paid

## Data Processing

### Account Required:

* [ ] Yes
* [x] No

### Cookies:&#x20;

Filesec.io uses Laravel application cookies, including laravel\_session and XSRF-TOKEN. laravel\_session maintains the user's application session, while XSRF-TOKEN provides protection against Cross-Site Request Forgery (CSRF) attacks. These are primarily functional and security cookies rather than advertising or analytics cookies.

### Use in Reporting

Filesec.io can be used to:

* Identify potentially risky or security-relevant file extensions.
* Determine whether a file extension is associated with executable, scripting, phishing or macro functionality.
* Assess the potential significance of unfamiliar file types encountered during an investigation.
* Support analysis of suspicious email attachments, downloaded files or files associated with phishing campaigns.
* Compare file-extension characteristics across different operating systems.
* Provide context when explaining potentially malicious file types in an investigative report.
* Support technical findings alongside malware-analysis, sandboxing and other independent sources.

| **Capabilities**                                                                        | **Limitations**                                                                            |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Large catalogue of file extensions associated with security-relevant behaviour.         | It does not analyse or sandbox the actual file submitted by an investigator.               |
| Searchable by extension, function and operating system.                                 | Classifications provide context rather than a complete threat assessment.                  |
| Classifies extensions into categories such as executable, script, phishing and macros.  | It does not replace antivirus, sandboxing, reverse engineering or malware-analysis tools.  |
| Useful for identifying potentially risky or unusual file types.                         | Information may not capture every new or emerging abuse technique immediately.             |
| Covers Windows, macOS and Linux file types.                                             | A file extension alone does not establish that a file is malicious.                        |
| Useful as a quick reference during cyber/OSINT investigations.                          | Some classifications are broad and require technical interpretation and corroboration.     |

### Summary

Filesec.io is particularly useful during initial triage when an investigator encounters an unfamiliar or suspicious file extension and needs to understand its potential significance before conducting deeper analysis.

**Note:** It should be treated as a reference source rather than a malware-detection service.

### Ownership

Filesec.io is associated with the security researcher [mrd0x.](https://x.com/mrd0x)

### Ethical Considerations

* Use Filesec.io to understand and investigate potentially malicious files rather than to facilitate malicious file delivery.
* Do not execute suspicious files on a normal workstation simply because their extension appears in the database.
* Treat file-extension classifications as indicators, not proof of maliciousness.
* Do not download or open suspicious samples unnecessarily.
* When reporting findings, distinguish between the file extension and the actual behaviour of the file.
* Corroborate important conclusions with malware-analysis, sandboxing, vendor research or other authoritative sources.

### Related Tools:

* LOLBAS
* GTFOBins
* [VirusTotal](virustotal.md)
* MalwareBazaar

#### Sources

[https://filesec.io/\
https://x.com/mrd0x &#x20;](https://filesec.io/https://x.com/mrd0x)
