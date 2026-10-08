# Sales Business Intelligence Dashboard

An end-to-end Data Analytics and Business Intelligence portfolio project demonstrating data validation, data cleaning, SQL business analysis, Python EDA, KPI analysis, visualization, and interactive dashboard development.

## Why this project

The goal is to turn raw sales data into business-focused analysis that helps answer questions about sales, profitability, products, customers, regions, and discount behavior.

## Dataset

The uploaded Tableau Superstore workbook was analyzed directly.

- File: `sample_-_superstore.xlsx`
- Sheet: `Orders`
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

## Analytics workflow

**Raw data → validation → cleaning → SQL analysis → Python EDA → KPI analysis → visualization → interactive dashboard → business insights**

### Technologies

- SQL
- Python
- Pandas
- Data Analysis
- Exploratory Data Analysis (EDA)
- Data Visualization
- HTML
- JavaScript
- Chart.js

## Dashboard

The project includes a responsive interactive dashboard at `dashboard/index.html`, designed around modern Business Intelligence reporting patterns.

It includes:

- KPI cards for sales, profit, margin, orders, customers, and products
- Monthly Sales & Profit trend
- Category sales/profit comparison
- Regional sales distribution
- Top products by sales
- Discount-band profitability analysis
- Evidence-based key insights
- Responsive desktop/tablet/mobile layout
- Dashboard navigation and search functionality

The dashboard uses Chart.js from its public CDN and embeds derived aggregate data; the raw workbook is not exposed.

## Key findings

- Technology leads sales and profit: $839.89K sales and $146.54K profit.
- West leads regions: $739.81K sales and $110.80K profit.
- Tables require profitability attention: $208.02K sales but -$17.75K profit.
- Annual sales rose from $494.04K in 2023 to $745.57K in 2026, but 1,159 rows are dated after 2026-10-07. This trend needs a reporting cutoff before being treated as current operational performance.
- Rows with discounts above 20% show $364.76K sales and -$136.02K profit. This is an observed association, not a causal claim.

## Repository structure

```
dashboard/
  index.html
  dashboard_spec.md
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
```

## Reproducible workflow

1. Keep the raw workbook outside the public repository unless redistribution rights are confirmed.
2. Place a local copy in `data/raw/`.
3. Install dependencies: `pip install -r requirements.txt`
4. Run `python src/data_cleaning.py`
5. Run `python src/analysis.py`
6. Run `python src/visualization.py`

The pipeline reads the Orders sheet, validates the exact 21-column schema, cleans dates and numeric fields, profiles data quality, creates analysis tables, and generates visualizations.

## Recruiter takeaway

This project demonstrates a practical Data Analyst workflow from source-data validation and cleaning through SQL, Python EDA, KPI analysis, interactive dashboard development, and business-focused communication.

The project is intentionally documented around **evidence rather than exaggerated claims**. Reported numbers come from the analyzed workbook.

## Career focus

This project is part of a broader portfolio focused on **Data Analytics and Data Science**, with emphasis on SQL, Python, Excel, Power BI, data visualization, statistics, business intelligence, and practical analytical problem solving.
