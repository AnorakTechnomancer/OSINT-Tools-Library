---
description: >-
  Tool Description : A browser-based tool for inspecting media provenance,
  without uploading files, by reading C2PA Content Credentials locally in the
  browser.
---

# C2PA Lab

| **C2PA Lab**     | **Quick Overview**                                                                                                                                        |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URL              | [https://c2palab.com/](https://c2palab.com/)                                                                                                              |
| What it does     | Inspects C2PA manifests in images and videos and shows verification state, provenance timeline, ingredients, and signer/issuer details from the manifest. |
| How to use it    | Open the site, drop or select a JPEG, PNG, WebP, AVIF, MP4, or MOV file up to 200 MB, then review the credential evidence and manifest details.           |
| Cost             | Free with no ads or signup.                                                                                                                               |
| Account required | No.                                                                                                                                                       |
| Cookies          | Google Analytics.                                                                                                                                         |
| Ownership        | C2PA Lab; the site identifies itself as an independent tool and not affiliated with C2PA.                                                                 |
| Use in Reporting | Useful for verifying and documenting digital provenance, Content Credentials, recorded edits, ingredients, and signing information in images and video.   |

### What does CP2A Lab do?

C2PA Lab is a free web tool for inspecting C2PA Content Credentials and digital provenance in images and videos. It reads the file locally with WebAssembly and reports what the manifest records: verification state, provenance timeline, ingredient references, recorded actions, and signer/issuer details.&#x20;

A Manifest Viewer exposes the manifest store, active manifest, claims, assertions, and JSON; a Metadata Inspector presents selected fields in a structured table. A Proof Card can be rendered locally as a 1200x630 PNG summary.

**The lowdown:** It provides a way to examine what a C2PA-compatible system has cryptographically recorded about a piece of media, rather than relying solely on conventional metadata or visual inspection.&#x20;

### How to Use:

**1. Open https://c2palab.com/ then drop or choose a supported media file up to 200 MB.**

<img src="../.gitbook/assets/unknown (612).png" alt="" height="600" width="602">

**2. Review the evidence view for verification state and manifest-recorded provenance.**

<img src="../.gitbook/assets/unknown (613).png" alt="" height="435" width="602">

**3. For technical review, open Manifest Viewer / Metadata Inspector.**

<img src="../.gitbook/assets/unknown (614).png" alt="" height="308" width="602">

**4. Use the public example files if testing the workflow:**

<img src="../.gitbook/assets/unknown (615).png" alt="" height="295" width="602">

### Cost

* [x] Free
* [ ] Partially Free
* [ ] Paid

## Data Processing

### Account Required:

* [ ] Yes
* [x] No

### Cookies:&#x20;

C2PA Lab uses Google Analytics cookies, including \_ga and \_ga\_70L9YB69CY, to distinguish visitors and measure website/session activity.&#x20;

### Use in Reporting

C2PA Lab can be used to:

* Verify whether an image or video contains C2PA Content Credentials.
* Examine cryptographically signed provenance associated with digital media.
* Identify recorded creation, editing or production actions.
* Identify source or ingredient files referenced by a provenance record.
* Examine signer, issuer, certificate and signature information where available.
* Compare provenance information with claims made about how or where media was produced.
* Document validation failures, hash mismatches or other provenance issues.
* Establish whether provenance evidence remains attached to a particular copy of a file.
* Support fact-checking and verification of photographs, videos and potentially synthetic media.
* Preserve technical provenance findings as part of an investigative evidence trail

**Note:** A valid credential supports statements about recorded provenance and cryptographic binding, but absence of C2PA is not evidence that content is AI-generated.&#x20;

| **Capabilities**                                                                                                   | **Limitations**                                                                              |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| Local browser inspection of C2PA Content Credentials.                                                              | Requires media to contain a C2PA manifest to return credential evidence.                     |
| Supports JPEG, PNG, WebP, AVIF, MP4, and MOV up to 200 MB.                                                         | Cannot prove that all real-world claims in a manifest are true.                              |
| Shows verification state, provenance timeline, recorded actions, ingredient references, and signer/issuer details. | It’s not an AI detector and cannot identify manipulated content without recorded provenance. |
| Manifest Viewer exposes manifest store, claims, assertions, and JSON.                                              | Absence of C2PA data does not mean content is AI-generated.                                  |
| Manifest Viewer exposes manifest store, claims, assertions, and JSON.                                              | File inspection workflow does not replace full forensic analysis or chain-of-custody review. |
| Proof Card export rendered locally as a 1200x630 PNG.                                                              | <p><br></p>                                                                                  |

### Summary

C2PA Lab is a strong option for the provenance/content-credential step of media verification when a file may contain C2PA data. Its’ main advantage is local inspection and manifest-level transparency however only recorded evidence can be shown, with no inference about authenticity or AI generation.

### Ownership

C2PA Lab; the site identifies itself as an independent tool and not affiliated with C2PA.

The site's [privacy policy](https://c2palab.com/privacy/) provides a contact address at hello@c2palab.com, while a current independent corporate ownership structure is not clearly identified on the site.

### Ethical Considerations

* Treat C2PA evidence as provenance evidence, not proof of truth or authenticity.
* Do not infer AI generation from absent credentials.
* Preserve source files and avoid basing serious published claims only on one verification signal.
* Be careful with sensitive media and personal data embedded in files; C2PA Lab keeps selected files local during inspection but cannot control downstream handling after download.

### Related Tools:

* Content Credentials Verify
* InVID / WeVerify verification plugin
* ExifTool&#x20;
* Google SynthID

#### Sources

[https://c2palab.com/](https://c2palab.com/)&#x20;

[https://c2palab.com/privacy/](https://c2palab.com/privacy/)&#x20;

[https://c2palab.com/about/](https://c2palab.com/about/)&#x20;

[https://c2palab.com/guides/](https://c2palab.com/guides/)&#x20;

[https://c2palab.com/c2pa-manifest-viewer/](https://c2palab.com/c2pa-manifest-viewer/)&#x20;

[https://c2palab.com/c2pa-metadata/](https://c2palab.com/c2pa-metadata/) <br>

_With thanks to C2PA Lab for submitting this tool to the OSINT Tool Library._

\
<br>
