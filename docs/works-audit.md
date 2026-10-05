# Works archive audit — Step 1a

Date: 2026-10-04 · Source: Drive folder **Our Project** (54 top-level entries; 4 non-project) · Branch `works-video-aman`

**Method.** All 54 top-level folders and every subfolder were enumerated through the Google Drive connector (file name, id, MIME type, size). Duplicates were matched by filename+size within each merged project (Drive metadata exposes no MD5, so byte-hashing would require downloading all ~2 GB; size+name matching reproduced every duplicate you had spotted). Eleven sample images across the trees were downloaded and inspected visually to classify photos vs renders and finished vs progress.

**Counts.** 54 distinct projects: 8 already on the site, 14 recommended publish, 31 need your decision, 1 skip (empty folder).


## Key findings

1. **“1 Photo Render” is a mix of real photos and AI-generated images.** Several subfolders contain
   ChatGPT/Gemini images (one file is literally named `ChatGPT Image Aug 30, 2026…png`; others carry “By Claude”
   names): Shiseido ×2, Bobbi Brown Bangkae, Gucci (Pinklao & Mega Bangna sets look AI-stylised), Chanel
   Cheangwattana/Siam Paragon, Rouge Coco, Blue Bottle. Others are genuine photographs (Paul Smith, Pop Mart,
   Panpuri ×2, Hourglass Khonkaen, CPB Dusit, Chanel Chiangmai). **Recommendation: never publish the AI images as
   finished work**; each PR image used in Step 1b will be verified visually first.
2. **“1 Wiriwork” is genuine site/fixture photography** (CDS fixtures, Another Story, Sunnies ×2 — the Sunnies
   sets duplicate the top-level folders file-for-file by size). What “Wiriwork” denotes is still unknown — please
   tell me (internal team? sister brand, cf. Wiribed?).
3. **Empty folders:** top-level `Chanel emsphere` (!), `Hourglass Central Pinklao`, `Sunnies central world`
   (lowercase), and PR subfolders `Gucci Central Dusit`, `Chanel Central Udon`, `Pralet EmQuartier`.
4. **Brand names resolved visually:** VCA = **Van Cleef & Arpels** (Collection Extraordinaire fixture), Charlotte =
   **Charlotte Tilbury** (branded counter). Still open: **Elixir** (probably Shiseido’s ELIXIR skincare — confirm),
   **CDS** (probably Central Department Store — confirm), **EA7** (presumably Emporio Armani — confirm), **Pralet**
   (brand/venue type), and the meaning of **Wiriwork**.
5. **Resolution caveat:** many folders are LINE-app exports (`LINE_ALBUM_…`, `S__…`), already recompressed to
   ~150–400 KB (≈1,000–2,000 px). That is the maximum resolution that exists in the archive for those projects —
   fine for the site’s 2,000 px target in most cases, but these are not camera originals. The CPB and Chanel-airport
   folders do hold 2–3 MB camera files.
6. **Prada Changi T1 & T2** is 1,838 daily construction-progress photos (plus a 41 MB install manual) — not
   finished-work photography.
7. The Burberry folder also holds a 118 MB **as-built PDF** titled “GUCCI&BURBERRY CENTRAL DUSIT PARK”, which
   supports the dual-brand naming already used on the site.


## Projects already on the site — better/extra photos in archive?

| Page | Archive photos | Verdict |
|---|---|---|
| `project-chanel-emsphere.html` | 0 | **None** — archive folder is empty; keep current images |
| `project-gucci-mega-bangna.html` | 12 | 12 extra angles; PR set AI-suspect. Current hi-res images fine; a few extra angles usable after verification |
| `project-burberry-gucci-dusit-central-park.html` | 24 | ~24 extra photos + as-built PDF; worth adding 2–3 angles |
| `project-paul-smith-central-village.html` | 40 | 35 real photos — **upgrade**: replace the generic sector image on the page |
| `project-shiseido-centralworld.html` | 17 | 13 extra but LINE-compressed (~175 KB); marginal gain |
| `project-panpuri-one-bangkok.html` | 39 | 33 real photos — **upgrade**: replace the generic image on the page |
| `project-cpb-dusit-central-park.html` | 11 | 7+4 extra photos; add 1–2 angles |
| `project-popmart-maya-chiangmai.html` | 82 | 78 photos — **upgrade**: plenty of real interior/detail shots |

(Per your instruction these eight pages were not changed in this step.)


## Full project table

