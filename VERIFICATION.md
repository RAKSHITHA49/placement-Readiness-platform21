# Placement Readiness Platform — Verification Guide

## Proof + Submission (New)

### Route
- **#prp/proof** — Build Proof page with 8-step overview, 3 artifact URLs, Copy Final Submission

### Storage
- **prp_build_steps** — Step 1–6 checkboxes: `{ onboarded, jd-analysis, company-intel, round-mapping, readiness-score, history-export }`
- **prp_final_submission** — Artifact links: `{ lovableUrl, githubUrl, deployedUrl }`

### Shipped status
- Header badge shows **"Shipped"** only when: all 8 steps done + all 10 tests passed + all 3 URLs valid
- Otherwise: **"In Progress"**
- Checklist lock unchanged: Ship stays locked until all 10 tests pass

### Verification steps
1. Go to **Proof** — see 8 steps (6 checkable, 2 auto), 3 URL inputs, Copy Final Submission.
2. Enter invalid URL (e.g. `abc`) in Lovable field, blur — see red border and error.
3. Enter `https://lovable.dev/x` — error clears, value persists.
4. Fill all 3 URLs, check all 6 steps, pass all 10 tests — badge becomes "Shipped", completion message appears.
5. Click **Copy Final Submission** — paste elsewhere, format matches spec.
6. With 9/10 tests — Ship locked, Proof cannot show Shipped.

---

## Test Checklist & Ship Lock

### Routes
- **#prp/07-test** — Test checklist page (10 items, localStorage persisted)
- **#prp/08-ship** — Ship page (locked until all 10 tests pass)

### Checklist storage
- **Key:** `prp_test_checklist` in localStorage
- **Format:** `{ "jd-required": true, "short-jd-warning": true, ... }`
- **Persistence:** Checkboxes survive refresh; Reset clears all

### Ship lock behavior
- **&lt; 10 passed:** Ship page shows "Locked" — must complete all tests first
- **10 passed:** Ship page shows "Ready to Ship"

### Verification steps
1. Go to **Test** (sidebar or `#prp/07-test`). See "Tests Passed: 0 / 10" and "Fix issues before shipping."
2. Check 3 items → summary updates to 3/10. Go to **Ship** → see Locked.
3. Check all 10 → go to **Ship** → see "Ready to Ship."
4. Refresh page → checklist state persists (same checkboxes checked).
5. Click **Reset checklist** → all unchecked, Ship shows Locked again.

---

## Company Intel + Round Mapping (New)

### Company Intel (when company name provided)
- Company name, Industry, Size category (Startup / Mid-size / Enterprise)
- Typical Hiring Focus (template based on size)
- Demo note: "Demo Mode: Company intel generated heuristically."

### Round Mapping Engine
- Dynamic rounds based on company size + detected skills
- Vertical timeline with "Why this round matters" under each
- **Test scenarios:**
  - **Amazon + DSA** → Enterprise flow: Online Test → Technical (DSA+CS) → Tech+Projects → HR
  - **TechCorp (unknown) + React/Node** → Startup flow: Practical Coding → System Discussion → Culture Fit
  - **Mid-size company** → 3 rounds: Online Test → Technical → Projects+HR

---

## 1. Skill Extraction

**How it works:** Case-insensitive keyword matching across 6 categories.

| Category | Sample Keywords |
|----------|-----------------|
| Core CS | DSA, OOP, DBMS, OS, Networks |
| Languages | Java, Python, JavaScript, C++, Go |
| Web | React, Node.js, Express, REST, GraphQL |
| Data | SQL, MongoDB, PostgreSQL, MySQL, Redis |
| Cloud/DevOps | AWS, Docker, Kubernetes, CI/CD, Linux |
| Testing | Selenium, Cypress, JUnit, PyTest |

**If no keywords found:** Shows "General fresher stack".

---

## 2. History Persistence

- **Storage:** `localStorage` key `placement_jd_history`
- **On Analyze:** Entry is saved and prepended to history
- **After refresh:** History list and saved entries remain
- **URL:** `#results/<id>` — bookmarkable, works after refresh

---

## 3. Interactive Features (New)

### Skill self-assessment
- Each skill tag has **"I know"** / **"Need practice"** toggle
- Default: Need practice
- Stored in `skillConfidenceMap[skill]` per history entry

### Live readiness score
- Base score +2 per "I know", -2 per "Need practice"
- Bounds: 0–100, updates in real time

### Export tools
- **Copy 7-day plan** | **Copy round checklist** | **Copy 10 questions**
- **Download as TXT** — single file with all sections

### Action Next box
- Top 3 weak skills (practice-marked)
- Suggestion: "Start Day 1 plan now." (or "You're ready..." when all known)

---

## 4. Verification Steps

### A. Live score & toggles

1. Run an analysis and open Results.
2. Note the initial readiness score.
3. Click **"I know"** on 2 skills → score increases by +4.
4. Click **"Need practice"** again → score returns.
5. Refresh (F5) → selections and score stay the same.

### B. Persistence after refresh

1. Change some skills to "I know".
2. Refresh the page.
3. Reopen the entry from History.
4. Confirm toggles and score match your last edits.

### C. Export

1. On Results, click **Copy 7-day plan** → paste in notepad.
2. Click **Copy round checklist** → paste.
3. Click **Download as TXT** → file downloads with full content.

### D. Action Next

1. With some skills on "Need practice" → focus areas list those skills.
2. Mark all as "I know" → message switches to "All skills marked as known" / "You're ready."

---

## 5. Readiness Score Formula

| Factor | Points |
|--------|--------|
| Base | 35 |
| Per detected category (max 6) | +5 each (max 30) |
| Company name provided | +10 |
| Role provided | +10 |
| JD length > 800 chars | +10 |
| **Live adjustment** | **+2 per "I know", -2 per "Need practice"** |
| **Cap** | **0–100** |
