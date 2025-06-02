# ------------------------------------------------------------
# 📝 Project Overview:
# ------------------------------------------------------------
# Hello team!
#
# I’ve developed an intuitive app that demonstrates data analysis
# features using a retail store dataset.
#
# I chose this real-life scenario to simulate how a shop could 
# visualize its data trends in a meaningful way. 
#
# The goal is to help businesses understand customer behavior 
# and spending patterns so they can grow more efficiently.
#
# Initially, I tried using the YC dataset (data/yc-companies.csv)
# to showcase the same logic, but faced some issues (explained below).

# ------------------------------------------------------------
#  Bug Report – Table Display Glitch:
# ------------------------------------------------------------
# While testing with the YC dataset, I noticed that whenever a text 
# field (e.g., company description) is too long, the table display 
# becomes misaligned or overflows.
#
# This leads to a poor layout and makes the data hard to read,also effects the query.
#
# Consider:
# - Auto-wrapping long text
# - Using tooltips for overflowing text
# - Dynamically adjusting row height

# ------------------------------------------------------------
# 🗑️ Feature Request – File Deletion Option:
# ------------------------------------------------------------
# Currently, there's no option to delete files (like unused CSVs) 
# directly from the app.
#
# I found myself needing this when experimenting with multiple datasets.

from preswald import connect, get_df, query, table, text, plotly
import pandas as pd
import plotly.express as px

connect()
# 1. Load the dataset
df = pd.read_csv("data/Shop.csv", header=0)

# Ensure numeric columns are properly typed
numeric_cols = ["Age", "Purchase Amount (USD)", "Review Rating", "Previous Purchases", "Discount Applied"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["Purchase Amount (USD)", "Age", "Gender", "Location"])


text("# Customer Spending certain amount")
# 2. Query or manipulate the data
sql_high_spenders = """
SELECT "Customer ID", "Age", "Gender", "Location", "Purchase Amount (USD)"
FROM "data/Shop.csv"
WHERE CAST("Purchase Amount (USD)" AS DOUBLE) = 99
ORDER BY "Purchase Amount (USD)" DESC
LIMIT 10
"""
high_spenders = query(sql_high_spenders, "data/Shop.csv")

text("These are the **top 10 customers** who spent $99 in a single purchase.")
table(high_spenders, title="99$ Customer")

text("## ️ Top Spending Locations")
# 3. Build an interactive UI
sql_locations = """
SELECT "Location", SUM(CAST("Purchase Amount (USD)" AS DOUBLE)) AS "Total Spend"
FROM "data/Shop.csv"
GROUP BY "Location"
ORDER BY "Total Spend" DESC
LIMIT 10
"""
top_locations = query(sql_locations, "data/Shop.csv")

table(top_locations, title="Top 10 Locations by Total Spend")


text("##  Age vs. Purchase Amount by Gender")
# 4. Create a visualization
fig1 = px.scatter(
    df,
    x="Age",
    y="Purchase Amount (USD)",
    color="Gender",
    hover_data=["Customer ID", "Location"],
    title="Customer Age vs Purchase Amount"
)
plotly(fig1)


fig2 = px.bar(
    top_locations,
    x="Location",
    y="Total Spend",
    title=" Top 10 Locations by Purchase Amount",
    color="Total Spend",
    text_auto=True
)
plotly(fig2)
text("##  Gender Distribution")

gender_counts = df["Gender"].value_counts().reset_index()
gender_counts.columns = ["Gender", "Count"]

fig_pie_gender = px.pie(
    gender_counts,
    names="Gender",
    values="Count",
    title="Customer Gender Distribution",
    color_discrete_sequence=px.colors.sequential.RdBu
)
plotly(fig_pie_gender)

