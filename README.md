# Blue Ocean Startup Empire ⚡

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Ready-emerald?style=flat-square&logo=github)](https://pages.github.com/)
[![Papers](https://img.shields.io/badge/Papers-500%20Verified-blue?style=flat-square)](index.html)
[![Council Startups](https://img.shields.io/badge/Council%20Startups-53%20Sovereign-purple?style=flat-square)](index.html)
[![Venture Blueprints](https://img.shields.io/badge/Venture%20Blueprints-Top%2015-amber?style=flat-square)](index.html)
[![Offline Capable](https://img.shields.io/badge/Offline-100%25%20Standalone-zinc?style=flat-square)](index.html)

A standalone, interactive discovery portal synthesizing **500 radically unique blue-ocean research papers**, **53 sovereign council startups**, the **Phonon Dynamics (Acoustic Negawatt)** breakthrough invention, and **15 institutional venture pitch blueprints**.

---

## 🚀 Live Demo on GitHub Pages

Once deployed, the live web portal is accessible at:
```
https://<your-github-username>.github.io/<repository-name>/
```

### 1-Click Local Execution
Simply double-click or open [`index.html`](index.html) in any modern web browser. No local web server, node modules, or build steps required.

---

## 🛠️ How to Deploy on GitHub Pages

1. **Create Repository & Push**:
   ```bash
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git branch -M main
   git push -u origin main
   ```
   *(Or run `gh repo create <repo-name> --public --source=. --push`)*

2. **Activate GitHub Pages**:
   - Go to your repository on GitHub.
   - Click **Settings** → **Pages** (in the left sidebar).
   - Under **Build and deployment** > **Source**, select **Deploy from a branch**.
   - Under **Branch**, select `main` and folder `/ (root)`, then click **Save**.
   - Your site will be live within 1–2 minutes!

---

## 📂 Repository Contents

| File | Description |
| :--- | :--- |
| [`index.html`](index.html) | **Production Single-Page Web App** (1.64 MB). 100% self-contained with complete embedded data bundle, Luma-styled UI, responsive layouts, search engine, and modals. |
| [`.nojekyll`](.nojekyll) | Bypasses Jekyll on GitHub Pages to ensure fast, direct static asset serving. |
| [`template.html`](template.html) | Source HTML & Tailwind/JS layout template. |
| [`data_bundle.json`](data_bundle.json) | The comprehensive research database (500 papers, metadata, council specs, BOM, firmware). |
| [`build_index_html.py`](build_index_html.py) | Python build script to regenerate `index.html` from `template.html` + `data_bundle.json`. |

---

## ✨ Features & Capabilities

- **Luma (lu.ma) Design Aesthetic**: Off-white pearl canvas (`#FAFAFC`), delicate borders, glassmorphic cards, luminous glowing pill badges.
- **Strict Zero-Overflow Responsiveness**: Tested and verified across viewports from 360px mobile (e.g. Realme P1 5G, iPhones, Pixels) to 4K desktops.
- **Global Omni-Search**: Instant full-text search with `⌘K` / `Ctrl+K` keyboard shortcut across all papers, startups, and blueprints.
- **Interactive Transducer BOM Calculator**: Real-time component cost recalculation for the Phonon Dynamics 72-hour dorm prototype.
- **Embedded C++ Firmware Viewer**: Copyable FreeRTOS dual-core ultrasonic frequency modulation driver for ESP32-S3.
- **Full CSV Export**: 1-click download of the complete 500-paper dataset with verified arXiv and DOI links.
