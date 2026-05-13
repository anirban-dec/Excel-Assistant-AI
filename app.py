import pandas as pd
import streamlit as st
st.title("AI Excel Assistant")

# 1. Upload file setup 
uploaded_file = st.file_uploader("Upload your excel file", type=["xlsx"])

# 2. Preview File
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Dataset Preview")
    st.dataframe(df)

# 3. Adding KPIs
    st.subheader("Dataset Information")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

# 4. More detailing KIPs (Sales)
    st.subheader("Sales KPI")
    st.write("Total Sales:", df["Sales"].sum())
    st.write("Average Sales:", df["Sales"].mean())
    st.write("maximum Sales:", df["Sales"].max())

# 5. Adding Charts
    st.subheader("Sales Chart")
    st.bar_chart(df["Sales"])

# 6. Adding Filters
    region = st.selectbox(
        "Select Region", df["Region"].unique()
    )

    filtered_df = df[df["Region"] == region]
    st.dataframe(filtered_df)

# 7. Basic Business Insights (Top region with sales)
    region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
)
    top_region = region_sales.idxmax()
    top_region_sales = region_sales.max()
    st.write(
    "Top Region:",
    top_region,
    top_region_sales
)   

# Top Product with Sales
    product_sales = (df.groupby("Product")["Sales"].sum())
    best_product = product_sales.idxmax()
    best_product_sales = product_sales.max()
    st.write("Best Product:", best_product, " ",best_product_sales)

# Lowest Month
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month_name()
    month_sales = (df.groupby("Month")["Sales"].sum())
    lowest_month = month_sales.idxmin()
    lowest_month_sales = month_sales[lowest_month].sum()
    st.write("Lowest Month:", lowest_month, " ",lowest_month_sales)

# Growth %

    df["Month"] = df["Date"].dt.to_period("M")
    monthly_sales = (df.groupby("Month")["Sales"].sum())
    growth_percent = round(monthly_sales.pct_change() * 100,2)
    st.write("Growth% :", growth_percent)

# Improve UI
    col1, col2 = st.columns(2)
    col1.metric("Total Sales", df["Sales"].sum())
    col2.metric("Average Sales", df["Sales"].mean())