"""Exploratory analysis for the verified Sample Superstore schema."""
from __future__ import annotations
from pathlib import Path
import pandas as pd
from data_cleaning import discover_dataset, load_raw, clean_data

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "reports"


def build_analysis_tables(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    x = df.copy()
    x["Year"] = x["Order Date"].dt.year
    x["Month"] = x["Order Date"].dt.to_period("M").astype(str)
    return {
        "monthly_sales_profit": x.groupby("Month", as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Orders=("Order ID","nunique")),
        "category_performance": x.groupby("Category", as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Quantity=("Quantity","sum"), Orders=("Order ID","nunique")),
        "subcategory_performance": x.groupby("Sub-Category", as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Quantity=("Quantity","sum"), Orders=("Order ID","nunique")).sort_values("Profit", ascending=False),
        "regional_performance": x.groupby("Region", as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Orders=("Order ID","nunique"), Customers=("Customer ID","nunique")),
        "segment_performance": x.groupby("Segment", as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Orders=("Order ID","nunique"), Customers=("Customer ID","nunique")),
        "customer_performance": x.groupby(["Customer ID","Customer Name"], as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Orders=("Order ID","nunique")).sort_values("Sales", ascending=False),
        "product_performance": x.groupby(["Product ID","Product Name"], as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Quantity=("Quantity","sum"), Orders=("Order ID","nunique")).sort_values("Sales", ascending=False),
        "discount_profitability": x.assign(DiscountBand=pd.cut(x["Discount"], bins=[-0.001,0,0.10,0.20,0.30,0.50,1.0], labels=["0%","1-10%","11-20%","21-30%","31-50%","51%+"])).groupby("DiscountBand", observed=False, as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Orders=("Order ID","nunique")),
    }


def main() -> None:
    path = discover_dataset()
    df = clean_data(load_raw(path))
    OUTPUT.mkdir(exist_ok=True)
    tables = build_analysis_tables(df)
    for name, table in tables.items():
        table.to_csv(OUTPUT / f"{name}.csv", index=False)
    print("Analysis executed successfully.")
    for name, table in tables.items(): print(f"{name}: {len(table)} rows")

if __name__ == "__main__":
    main()
