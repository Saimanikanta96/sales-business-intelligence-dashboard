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

