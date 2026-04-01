from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
import plotly.express as px
from flask import Flask, render_template

app = Flask(__name__)

CSV_PATH = Path(os.getenv("COFFEE_CSV", "data/coffee_sales.csv"))


def load_data() -> pd.DataFrame:
    if not CSV_PATH.exists():
        return pd.DataFrame()

    df = pd.read_csv(CSV_PATH)

    if "transaction_date" in df.columns:
        df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")
    if "transaction_time" in df.columns:
        try:
            df["Hour"] = pd.to_datetime(df["transaction_time"], format="%H:%M:%S", errors="coerce").dt.hour
        except Exception:
            pass

    if "transaction_date" in df.columns and "Month Name" not in df.columns:
        df["Month Name"] = df["transaction_date"].dt.month_name()
    if "transaction_date" in df.columns and "Day Name" not in df.columns:
        df["Day Name"] = df["transaction_date"].dt.day_name()

    if "Total_Bill" not in df.columns and {"transaction_qty", "unit_price"}.issubset(df.columns):
        df["Total_Bill"] = df["transaction_qty"] * df["unit_price"]

    return df


def chart_or_empty(df: pd.DataFrame, fig_builder, empty_msg: str) -> str:
    if df.empty:
        return f"<div class='empty'>{empty_msg}</div>"
    fig = fig_builder(df)
    return fig.to_html(full_html=False, include_plotlyjs="cdn")


@app.route("/")
def dashboard() -> str:
    df = load_data()

    if df.empty:
        return render_template(
            "index.html",
            has_data=False,
            csv_path=str(CSV_PATH),
            kpis={},
            hourly_chart="",
            dow_chart="",
            category_chart="",
            store_chart="",
        )

    total_revenue = float(df.get("Total_Bill", pd.Series(dtype=float)).fillna(0).sum())
    total_txns = int(df["transaction_id"].nunique()) if "transaction_id" in df.columns else len(df)
    avg_bill = float(df.get("Total_Bill", pd.Series(dtype=float)).fillna(0).mean())

    best_category = "N/A"
    if {"product_category", "Total_Bill"}.issubset(df.columns):
        best_category = (
            df.groupby("product_category", as_index=False)["Total_Bill"].sum().sort_values("Total_Bill", ascending=False).head(1)["product_category"].iloc[0]
        )

    kpis = {
        "total_revenue": f"${total_revenue:,.2f}",
        "total_transactions": f"{total_txns:,}",
        "avg_bill": f"${avg_bill:,.2f}",
        "best_category": best_category,
    }

    hourly_chart = chart_or_empty(
        df,
        lambda d: px.line(
            d.groupby("Hour", as_index=False)["Total_Bill"].sum(),
            x="Hour",
            y="Total_Bill",
            title="Sales by Hour",
            markers=True,
        ) if {"Hour", "Total_Bill"}.issubset(d.columns) else px.scatter(title="Sales by Hour (missing columns)"),
        "No hourly data available.",
    )

    dow_chart = chart_or_empty(
        df,
        lambda d: px.bar(
            d.groupby("Day Name", as_index=False)["Total_Bill"].sum(),
            x="Day Name",
            y="Total_Bill",
            title="Sales by Day of Week",
        ) if {"Day Name", "Total_Bill"}.issubset(d.columns) else px.scatter(title="Sales by Day (missing columns)"),
        "No day-of-week data available.",
    )

    category_chart = chart_or_empty(
        df,
        lambda d: px.bar(
            d.groupby("product_category", as_index=False)["Total_Bill"].sum().sort_values("Total_Bill", ascending=False).head(10),
            x="product_category",
            y="Total_Bill",
            title="Revenue by Product Category",
        ) if {"product_category", "Total_Bill"}.issubset(d.columns) else px.scatter(title="Category chart (missing columns)"),
        "No category data available.",
    )

    store_chart = chart_or_empty(
        df,
        lambda d: px.bar(
            d.groupby("store_location", as_index=False)["Total_Bill"].sum().sort_values("Total_Bill", ascending=False),
            x="store_location",
            y="Total_Bill",
            title="Revenue by Store Location",
        ) if {"store_location", "Total_Bill"}.issubset(d.columns) else px.scatter(title="Store chart (missing columns)"),
        "No store data available.",
    )

    return render_template(
        "index.html",
        has_data=True,
        csv_path=str(CSV_PATH),
        kpis=kpis,
        hourly_chart=hourly_chart,
        dow_chart=dow_chart,
        category_chart=category_chart,
        store_chart=store_chart,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")), debug=False)
