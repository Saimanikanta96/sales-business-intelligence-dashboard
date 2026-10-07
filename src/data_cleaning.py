"""Load, validate, clean, and profile the uploaded Superstore workbook."""
from __future__ import annotations
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
CLEAN_DIR = ROOT / "data" / "processed"

EXPECTED_COLUMNS = [
    "Row ID", "Order ID", "Order Date", "Ship Date", "Ship Mode",
    "Customer ID", "Customer Name", "Segment", "Country/Region", "City",
    "State/Province", "Postal Code", "Region", "Product ID", "Category",
    "Sub-Category", "Product Name", "Sales", "Quantity", "Discount", "Profit",
]
NUMERIC_COLUMNS = ["Row ID", "Sales", "Quantity", "Discount", "Profit"]
DATE_COLUMNS = ["Order Date", "Ship Date"]

def discover_dataset() -> Path:
    candidates = sorted(RAW_DIR.glob("*.csv")) + sorted(RAW_DIR.glob("*.xlsx")) + sorted(RAW_DIR.glob("*.xls"))
    if not candidates:
        raise FileNotFoundError("Place the Superstore CSV/XLS/XLSX workbook in data/raw/.")
    return candidates[0]

def load_raw(path: Path | None = None) -> pd.DataFrame:
    path = path or discover_dataset()
    if path.suffix.lower() == ".csv":
        try:
            return pd.read_csv(path, encoding="utf-8-sig")
        except UnicodeDecodeError:
            return pd.read_csv(path, encoding="latin-1")
    return pd.read_excel(path, sheet_name="Orders")

def validate_schema(df: pd.DataFrame) -> None:
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    extra = [c for c in df.columns if c not in EXPECTED_COLUMNS]
    if missing or extra:
        raise ValueError(f"Schema mismatch. Missing columns: {missing}; unexpected columns: {extra}")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    validate_schema(df)
    out = df.copy()
    for col in DATE_COLUMNS:
        out[col] = pd.to_datetime(out[col], errors="coerce")
    for col in NUMERIC_COLUMNS:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    for col in ["Order ID", "Customer ID", "Product ID"]:
        out[col] = out[col].astype("string").str.strip()
    return out

def quality_profile(df: pd.DataFrame) -> dict:
    today = pd.Timestamp.today().normalize()
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_cells": int(df.isna().sum().sum()),
        "missing_by_column": df.isna().sum().to_dict(),
        "dtypes": {k: str(v) for k, v in df.dtypes.items()},
        "order_date_min": str(df["Order Date"].min().date()),
        "order_date_max": str(df["Order Date"].max().date()),
        "unique_customers": int(df["Customer ID"].nunique(dropna=True)),
        "unique_orders": int(df["Order ID"].nunique(dropna=True)),
        "unique_products": int(df["Product ID"].nunique(dropna=True)),
        "invalid_sales": int((df["Sales"] < 0).sum()),
        "invalid_quantity": int((df["Quantity"] <= 0).sum()),
        "invalid_discount": int(((df["Discount"] < 0) | (df["Discount"] > 1)).sum()),
        "ship_before_order": int((df["Ship Date"] < df["Order Date"]).sum()),
        "future_order_dates": int((df["Order Date"] > today).sum()),
    }

def main() -> None:
    path = discover_dataset()
    cleaned = clean_data(load_raw(path))
    profile = quality_profile(cleaned)
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(CLEAN_DIR / "superstore_cleaned.csv", index=False)
    pd.DataFrame({"column": list(profile["missing_by_column"]),
                  "missing_count": list(profile["missing_by_column"].values())}).to_csv(
        CLEAN_DIR / "missing_values.csv", index=False)
    print(f"Loaded Orders sheet: {path}")
    for key, value in profile.items():
        if key != "missing_by_column":
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
