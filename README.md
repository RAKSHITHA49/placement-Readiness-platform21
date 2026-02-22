# Placement Readiness Platform

Practice, assess, and prepare for your dream job.

## Features

- **Landing & Dashboard** — Get started, view readiness score, upcoming assessments
- **JD Analysis** — Paste job descriptions to extract skills, get round mapping, and a 7-day prep plan
- **Practice** — DSA chapters (Arrays, Trees, DP, System Design) with topic tracking
- **Assessments** — DSA, System Design, Aptitude, and HR mock tests with MCQ flow
- **Resources** — Curated links (NeetCode, ByteByteGo, STAR method, etc.)
- **History** — Save and reload analyses
- **Results** — Skill toggles, readiness score, exports (7-day plan, checklist, questions)
- **Test Checklist** — 10 verification items before shipping
- **Ship & Proof** — Artifact URLs, copy final submission

## Tech Stack

- Vanilla HTML/CSS/JS (single-file SPA: `index.html` at root for Vercel, `static/index.html` for local dev)

## How to Run — Full Platform (Recommended)

1. Install Node.js (v18+) if needed.
2. From the project root:

```bash
npm install
npm run serve
```

3. Open **http://localhost:8765** in your browser.

**Alternative (Python):**

```bash
python launch_browser.py
```

Serves `static/` on port 8765 and opens the app in your default browser.


## Deploy to Vercel

The project includes a `vercel.json` that configures the build. To deploy:

1. Push your code to GitHub
2. Import the project in [Vercel](https://vercel.com)
3. Vercel will use the build command and output directory automatically
4. Deploy

Or use the Vercel CLI: `vercel`

## Hash Routes (Deep Links)

All pages support direct URLs:

- `#dashboard` — Dashboard  
- `#practice` — Practice  
- `#assessments` — Assessments  
- `#analyze` — Analyze JD  
- `#history` — History  
- `#resources` — Resources  
- `#profile` — Profile  
- `#results` — Results (or `#results/<id>` for a specific analysis)  
- `#prp/07-test` — Test checklist  
- `#prp/08-ship` — Ship page  
- `#prp/proof` — Proof page  

## Color Scheme

Primary: `hsl(245, 58%, 51%)` (indigo/purple)
