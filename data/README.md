# Dataset Source & Data Profile

## Dataset
**Sample - Superstore / Superstore Sales**

Tableau identifies Superstore as a sample dataset containing products, customers, sales, dates, geographic fields, categories, and profit-related measures. Tableau describes it as data for a fictitious retail company. citeturn0search0turn0search1

## Official source
Tableau Public Sample Data:
https://public.tableau.com/app/learn/sample-data

Tableau documentation also points users to the Tableau Public sample-data page to download Superstore. citeturn0search0turn0search2

## Redistribution decision
The official Tableau pages found for this dataset provide a download but do **not** state an open-source redistribution license for the raw Superstore file. Therefore, this repository will **not redistribute the raw dataset at this stage**.

Download the dataset from the official Tableau source and place the file at:

`data/raw/Sample - Superstore.csv`

If your downloaded version is an Excel workbook, export the Orders sheet to CSV while preserving the original values and document that conversion.

## Verified dataset profile
Public documentation and the commonly distributed Tableau Superstore Orders dataset identify:
- **Rows:** 9,994
- **Columns:** 21
- **Order period:** 2014–2017; commonly documented range is 2014-01-03 through 2017-12-30.
- **Granularity:** order-line/item-level records.

Tableau describes the data as disaggregated, with each row representing an item in a transaction that can be aggregated by Order ID, date, customer, region, category, and other dimensions. citeturn0search1turn4search7

## Actual columns
1. Row ID
2. Order ID
3. Order Date
4. Ship Date
5. Ship Mode
6. Customer ID
7. Customer Name
8. Segment
9. Country
10. City
11. State
12. Postal Code
13. Region
14. Product ID
15. Category
16. Sub-Category
17. Product Name
18. Sales
19. Quantity
20. Discount
21. Profit

The 21-field schema is independently documented in public analyses of the same Sample Superstore dataset. citeturn4search7turn0search14

## Dimensions
- Date: Order Date, Ship Date
- Customer: Customer ID, Customer Name, Segment
- Geography: Country, City, State, Postal Code, Region
- Product: Product ID, Product Name, Category, Sub-Category
- Shipping: Ship Mode

## Measures
- Sales
- Quantity
- Discount
- Profit

## Data-quality status
**Not yet independently computed from the official downloaded file in this execution.**

Therefore this repository intentionally does **not** claim a missing-value count, duplicate count, or other quality statistic yet. Those values will be generated from the actual downloaded file before analysis conclusions are written.

## Required validation
After placing the source file in `data/raw/`, run the analysis pipeline. It will validate:
- column names
- data types
- date parsing
- missing values
- duplicate rows
- numeric fields
- invalid dates/values
