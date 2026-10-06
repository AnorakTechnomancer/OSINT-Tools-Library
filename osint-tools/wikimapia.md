---
description: >-
  Tool Description : A collaborative online map that combines satellite imagery
tool:
  name: Wikimapia
  url: https://wikimapia.org/
  status: active
  categories:
    - geolocation
  inputs:
    - location
  capabilities:
    - collaborative-mapping
    - place-labels
    - satellite-imagery
  pricing:
    model: free
    free_tier: Map browsing and user-contributed place information.
    paid_unlocks: []
    price: free
  account_required: optional
  access_methods:
    - online-web
  implementation:
    - hosted-service
  open_source: false
  geographic_scope: global
  last_verified: 2026-10-06
---

# Wikimapia

| **Wikimapia**    | **Quick Overview**                                                                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URL              | [https://wikimapia.org/](https://wikimapia.org/)                                                                                                                                |
| What it does     | It lets users add and edit detailed information about places around the world on an interactive map.                                                                            |
| How to use it    | Search for a location or manually explore the map. Click on highlighted areas to view user-generated descriptions, categories, and sometimes photos.                            |
| Cost             | Free.                                                                                                                                                                           |
| Account required | No, but creating an account allows editing and contributing.                                                                                                                    |
| Cookies          | Uses standard web cookies for functionality and analytics.                                                                                                                      |
| Ownership        | Owned by Wikimapia Ltd. and originally founded by Russian developer and internet entrepreneurs, [Alexandre Koriakine](https://x.com/thewikimapia?lang=ar) and Evgeniy Saveliev. |
| Use in Reporting | Can provide context about locations, including names, historical use, and local knowledge.                                                                                      |

### What does Wikimapia do?

A collaborative online map that combines satellite imagery with user-added information about places around the world. Users can outline buildings or areas and add descriptions, categories (e.g., school, military base, factory), and sometimes links or photos. Think of it as a mix between a map and a wiki, where people label buildings, landmarks, and areas.

**The lowdown:** It’s a useful OSINT tool for identifying places that might not appear clearly on other mapping platforms.

### How to Use:

1. **Go to the website and enter a location in the search bar, or zoom in manually on the map.**

<figure><img src="../.gitbook/assets/unknown (63).png" alt=""><figcaption></figcaption></figure>

\
**2. Look for outlined shapes on the map—these represent user-identified locations. Click on them to open an information box.**

For example, we clicked on St James’ Park, London, to reveal the below:

<figure><img src="../.gitbook/assets/unknown (64).png" alt=""><figcaption></figcaption></figure>

\
**3. Review the details provided (name, description, category), and cross-check with other sources like satellite imagery or news reports.**

### Cost

* [x] Free
* [ ] Partially Free
* [ ] Paid

## Data Processing

### Account Required:

* [x] Yes
* [x] No

Yes to edit/add content. No to view content.

### Cookies:&#x20;

The site uses basic cookies for site functionality, preferences, and analytics.

### Use in Reporting

Wikimapia can help:

* Identify buildings or areas of interest.
* Provide local or historical context.
* Support geolocation investigations.

As a real-world example, [in open source cases related to the Yemeni conflict](https://eprints.ncrm.ac.uk/id/eprint/4545/1/Bellingcat%E2%80%99s%20Yemen%20Project.pdf?), researchers cited Wikimapia data (e.g. pre‑conflict tags for buildings) as part of investigations to correct misreported target locations in airstrike analyses.

For example, investigation materials showed that a building commonly reported as the “Presidential Palace” hit in a Yemeni strike had been tagged on Wikimapia as a different administrative building prior to the event. This helped analysts challenge initial reporting based on ambiguous claims and imagery.&#x20;

| **Capabilities**                            | **Limitations**                                        |
| ------------------------------------------- | ------------------------------------------------------ |
| Crowd-sourced location data.                | Information may be inaccurate or outdated.             |
| Identifies obscure/niche locations.         | Not regularly moderated.                               |
| Useful for geolocation and mapping.         | Coverage varies depending on user contributions.       |
| Provides contextual descriptions of places. | Limited official verification of content.              |
| Easy to use with no login required.         | The interface is less modern than other mapping tools. |

### Summary

Wikimapia is a simple but powerful OSINT mapping tool that provides user-generated insights into locations worldwide. It’s best used as a starting point for location-based research, with findings verified using other sources.

### Ownership

Wikimapia Ltd. is a private company, originally founded by Russian developer and internet entrepreneurs, [Alexandre Koriakine](https://x.com/thewikimapia?lang=ar) and Evgeniy Saveliev on 24 May 2006.

### Ethical Considerations

* Be cautious when using unverified, crowd-sourced data.
* Avoid relying on it as a sole source for critical reporting.
* Respect privacy when investigating residential or sensitive locations.
* Consider potential misinformation or bias in user contributions.



### Related Tools:

* Google Maps
* Google Earth
* [Apple Maps](apple-maps.md)
* OpenStreetMap
* Mapillary



#### Sources

[https://wikimapia.org/](https://wikimapia.org/)&#x20;

[https://bellingcat.gitbook.io/toolkit/more/all-tools/wikimapia](https://bellingcat.gitbook.io/toolkit/more/all-tools/wikimapia) &#x20;

[https://x.com/thewikimapia?lang=ar](https://x.com/thewikimapia?lang=ar)

