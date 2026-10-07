"""Reproducible sales KPI pipeline.

Place a documented public CSV in data/raw/ and map its columns to:
order_id, order_date, sales, profit.
"""

from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def load_sales_file(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def prepare(df: pd.DataFrame) -> pd.DataFrame:
    required = {"order_id", "order_date", "sales", "profit"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing canonical columns: {sorted(missing)}")
    out = df.copy()
    out["order_date"] = pd.to_datetime(out["order_date"], errors="coerce")
    out["sales"] = pd.to_numeric(out["sales"], errors="coerce")
    out["profit"] = pd.to_numeric(out["profit"], errors="coerce")
    return out.dropna(subset=["order_id", "order_date", "sales"])

def build_kpis(df: pd.DataFrame) -> pd.DataFrame:
    orders = df["order_id"].nunique()
    return pd.DataFrame([{
        "total_sales": df["sales"].sum(),
        "total_profit": df["profit"].sum(),
        "total_orders": orders,
        "average_order_value": df["sales"].sum() / orders if orders else 0,
    }])

if __name__ == "__main__":
    files = sorted(RAW_DIR.glob("*.csv"))
    if not files:
        raise FileNotFoundError("Add the documented public CSV to data/raw/ first.")
    sales = prepare(load_sales_file(files[0]))
    build_kpis(sales).to_csv(OUTPUT_DIR / "kpis.csv", index=False)
    print("KPI analysis complete: outputs/kpis.csv")
