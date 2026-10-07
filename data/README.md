# Data Source & Documentation

## Source policy
Use a legitimate public sales/retail dataset. Record the dataset name, original publisher, source URL, license/usage terms, download date, file name, and transformations.

The repository must not contain confidential, private, restricted, or fabricated business data.

## Raw data
Place the downloaded source file under `data/raw/`.

## Canonical fields
The analysis script expects these fields:
- `order_id`
- `order_date`
- `sales`
- `profit`

If the public dataset uses different names, document the mapping here before analysis.

## Data dictionary
After selecting the dataset, document each actual column, its meaning, data type, missing-value treatment, and transformation.