| Project | Brand | City | Usable imgs (est) | On site | Category | Slug | Rec |
|---|---|---|---|---|---|---|---|
| Chanel @ Emsphere | Chanel | Bangkok | 0 | project-chanel-emsphere.html | luxury-retail | `chanel-emsphere` | **on-site** |
| Gucci @ Mega Bangna | Gucci | Bangkok | 12 | project-gucci-mega-bangna.html | luxury-retail | `gucci-mega-bangna` | **on-site** |
| Burberry & Gucci @ Dusit Central Park | Burberry & Gucci | Bangkok | 24 | project-burberry-gucci-dusit-central-park.html | luxury-retail | `burberry-gucci-dusit-central-park` | **on-site** |
| Paul Smith @ Central Village | Paul Smith | Bangkok (Suvarnabhumi) | 40 | project-paul-smith-central-village.html | luxury-retail | `paul-smith-central-village` | **on-site** |
| Shiseido @ CentralWorld | Shiseido | Bangkok | 17 | project-shiseido-centralworld.html | luxury-retail | `shiseido-centralworld` | **on-site** |
| Panpuri @ One Bangkok | Panpuri | Bangkok | 39 | project-panpuri-one-bangkok.html | luxury-retail | `panpuri-one-bangkok` | **on-site** |
| Clé de Peau Beauté @ Dusit Central Park | Clé de Peau Beauté | Bangkok | 11 | project-cpb-dusit-central-park.html | luxury-retail | `cpb-dusit-central-park` | **on-site** |
| Pop Mart @ Maya Chiangmai | Pop Mart | Chiang Mai | 82 | project-popmart-maya-chiangmai.html | luxury-retail | `popmart-maya-chiangmai` | **on-site** |
| Chanel @ Central Udon Thani | Chanel | Udon Thani | 14 | — | luxury-retail | `chanel-central-udon` | **publish** |
| Chanel @ Central Chaengwattana | Chanel | Nonthaburi | 12 | — | luxury-retail | `chanel-central-chaengwattana` | **publish** |
| Chanel @ Suvarnabhumi Airport | Chanel | Samut Prakan (BKK airport) | 13 | — | luxury-retail | `chanel-suvarnabhumi` | **publish** |
| Chanel @ Chiang Mai Airport | Chanel | Chiang Mai | 21 | — | luxury-retail | `chanel-chiangmai-airport` | **publish** |
| Gucci @ Central Pinklao | Gucci | Bangkok | 16 | — | luxury-retail | `gucci-central-pinklao` | **publish** |
| Shiseido @ Siam Takashimaya | Shiseido | Bangkok | 14 (7 HEIC) | — | luxury-retail | `shiseido-siam-takashimaya` | **publish** |
| Panpuri @ Suvarnabhumi Airport | Panpuri | Samut Prakan (BKK airport) | 15 | — | luxury-retail | `panpuri-suvarnabhumi` | **publish** |
| Panpuri @ Chiang Mai Airport | Panpuri | Chiang Mai | 19 | — | luxury-retail | `panpuri-chiangmai-airport` | **publish** |
| Van Cleef & Arpels @ Emsphere | Van Cleef & Arpels | Bangkok | 24 | — | luxury-retail | `vca-emsphere` | **publish** |
| Sunnies @ CentralWorld | Sunnies | Bangkok | 7 | — | luxury-retail | `sunnies-centralworld` | **publish** |
| Sunnies @ Central Bangna | Sunnies | Bangkok | 22 | — | luxury-retail | `sunnies-central-bangna` | **publish** |
| Another Story @ Emsphere | Another Story | Bangkok | 23 | — | luxury-retail | `another-story-emsphere` | **publish** |
| Philips pop-up @ Central Chidlom | Philips | Bangkok | 7 | — | corporate | `philips-popup-central-chidlom` | **publish** |
| Blue Bottle @ EmQuartier | Blue Bottle Coffee | Bangkok | 23 | — | fnb | `blue-bottle-emquartier` | **publish** |
| Chanel @ Central Chiangmai (PR folder) | Chanel | Chiang Mai | 6 | — | luxury-retail | `chanel-central-chiangmai` | **needs-decision** |
| Chanel cabin @ The Emporium | Chanel | Bangkok | 3 | — | luxury-retail | `chanel-cabin-emporium` | **needs-decision** |
| Chanel @ Siam Paragon | Chanel | Bangkok | 6 | — | luxury-retail | `chanel-siam-paragon` | **needs-decision** |
| Chanel N°5 Re-edition 2026 (VM) | Chanel | Bangkok | 27 (27 HEIC) | — | luxury-retail | `chanel-vm-no5-2026` | **needs-decision** |
| Chanel Rouge Coco Gloss 2026 (VM) | Chanel | Bangkok | 21 | — | luxury-retail | `chanel-vm-rouge-coco-2026` | **needs-decision** |
| Chanel Rouge Noir 2026 (VM) | Chanel | Bangkok | 11 (11 HEIC) | — | luxury-retail | `chanel-vm-rouge-noir-2026` | **needs-decision** |
| Chanel Holiday 2025 (VM) | Chanel | Bangkok | 11 (11 HEIC) | — | luxury-retail | `chanel-vm-holiday-2025` | **needs-decision** |
| Clé de Peau Beauté @ Central Pinklao | Clé de Peau Beauté | Bangkok | 11 | — | luxury-retail | `cpb-central-pinklao` | **needs-decision** |
| Clé de Peau Beauté @ Siam Takashimaya | Clé de Peau Beauté | Bangkok | 21 | — | luxury-retail | `cpb-siam-takashimaya` | **needs-decision** |
| Clé de Peau Beauté @ Central Chidlom | Clé de Peau Beauté | Bangkok | 35 | — | luxury-retail | `cpb-central-chidlom` | **needs-decision** |
| Van Cleef & Arpels @ Central Chidlom | Van Cleef & Arpels | Bangkok | 10 | — | luxury-retail | `vca-central-chidlom` | **needs-decision** |
| Van Cleef & Arpels Escential @ Siam Paragon | Van Cleef & Arpels | Bangkok | 2 | — | luxury-retail | `vca-escential-siam-paragon` | **needs-decision** |
| Elixir @ Central Chaengwattana | Elixir (confirm brand) | Nonthaburi | 11 | — | luxury-retail | `elixir-central-chaengwattana` | **needs-decision** |
| Elixir @ Central Pinklao | Elixir (confirm brand) | Bangkok | 5 | — | luxury-retail | `elixir-central-pinklao` | **needs-decision** |
| Charlotte Tilbury @ Central Chiangmai | Charlotte Tilbury | Chiang Mai | 4 | — | luxury-retail | `charlotte-tilbury-central-chiangmai` | **needs-decision** |
| Bobbi Brown @ Central Chaengwattana | Bobbi Brown | Nonthaburi | 4 | — | luxury-retail | `bobbi-brown-central-chaengwattana` | **needs-decision** |
| Bobbi Brown @ Central Pinklao | Bobbi Brown | Bangkok | 8 | — | luxury-retail | `bobbi-brown-central-pinklao` | **needs-decision** |
| Bobbi Brown @ The Mall Bangkae | Bobbi Brown | Bangkok | 2 | — | luxury-retail | `bobbi-brown-the-mall-bangkae` | **needs-decision** |
| Hourglass @ Central Phuket | Hourglass | Phuket | 15 | — | luxury-retail | `hourglass-central-phuket` | **needs-decision** |
| Hourglass @ Central Chiangmai | Hourglass | Chiang Mai | 12 | — | luxury-retail | `hourglass-central-chiangmai` | **needs-decision** |
| Hourglass @ Siam Takashimaya | Hourglass | Bangkok | 12 | — | luxury-retail | `hourglass-siam-takashimaya` | **needs-decision** |
| Hourglass @ Central Chidlom | Hourglass | Bangkok | 7 | — | luxury-retail | `hourglass-central-chidlom` | **needs-decision** |
| Hourglass @ The Mall Ngamwongwan | Hourglass | Nonthaburi | 8 | — | luxury-retail | `hourglass-the-mall-ngamwongwan` | **needs-decision** |
| Hourglass @ Central Khonkaen | Hourglass | Khon Kaen | 4 | — | luxury-retail | `hourglass-central-khonkaen` | **needs-decision** |
| Hourglass Additional @ Siam Paragon | Hourglass | Bangkok | 13 | — | luxury-retail | `hourglass-siam-paragon-additional` | **needs-decision** |
| Hourglass Minor Changes @ CentralWorld | Hourglass | Bangkok | 7 | — | luxury-retail | `hourglass-centralworld-minor` | **needs-decision** |
| Pralet @ EmQuartier | Pralet | Bangkok | 3 | — | fnb | `pralet-emquartier` | **needs-decision** |
| EA7 @ Siam Paragon | EA7 Emporio Armani (confirm) | Bangkok | 4 | — | luxury-retail | `ea7-siam-paragon` | **needs-decision** |
| CDS @ Central Bangna | CDS (confirm meaning) | Bangkok | 3 | — | needs-decision-category | `cds-central-bangna` | **needs-decision** |
| 3M (unknown venue) | 3M | unknown | 3 | — | corporate | `3m` | **needs-decision** |
| Prada @ Changi Airport T1 & T2 | Prada | Singapore | 1838 | — | luxury-retail | `prada-changi` | **needs-decision** |
| Hourglass @ Central Pinklao | Hourglass | Bangkok | 0 | — | luxury-retail | `hourglass-central-pinklao` | **skip** |

