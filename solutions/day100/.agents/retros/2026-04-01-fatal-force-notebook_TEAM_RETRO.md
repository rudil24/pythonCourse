---
date: 2026-04-01
project: Fatal Force — Day 100 Python Course Capstone
scope: Complete Fatal_Force_Claude.ipynb from skeleton to fully working notebook
---

# Team Retro: Fatal Force Notebook

## What Went Well

__Cap (Team Lead / Architect):__
- Boot sequence executed cleanly — `.opst-project-type` was present, routing to software track was unambiguous.
- `owner.txt` directive was clear and provided an immediate, actionable goal.
- Splitting the work into logical sections (exploration → cleaning → charts) kept execution orderly with no backtracking.
- The decision to inspect column names and data types before writing a single line of chart code prevented multiple fixable errors (e.g., poverty_rate stored as string, not float).

__Stella (Python Developer — Data Viz):__
- Plotly Express handled the majority of interactive charts cleanly. Stacked bar for racial makeup, choropleth for state map, dual y-axis line chart for poverty/HS relationship all rendered without issues.
- Seaborn `jointplot`, `kdeplot`, and `lmplot` each served their intended analytical purpose with minimal boilerplate.
- The per-capita rate chart addition was the most analytically valuable cell in the notebook — it transformed a misleading raw count into the actual story.

__Schema (Data Modeling):__
- Identifying that `poverty_rate`, `percent_completed_hs`, and all race share columns were stored as strings (not floats) early was critical. `pd.to_numeric(..., errors='coerce')` handled edge cases cleanly.
- `fillna(0)` on census frames was appropriate since missing city-level data represented zero representation, not unknown data.
- Keeping `df_fatalities` NaN rows intact and handling them per-chart (via `dropna(subset=[...])`) was the correct approach — it avoided data loss for columns that were complete.

__Rudi (Owner):__
- I handed the team the entire notebook with its queries and they one shot it.
- I asked them to analyze per capita race deaths and they went above and beyond to pull 2015 census data that wasn't in the included set.

## What Went Wrong

__Cap (Team Lead):__
- The `NotebookEdit` tool failed twice when the notebook had been auto-modified (likely by VS Code's Jupyter extension saving cell outputs). The fallback to direct `json.load` / `json.dump` via Bash was necessary for the per-capita cell insert. This should be anticipated for `.ipynb` files that are open in an IDE during editing.
- Cell IDs were absent (`nbformat 4.0`), making `NotebookEdit`'s cell_id references non-functional. All edits ultimately relied on the sequential index, which is more fragile.

__Stella (Python Developer):__
- The `pie` chart for mental illness passed `values` in `[False, True]` order from `value_counts()` — the label mapping `['No Mental Illness', 'Mental Illness']` was manually matched to that order, which is fragile if the value_counts sort order changes. A more robust approach would explicitly filter by boolean value.

__Rudi (Owner):__
- One nitpick, at the start it said I'm Cap but asked me what to do next. The owner.txt has everything they need to tell/ask me their approach.

## What Did We Discover

__Cap (Team Lead):__
- __`nbformat 4.0` notebooks have no cell IDs.__ Any agentic tool that targets cells by ID will silently fail. When working with older notebooks, always verify format version first and fall back to index-based or JSON-direct manipulation.
- __Inspecting data types before charting is non-negotiable for CSV-sourced notebooks.__ The WaPo/Census CSVs stored numeric rates as strings — a pattern common in government data exports. This step should be a standard pre-chart checklist item.

__Stella (Python Developer):__
- __Per-capita rates tell a fundamentally different story than raw counts.__ White Americans appeared to be killed most often in raw numbers. Black Americans are killed at 2.5x the per-capita rate. Native Americans at 2x. This is a textbook example of why population-normalized rates must accompany any absolute count chart when comparing groups of unequal size.
- __The `Share_of_Race_By_City` dataset could not be cleanly joined to `Deaths_by_Police_US` by city name__ due to formatting inconsistencies (e.g., "Los Angeles city" vs "Los Angeles"). For the Rate of Death by Race section, an approximate match was used. A production analysis would require a standardized FIPS code join.

__Schema (Data Modeling):__
- __Census data at city level + fatalities at city level creates a join hazard.__ The race share data has 29,268 rows (many cities, many states) while fatalities has 2,535. A naive merge on city name alone would produce many false matches (e.g., "Springfield" exists in dozens of states). State-scoped joins are required for accurate per-city analysis.

__Rudi (Owner):__
- I love the fact that we can just jot down some notes and overarching thoughts of what we are looking for in a dataset, and AI can write all the code boxes, and meaningful graphs. Amazes me every time.
---

_Awaiting Product Owner review and comments below each section._
