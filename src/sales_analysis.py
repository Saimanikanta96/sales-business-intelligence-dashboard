"""Sample Superstore validation and KPI pipeline.

Source:
https://public.tableau.com/app/learn/sample-data

The raw dataset is intentionally not committed because the official
Tableau sample-data pages do not state an open redistribution license.

Place the downloaded Orders data at:
data/raw/Sample - Superstore.csv
"""

from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

EXPECTED_COLUMNS = [
    "Row ID", "Order ID", "Order Date", "Ship Date", "Ship Mode",
    "Customer ID", "Customer Name", "Segment", "Country", "City",
    "State", "Postal Code", "Region", "Product ID", "Category",
    "Sub-Category", "Product Name", "Sales", "Quantity", "Discount", "Profit",
]

def load_source(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, encoding="utf-8-sig")
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin-1")

def validate_schema(df: pd.DataFrame) -> None:
    actual = list(df.columns)
    if actual != EXPECTED_COLUMNS:
        missing = [c for c in EXPECTED_COLUMNS if c not in actual]
        extra = [c for c in actual if c not in EXPECTED_COLUMNS]
        raise ValueError(
            f"Unexpected schema. Missing={missing}; Extra={extra}; Actual={actual}"
        )

def profile(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "column": df.columns,
        "dtype": [str(x) for x in df.dtypes],
        "missing": [int(x) for x in df.isna().sum()],
        "unique_values": [int(x) for x in df.nunique(dropna=True)],
    })

def prepare(df: pd.DataFrame) -> pd.DataFrame:
    validate_schema(df)
    out = df.copy()
    out["Order Date"] = pd.to_datetime(out["Order Date"], errors="coerce")
    out["Ship Date"] = pd.to_datetime(out["Ship Date"], errors="coerce")
    for col in ["Sales", "Quantity", "Discount", "Profit"]:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    return out

def build_kpis(df: pd.DataFrame) -> pd.DataFrame:
    orders = df["Order ID"].nunique()
    return pd.DataFrame([{
        "total_sales": df["Sales"].sum(),
        "total_profit": df["Profit"].sum(),
        "total_orders": orders,
        "average_order_value": df["Sales"].sum() / orders if orders else 0,
        "profit_margin": df["Profit"].sum() / df["Sales"].sum() if df["Sales"].sum() else 0,
    }])

if __name__ == "__main__":
    files = sorted(RAW_DIR.glob("*.csv"))
    if not files:
        raise FileNotFoundError(
            "Download Sample - Superstore from the official Tableau source "
            "and place the Orders CSV in data/raw/."
        )

    raw = load_source(files[0])
    sales = prepare(raw)

    profile(sales).to_csv(OUTPUT_DIR / "data_quality_profile.csv", index=False)
    build_kpis(sales).to_csv(OUTPUT_DIR / "kpis.csv", index=False)

    print(f"Rows: {len(sales):,}")
    print(f"Columns: {len(sales.columns)}")
    print(f"Duplicate rows: {sales.duplicated().sum():,}")
    print(f"Missing cells: {int(sales.isna().sum().sum()):,}")
    print(f"Order date range: {sales['Order Date'].min().date()} to {sales['Order Date'].max().date()}")
    print("Outputs written to outputs/")
