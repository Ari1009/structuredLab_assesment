# ShopSight – Retail Data Visualization App

**ShopSight** is a data visualization application designed to help retail stores analyze customer purchase behavior, identify top-performing locations, and uncover actionable insights through clean, interactive dashboards.

---

## Project Overview

This app simulates a real-world use case for a retail store. It uses a sample dataset to demonstrate how businesses can leverage their data to:

- Understand customer spending habits
- Explore customer demographics
- Identify high-revenue locations
- Visualize sales trends

The project is structured to be flexible, with SQL-like querying and dynamic plots that allow for deeper insights.

---

## Features Implemented

### Data Cleaning
- Converts relevant columns (Age, Purchase Amount, etc.) to numeric types
- Drops rows with missing values in key fields to maintain integrity

### SQL-Based Querying
- Query to find customers who spent exactly $99
- Query to compute total spend by location

### Visualizations
- Scatter Plot: Age vs. Purchase Amount segmented by gender
- Bar Chart: Top 10 locations based on total spending
- Pie Chart: Gender distribution of customers

---

## Dataset

**File:** `data/Shop.csv`  
**Columns include:**
- Customer ID
- Age
- Gender
- Location
- Purchase Amount (USD)
- Review Rating
- Discount Applied
- Previous Purchases

---

## Known Issues

### Table Display Glitch (YC Dataset Test)

When testing with the YC dataset (`data/yc-companies.csv`), long text entries like company descriptions caused layout issues:
- Table rows became misaligned
- Query results were harder to interpret

**Suggestions:**
- Implement automatic text wrapping in tables
- Use tooltips for long text fields
- Allow rows to dynamically adjust height

---

## Suggested Improvements

### 1. File Deletion Option

There is currently no feature to delete uploaded files (e.g., CSVs) directly from the app. This becomes problematic when switching between datasets or cleaning up test files.

**Proposal:**
- Add a file explorer interface with delete functionality
- Include confirmation prompts to avoid accidental deletions

## Author

Developed by Arihant (Ari)