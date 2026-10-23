# Data Quality Report

## Execution status

REAL DATA EXECUTION COMPLETE using the uploaded sample_-_superstore.xlsx workbook.

The workbook contains Orders, People, and Returns sheets. This analysis uses the Orders sheet because it contains the row-level sales transaction fields.

## Dataset profile

| Check | Result |
|---|---:|
| Rows | 10,194 |
| Columns | 21 |
| Order date range | 2023-01-03 to 2026-12-30 |
| Unique orders | 5,111 |
| Unique customers | 804 |
| Unique products | 1,862 |
| Duplicate rows | 0 |
| Missing cells | 0 |
| Negative sales | 0 |
| Non-positive quantity | 0 |
| Invalid discount | 0 |
| Ship date before order date | 0 |
| Order dates after 2026-10-07 | 1,159 |

## Observed schema

Row ID, Order ID, Order Date, Ship Date, Ship Mode, Customer ID, Customer Name, Segment, Country/Region, City, State/Province, Postal Code, Region, Product ID, Category, Sub-Category, Product Name, Sales, Quantity, Discount, Profit.

## Data-quality interpretation

The transaction table is structurally clean: no missing cells or duplicate rows were observed, and the basic numeric and date validation checks passed.

One important issue requires documentation: 1,159 order rows have dates after the execution date of 2026-10-07, extending through 2026-12-30. These rows were not deleted. A real operational dashboard should confirm whether they are sample/forecast dates or apply an explicit reporting cutoff.

## Data handling

The raw workbook is not committed to the public repository. The repository contains reproducible code, derived analysis tables, documentation, and visualization artifacts.
