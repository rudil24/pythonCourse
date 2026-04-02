# Retrospective: Fatal Force Notebook — Day 100 Capstone

__Date:__ 2026-04-01
__Scope:__ Complete Fatal_Force_Claude.ipynb from blank skeleton to fully executed data analysis notebook

## Summary

The team one-shot completed a 76-cell Jupyter notebook covering data exploration, cleaning, and 15+ charts across 5 datasets. The highest-value addition was an unasked-for per-capita killing rate chart using hardcoded 2015 Census data, which surfaced the actual Washington Post story (Black Americans killed at 2.5x the White per-capita rate).

## What Went Well

- One-shot notebook completion from skeleton with no human course-correction on the analysis itself
- Proactive data type inspection before charting prevented silent aggregation errors
- Per-capita race rate chart went beyond the prompt and delivered the analytically meaningful story
- Dual-DataFrame approach (raw counts + normalized rates) is now a reusable pattern for any demographic analysis

## What Could Be Improved

- Boot sequence asked the owner for their directive instead of reading `owner.txt` first — wakeup flow should check for a directive file before surfacing to the user
- `NotebookEdit` failed twice on an open `.ipynb` file (VS Code auto-save conflict); should detect `nbformat < 4.1` and go straight to JSON manipulation
- Boolean `value_counts()` label mapping is order-dependent and fragile — use explicit boolean filtering instead
- City-name joins across the two datasets were approximate; FIPS-code joins are required for production accuracy

## Learnings Extracted

- L1: Check nbformat version before using NotebookEdit — fall back to JSON if < 4.1
- L2: Cast all CSV numeric columns immediately after load; government data ships as strings
- L3: Always pair raw counts with per-capita rates when comparing unequal-size population groups
- L4: City-name joins require state scope or FIPS codes to avoid ambiguous multi-state matches
- L5: Read `owner.txt` (or equivalent directive file) as part of wakeup before asking the owner for input
- L6: Use explicit boolean filtering instead of `value_counts()` label mapping for pie/bar charts

See: `.agents/learnings/2026-04-01-fatal-force-notebook.md`

## Action Items

- [ ] Update teamlead-wakeup SKILL.md to include: check for `owner.txt` before prompting the user
- [ ] Add nbformat version check to standard notebook editing checklist in GLOBAL_EVOLUTION.md
