"""Generate reproducible EDA charts from the cleaned Sample Superstore data."""
from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from data_cleaning import discover_dataset, load_raw, clean_data
from analysis import build_analysis_tables

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "visualizations"


def save_plot(fig, name: str) -> None:
    OUT.mkdir(exist_ok=True)
    fig.tight_layout()
    fig.savefig(OUT / name, dpi=160, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    df = clean_data(load_raw(discover_dataset()))
    tables = build_analysis_tables(df)
    monthly = tables["monthly_sales_profit"]
    fig, ax = plt.subplots(figsize=(10,5)); ax.plot(monthly["Month"], monthly["Sales"], marker="o"); ax.set_title("Monthly Sales"); ax.set_xlabel("Month"); ax.set_ylabel("Sales"); ax.tick_params(axis="x", rotation=60); save_plot(fig, "monthly_sales.png")
    cat = tables["category_performance"].sort_values("Sales", ascending=False)
    fig, ax = plt.subplots(figsize=(8,5)); ax.bar(cat["Category"], cat["Sales"]); ax.set_title("Sales by Category"); ax.set_ylabel("Sales"); save_plot(fig, "sales_by_category.png")
    reg = tables["regional_performance"].sort_values("Profit", ascending=False)
    fig, ax = plt.subplots(figsize=(8,5)); ax.bar(reg["Region"], reg["Profit"]); ax.set_title("Profit by Region"); ax.set_ylabel("Profit"); save_plot(fig, "profit_by_region.png")
    sub = tables["subcategory_performance"].sort_values("Profit")
    fig, ax = plt.subplots(figsize=(9,7)); ax.barh(sub["Sub-Category"], sub["Profit"]); ax.set_title("Profit by Sub-Category"); ax.set_xlabel("Profit"); save_plot(fig, "profit_by_subcategory.png")
    fig, ax = plt.subplots(figsize=(8,5)); ax.scatter(df["Discount"], df["Profit"], alpha=0.35); ax.set_title("Discount vs Profit"); ax.set_xlabel("Discount"); ax.set_ylabel("Profit"); save_plot(fig, "discount_vs_profit.png")
    print(f"Generated charts in {OUT}")

if __name__ == "__main__": main()
