# Dec 2025 Tech Salary Benchmarking Cross Market Analysis for Competitive Salary Bands

## Introduction 
Tech salaries vary widely across locations because of:
- local talent demand vs offer
- cost of living
- market maturity
- seniority expectations
- competitiveness

For the People Team, creating salary bands that are competitive, fair and market aligned per location supports:
- hiring ease and strategy
- retention
- equity
- forecasting costs
- global mobility/relocation decisions

Because markets use different currencies, all compensation figures will be standardised into GBP for consistent comparison.

## Data Sources
- Mercer Comptryx dataset
- Job Salary Data API

## Methodology

1. Data loading
- Imported cleaned datasets from data/processed/mercer_clean.csv and data/processed/api_clean.csv.
- Mercer data provides employer-reported market benchmarks.
- API/Glassdoor data provides employee-reported salary estimates.

2. Standardisation
- Normalised both sources into a common schema:
    - location
    - role_bucket (role category)
    - job_level
    - salary_gbp (annual base salary in GBP)
- Converted all salaries to annual GBP to allow direct cross-market comparison.

3. Location aggregation
- Mercer and API locations were aligned to the same target markets:
    - London (UK)
    - Portugal (Lisbon aggregated to Portugal)
    - Sweden (Malmö/Lund aggregated to Sweden)
    - New York (Tri-State / New York State aggregated to New York)
- API runs did not return London values; therefore London comparisons rely on Mercer only.

4. Role mapping
- Standardised job titles into four role buckets to match Mercer structure:
    - Full Stack Engineer
    - Mobile Engineer
    - UX Designer
    - QA Engineer
- Several API titles (e.g., backend/frontend/software developer/software engineer) were grouped into Full Stack Engineer.

5. Level mapping
- API and Mercer seniority levels were mapped to a shared order:
    - Junior → Mid → Senior → Lead → Principal → Head of

6. Exploratory analysis
- Produced:
    - Heatmaps per location showing salary progression across roles and levels.
    - Line charts showing role progression by level (averaged across locations).
    - Cross-source gap chart showing % difference where Mercer/API overlaps exist.

7. Gap calculation
- Overlapping role/location pairs.
- Negative gaps indicate API salaries are lower than Mercer benchmarks.

8. Limitations
- API overlaps are limited to a small subset of roles/locations, so the size of gaps should be interpreted as directional rather than definitive.
- Missing London data in API prevents full cross-source validation for the UK market.

## Conclusions

### Clear seniority progression in Mercer.
Across all Mercer markets, pay rises steadily from Junior to Head of, with the steepest jumps occurring at senior levels (Senior → Lead and above).

### Market ranking is consistent.
New York is the highest-paying market across roles and levels, followed by London. Portugal and Sweden are lower-paying markets but show similar upward level slopes.

### Role patterns differ by seniority.
At early levels, Full Stack tends to move ahead faster than UX; however at top levels (Principal/Head of) UX reaches or exceeds Full Stack in several markets, suggesting senior UX roles command strong premiums.

### API/Glassdoor salaries are substantially lower in overlaps.
In every overlapping role/location pair, API mean salaries fall below Mercer P50, with gaps ranging roughly from -13% to -56%. The largest gaps appear in Portugal and New York, especially for UX and Full Stack.

### Interpretation of source differences.
The consistent negative gap suggests structural differences between the datasets: Mercer reflects employer benchmark targets, while Glassdoor reflects employee-reported realised pay (often from smaller samples and with more variation).

### Next steps:
- Expand API coverage (more roles + more locations, especially London) to validate whether gaps persist with a larger overlap.
- Compare additional Mercer percentiles (P25/P75) to see whether API aligns better with lower-quartile market pay.
- If used for compensation planning, treat API as a directional signal and Mercer as the formal benchmarking baseline.

## Links 
Slide deck findings presentation: https://www.canva.com/design/DAG6EsiIxzA/9ZJDIPWMAGB5G8nhRTfErQ/edit?ui=eyJBIjp7fX0