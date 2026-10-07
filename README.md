# Sales Business Intelligence Dashboard

End-to-end sales analytics portfolio project demonstrating data validation, cleaning, SQL business analysis, Python EDA, KPI design, visualization, and business storytelling.

## Dataset executed

The uploaded Tableau Superstore workbook was analyzed directly.

- File: sample_-_superstore.xlsx
- Sheet: Orders
- Rows: 10,194
- Columns: 21
- Order dates: 2023-01-03 to 2026-12-30
- Duplicate rows: 0
- Missing cells: 0
- Orders: 5,111
- Customers: 804
- Products: 1,862

The raw workbook is not committed because the official sample-data pages do not provide a clear open-source redistribution license.

## Executive snapshot

| KPI | Result |
|---|---:|
| Sales | $2.33M |
| Profit | $292.30K |
| Profit margin | 12.56% |
| Orders | 5,111 |
| Customers | 804 |
| Products | 1,862 |
| Average sales / order | $455.20 |

## Key findings

- Technology leads sales and profit: $839.89K sales and $146.54K profit.
- West leads regions: $739.81K sales and $110.80K profit.
- Tables require profitability attention: $208.02K sales but -$17.75K profit.
- Annual sales rose from $494.04K in 2023 to $745.57K in 2026, but 1,159 rows are dated after 2026-10-07. This trend therefore needs a reporting cutoff before being treated as current operational performance.
- Rows with discounts above 20% show $364.76K sales and -$136.02K profit. This is an observed association, not a causal claim.

## Repository structure

    data/
      README.md
      raw/.gitkeep
    sql/
      01_sales_overview.sql
      02_monthly_sales.sql
      03_product_performance.sql
      04_customer_analysis.sql
      05_regional_analysis.sql
      06_profitability_analysis.sql
      07_discount_analysis.sql
    src/
      data_cleaning.py
      analysis.py
      visualization.py
    reports/
      data_quality_report.md
      data_quality_profile.csv
      insights.md
      category_performance.csv
      regional_performance.csv
      subcategory_performance.csv
    notebooks/
      sales_analysis.ipynb

## Reproducible workflow

1. Keep the raw workbook outside the public repository unless redistribution rights are confirmed.
2. Place a local copy in data/raw/.
3. Install dependencies: pip install -r requirements.txt
4. Run: python src/data_cleaning.py
5. Run: python src/analysis.py
6. Run: python src/visualization.py

The pipeline reads the Orders sheet, validates the exact 21-column schema, cleans dates and numeric fields, profiles data quality, creates analysis tables, and generates charts.

## Recruiter takeaway

This project demonstrates a practical analyst workflow from source-data validation to cleaning, SQL, Python EDA, KPI analysis, visualization, and decision-oriented communication. Reported numbers come from the uploaded workbook, not fabricated examples.
