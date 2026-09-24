# Happexhibition — Website

Static website for **Happ Exhibition Co., Ltd.** — *Making Retail Architecture a Reality.*
Generated from the Figma design: https://www.figma.com/design/UrhSfSD2Z2Y072SNSbXFZa

## Structure
```
index.html                 Home (hero slider, stats, services, works, marquee, process, news)
about.html                 Story, timeline, why-us, leadership (9), factory, clients
services.html              5 service blocks + capability table + FAQ (all answered)
works.html                 Portfolio index with live category filter (8 projects)
project-*.html             8 project case pages, chained prev/next
news.html + article-*.html News index + 7 written articles (incl. Save Thai Ocean, Wiribed)
careers.html               Culture, benefits, open roles
role-senior-draftsman.html Role detail + application (mailto)
contact.html               Form (mailto), map, LINE QR, address
404.html                   Not found
css/style.css              Design tokens + all components
js/main.js                 Slider, header, dropdown, mobile menu, count-ups, reveals, filter
assets/img/                All imagery (76 files) incl. clients/ logo set
```

## Conversion & contact wiring
- Every **Get a Quote** action opens LINE: `https://line.me/R/ti/p/@happexhibition`
- Contact **Send Message** → `mailto:nathawat.j@happexhibition.com`
- Careers **Apply** → `mailto:pakavadee.c@happexhibition.co.th,nathawat.j@happexhibition.com`
- Phone everywhere: **+66 81-488-0475** (`tel:` linked) · Hours Mon–Sat 8:30–17:30
- Facebook: profile id 61593124306637 · Instagram: @happexhibition
- Map links to https://maps.app.goo.gl/vSq9KAFU9sLEjzBo8 (static image is an OpenStreetMap render — swap for a Google Maps iframe embed in production)

## Run locally
Open `index.html` in a browser, or serve it:
```bash
python3 -m http.server 8000
```

## Push to GitHub (from VSCode)
```bash
cd happexhibition-website
git init
git add -A
git commit -m "Happexhibition website v1"
git branch -M main
git remote add origin https://github.com/<your-username>/happexhibition-website.git
git push -u origin main
```
Then enable **GitHub Pages**: repo → Settings → Pages → Source: `main` / root.
Your site will be live at `https://<your-username>.github.io/happexhibition-website/`.

## Before going live (known TODOs)
- `assets/img/line-qr.png` is a regenerated QR encoding the real LINE link — replace with the official LINE QR file if you prefer the LINE-branded one.
- `assets/img/sto-logo.png` is **not included** (file wasn't available) — drop the Save Thai Ocean logo PNG in with that exact name and the article badge appears automatically.
- Images are ≤1600px extractions from the company profile PDF — swap in high-res originals when available.
- Brand font **DB FongNam** is commercial; the site ships with Archivo/Inter/Anuphan from Google Fonts. Add licensed DB FongNam via `@font-face` when you have the files.
- PDPA / cookie-policy pages are placeholder links in the footer.
- Forms use `mailto:` (no backend). For a real form endpoint, wire to Formspree/Google Forms or your own API.