## Decisions I need from you

**D1 — VM campaigns (4 Chanel campaigns).** The site has no visual-merchandising category. Options:
(a) one combined page “Chanel Visual Merchandising Campaigns” under Luxury Retail & Beauty, scope “Visual
merchandising”, showing all four campaigns (my recommendation — one strong page instead of four thin ones);
(b) one page per campaign (N°5 Re-edition 2026, Rouge Coco Gloss 2026, Rouge Noir 2026, Holiday 2025).

**D2 — Multi-location counter rollouts.** Hourglass has 7 usable locations (+2 amendment folders), CPB 3 more
locations, Van Cleef & Arpels 3, Bobbi Brown 3, Elixir 2. One page per location would add ~18 near-identical thin
pages. My recommendation: **one “rollout” page per brand** (e.g. “Hourglass — nationwide counter rollout” listing
Phuket, Chiang Mai, Khon Kaen, Bangkok locations; same for CPB / VCA / Bobbi Brown / Elixir), with the amendment
folders (“Additional”, “Minor Changes”) folded in as a maintenance mention, not pages. Per-location pages remain
possible later for standouts (e.g. CPB Siam Takashimaya’s 21 camera photos).

**D3 — Prada @ Changi (Singapore).** Progress photos only. Options: (a) skip; (b) a restrained page using the
least construction-looking shots, framed as “overseas installation programme” — needs your sign-off and ideally
client clearance; (c) you supply finished photos. My recommendation: (a) or (c).

