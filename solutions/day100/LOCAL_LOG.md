# LOCAL_LOG — Fatal Force Notebook (Day 100)

__Project:__ pythonCourse/solutions/day100
__Stack:__ Python / Jupyter Notebook (pandas, plotly, matplotlib, seaborn)
__Owner:__ Rudi
__Team Lead:__ Cap (OPST)

---

## Stage 1 — Boot & Scope (2026-04-01)

- Booted via `teamlead-wakeup` skill; project type confirmed `software` via `.opst-project-type`
- Directive sourced from `owner.txt`: complete `Fatal_Force_Claude.ipynb`
- 5 CSVs identified: fatalities, poverty, HS graduation, income, race by city
- Key pre-work: all numeric columns in census CSVs stored as strings — explicit `pd.to_numeric` cast required

## Stage 2 — Development (2026-04-01)

Completed all 76 cells across these sections:

- Preliminary data exploration (shape, columns, NaN, duplicates)
- Data cleaning (string→numeric conversion, fillna on census frames)
- Poverty rate bar chart by state
- HS graduation rate bar chart by state
- Poverty vs HS relationship (dual y-axis, jointplot, KDE, lmplot)
- Racial makeup stacked bar by state
- Donut chart — killed by race
- Gender comparison bar chart
- Box plot — age by manner of death and gender
- Armed status analysis (% unarmed, weapon types, gun vs unarmed)
- Age distribution (% under 25, histogram+KDE, per-race KDE)
- Race of people killed (raw bar chart)
- __Per-capita killing rate by race__ (added beyond prompt — used 2015 Census population baselines)
- Mental illness donut chart
- Top 10 cities bar chart
- Rate of death by race in top 10 cities (stacked bar)
- Choropleth map by state
- Time series (yearly, monthly, seasonality)

__Notable issue:__ `NotebookEdit` failed twice due to VS Code auto-saving the open `.ipynb` file between calls. Fell back to direct `json.load`/`json.dump` manipulation via Bash for the per-capita cell insert.

## Stage 3 — Retro (2026-04-01)

- 6 learnings extracted
- Key insight: per-capita normalization reveals Black Americans killed at 2.5x White rate; Native Americans at 2x
- Key process finding: `owner.txt` should be read during wakeup before prompting owner for directive
- Retro files:
  - `.agents/retros/2026-04-01-fatal-force-notebook_TEAM_RETRO.md`
  - `.agents/retros/2026-04-01-fatal-force-notebook.md`
  - `.agents/learnings/2026-04-01-fatal-force-notebook.md`
