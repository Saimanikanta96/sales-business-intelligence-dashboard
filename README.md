# Sales Business Intelligence Dashboard

An end-to-end sales analytics portfolio project demonstrating data cleaning, KPI design, SQL business analysis, Python analysis, and dashboard storytelling.

## Business Goals
- Track revenue, profit, orders, and average order value.
- Identify high-performing products, categories, and regions.
- Understand sales trends over time.
- Convert analysis into concise, decision-oriented insights.

## Repository Structure
```
data/
  README.md
  raw/.gitkeep
sql/business_questions.sql
src/sales_analysis.py
dashboard/dashboard_spec.md
reports/insights.md
requirements.txt
.gitignore
README.md
```

## Dataset & Data Integrity
The project uses a legitimate public dataset. The exact publisher, source URL, license/usage terms, download date, schema, and transformations are documented in `data/README.md`. No fabricated business results are included.

## Core Questions
1. What are total revenue, profit, orders, and average order value?
2. How do revenue and profit change by month?
3. Which categories and products drive revenue?
4. Which regions perform best?
5. Which segments require investigation?

## Tech Stack
Python • Pandas • SQL • Power BI/dashboard concepts • Git/GitHub

## Reproducibility
1. Install Python 3.10+.
2. Run `pip install -r requirements.txt`.
3. Download the documented public dataset and place it in `data/raw/`.
4. Map source columns to the canonical fields expected by `src/sales_analysis.py`.
5. Run `python src/sales_analysis.py`.
6. Use the generated KPI output for the dashboard and findings.

## Recruiter Takeaway
This project demonstrates practical analytics workflow: defining business questions, preparing data, writing SQL, calculating KPIs, designing decision-useful visuals, and communicating findings without inventing results.



## Step 3 — Data Cleaning, Validation & EDA

The repository now contains an executable, source-data-driven pipeline for the verified 21-column Sample Superstore schema.

### Pipeline
- `src/data_cleaning.py` — auto-discovers CSV/XLS/XLSX in `data/raw/`, validates the exact schema, parses dates/numerics, profiles missing values/duplicates/types/date range/unique entities, and writes processed data.
- `src/analysis.py` — generates monthly, category, sub-category, regional, segment, customer, product, and discount-band analysis tables.
- `src/visualization.py` — generates reproducible PNG charts for sales trends, category sales, regional profit, sub-category profit, and discount vs profit.
- `notebooks/sales_analysis.ipynb` — executable Jupyter workflow using the same pipeline.
- `sql/01_*.sql` through `sql/07_*.sql` — PostgreSQL-oriented analysis queries using the verified column names.

### Current execution status
**CODE PIPELINE BUILT — DATA EXECUTION PENDING**

The source dataset was not available in the execution environment during this build. Therefore, no missing-value counts, duplicate counts, KPIs, findings, or charts are claimed as executed. The scripts fail clearly when the source file is absent rather than generating fake results.

### To execute locally
1. Download the official Tableau Public **Superstore Sales** sample dataset.
2. Place the downloaded CSV/XLS/XLSX file in `data/raw/`.
3. Run:

```bash
pip install -r requirements.txt
python src/data_cleaning.py
python src/analysis.py
python src/visualization.py
```

Open `notebooks/sales_analysis.ipynb` for the interactive EDA workflow. Generated tables go to `reports/` and charts to `visualizations/`.