**D4 — Thin sets** (too few images for a page today): Chanel cabin @ Emporium (3), Chanel Siam Paragon (0 real),
VCA Escential Paragon (2), Charlotte Tilbury Chiang Mai (4), Bobbi Brown Bangkae (2, AI-suspect), Pralet (3),
EA7 (4, unverified), 3M (3, no venue), CDS (3). Publish anyway / skip / you send more photos — per project.

**D5 — Brand confirmations:** Elixir (= Shiseido ELIXIR?), EA7 (= Emporio Armani 7?), Pralet (what is it?),
CDS (= Central Department Store?), “Wiriwork” meaning, and whether Chanel “Central Chiangmai” (PR) is the same
job as Chanel Chiang Mai Airport.

**D6 — Facts for new pages.** For every approved project I have **no area (sqm), no scope confirmation and no
headline numbers**, and a year only where the folder name states one (Udon 2025, Chaengwattana 2026, SVB 2026,
Another Story 2026, Burberry 2025, VM campaigns). Per your rules those rows/blocks will simply be omitted until
you supply values — listed per-project in `docs/works-manifest.json` under `year`/`year_source`.


## Non-project folders

- **VDO Clip** — 4 videos: company profile master (1.10 GB) + 3 machine films. Used in Part 2.
- **1 Factory Photo** — 55 files: 52 real factory photos (LINE-compressed), 2 misc, 1 Gemini AI image. Not a project; could refresh about/factory imagery later.
- **1 Photo Render** — 21 project subfolders — a MIX of real photos and AI-generated images (ChatGPT/Gemini/'By Claude' files). Merged into projects above; AI flags noted per project.
- **1 Wiriwork** — 4 subfolders of genuine site/fixture photography (CDS, Another Story, Sunnies ×2). Meaning of 'Wiriwork' unknown — it may be an internal team or sister-brand name (cf. your Wiribed project); please confirm.
- **1 Photo Render/CC Work in process** — 4 files, explicitly work-in-process — excluded per your instruction.


## Logistics note for Step 1b (image export)

Downloads will go through the Drive connector (max-resolution originals, base64-decoded to disk), then be exported to `assets/img/works/<slug>/` at ≤2000 px JPEG q80, metadata stripped. Originals and working copies stay out of git (`.gitignore` entry added in Step 1b). HEIC sets are converted during export. The 20+ MB PDFs are ignored. No binaries beyond the exported JPEGs enter the repo.

