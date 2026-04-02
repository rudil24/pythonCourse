# Learning: Check nbformat Version Before Using NotebookEdit

__ID__: L1
__Category__: process
__Confidence__: high

## What We Learned

`nbformat 4.0` notebooks have no cell IDs — `NotebookEdit` cell_id targeting silently fails. Always check `nbformat_minor` first; if < 1, fall back to direct JSON manipulation via Bash.

## Why It Matters

Saves two failed tool calls and avoids confusion about why edits aren't applying.

## Source

Fatal Force notebook — per-capita cell insert required JSON fallback after two NotebookEdit failures.

---

# Learning: Inspect Data Types Before Any Chart Code

__ID__: L2
__Category__: process
__Confidence__: high

## What We Learned

Government and journalistic CSV exports frequently store numeric columns (rates, percentages) as strings. Always run `df.dtypes` and `df.head()` across all DataFrames before writing chart code, and cast with `pd.to_numeric(..., errors='coerce')` immediately after load.

## Why It Matters

Type mismatches cause silent groupby/aggregation errors that produce wrong charts with no exception raised.

## Source

Fatal Force — `poverty_rate`, `percent_completed_hs`, and all race share columns were strings requiring explicit conversion.

---

# Learning: Per-Capita Rates Are Mandatory When Comparing Unequal-Size Groups

__ID__: L3
__Category__: architecture
__Confidence__: high

## What We Learned

Raw kill counts made White Americans appear most at-risk. Per-capita normalization (kills per million people, using 2015 Census baselines) revealed Black Americans are killed at 2.5x and Native Americans at 2x the White rate — the actual story. Any dataset comparing groups of unequal population size requires a population-normalized metric alongside raw counts.

## Why It Matters

Raw counts without normalization are actively misleading and undermine the analytical value of the entire notebook.

## Source

Fatal Force — per-capita chart added in "Race of People Killed" section using hardcoded 2015 US Census population estimates not present in the provided dataset.

---

# Learning: City-Name Joins Require State Scope or FIPS Codes

__ID__: L4
__Category__: architecture
__Confidence__: high

## What We Learned

Joining `Deaths_by_Police_US.csv` (city, state) to `Share_of_Race_By_City.csv` (City with suffixes like "city", "CDP") on city name alone produces ambiguous matches — "Springfield" exists in dozens of states. Production-quality joins require state-scoped matching or standardized FIPS codes.

## Why It Matters

Incorrect joins silently produce wrong per-city race demographics, invalidating the "Rate of Death by Race" analysis.

## Source

Fatal Force — Rate of Death by Race section used approximate string matching; flagged as a known limitation.

---

# Learning: owner.txt Should Be Read Immediately After Project Type Detection

__ID__: L5
__Category__: process
__Confidence__: high

## What We Learned

The boot sequence correctly identified project type via `.opst-project-type` but asked the Product Owner for their first directive instead of reading `owner.txt` first. Reading `owner.txt` (or any owner-defined directive file) must be part of the wakeup sequence before surfacing to the user.

## Why It Matters

Avoids unnecessary back-and-forth; the owner has already written their intent and shouldn't have to repeat it verbally.

## Source

Rudi (Owner) feedback in TEAM_RETRO: "at the start it said I'm Cap but asked me what to do next. The owner.txt has everything they need."

---

# Learning: Boolean value_counts() Label Mapping Is Order-Dependent

__ID__: L6
__Category__: debugging
__Confidence__: medium

## What We Learned

When passing `value_counts()` results for boolean columns directly into a chart's `names` list, the label order must match the sort order of `value_counts()` (descending by count). This is fragile. Prefer explicit filtering: `df[col].sum()` for True count and `(~df[col]).sum()` for False count.

## Why It Matters

A change in data distribution could silently flip the labels on pie/bar charts without raising an error.

## Source

Fatal Force — mental illness pie chart used `value_counts()` with manually matched label list.
