# Data Quality Report

> **Status: Pending execution with source dataset**

This report is intentionally a template. No data-quality result is asserted here until the source dataset is present in `data/raw/` and the validation pipeline is executed.

## Expected source
- Dataset: Tableau Public **Superstore Sales / Sample - Superstore**
- Official source: https://public.tableau.com/app/learn/sample-data
- Expected schema: 21 columns documented in `data/README.md`.

## Checks performed by the pipeline
1. File discovery and readable format (CSV/XLS/XLSX)
2. Exact schema validation
3. Actual row/column count
4. Missing values by column and total missing cells
5. Exact duplicate row count
6. Data types after parsing
7. Order-date range
8. Unique customers, orders, and products
9. Numeric validity for Sales, Quantity, Discount, and Profit
10. Ship Date earlier than Order Date

## Execution
Run:

```bash
pip install -r requirements.txt
python src/data_cleaning.py
python src/analysis.py
python src/visualization.py
```

The scripts fail clearly if the dataset is missing; they do not invent values.

## Results
**Not yet executed in this repository because the source dataset file is not present in the execution environment.**
