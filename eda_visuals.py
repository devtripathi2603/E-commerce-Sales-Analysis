# eda_visuals.py
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_top_products(df, group_col="PRODUCTLINE", out_dir="plots"):
    os.makedirs(out_dir, exist_ok=True)
    top = df.groupby(group_col)["SALES"].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(9,6))
    sns.barplot(x=top.values, y=top.index)
    plt.title("Top 10 Product Lines by Sales")
    plt.xlabel("Sales")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "top_products.png"))

def plot_monthly_sales(df, date_col="ORDERDATE", out_dir="plots"):
    os.makedirs(out_dir, exist_ok=True)
    df["ORDER_MONTH"] = pd.to_datetime(df[date_col]).dt.to_period("M").astype(str)
    monthly = df.groupby("ORDER_MONTH")["SALES"].sum().reset_index()
    monthly["ORDER_MONTH"] = pd.to_datetime(monthly["ORDER_MONTH"])
    plt.figure(figsize=(10,5))
    plt.plot(monthly["ORDER_MONTH"], monthly["SALES"], marker='o')
    plt.title("Monthly Sales Trend")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "monthly_sales.png"))

def plot_region_pie(df, region_col="COUNTRY", out_dir="plots"):
    os.makedirs(out_dir, exist_ok=True)
    reg = df.groupby(region_col)["SALES"].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.pie(reg, names=region_col, values="SALES", title="Sales by Region")
    fig.write_image(os.path.join(out_dir, "sales_by_region.png"))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    df = pd.read_csv(args.input)
    plot_top_products(df)
    plot_monthly_sales(df)
