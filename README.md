# E-Commerce-Sales-Analysis

# Superstore Sales & Customer Profitability Analysis (SQLite + SQL Project)

A complete end-to-end SQL analytics project using the Superstore dataset.  
This project demonstrates practical skills in data cleaning, KPI analysis, customer segmentation, discount impact evaluation, and profitability insights.

---

# 📑 Table of Contents

1. [Project Overview](#project-overview)  
2. [Objectives](#objectives)  
3. [Data Preparation](#data-preparation)  
4. [Overall KPIs](#overall-kpis)  
5. [Yearly Performance](#yearly-performance)  
6. [Category Performance](#category-performance)  
7. [Monthly Sales & Profit Trend](#monthly-sales--profit-trend)  
8. [Regional Sales & Profit Analysis](#regional-sales--profit-analysis)  
9. [Top 10 Most Profitable Customers](#top-10-most-profitable-customers)  
10. [Unprofitable Customers Analysis](#unprofitable-customers-analysis)  
11. [Final Notes](#final-notes)

---

# 📘 Project Overview

This SQL project performs a complete analysis of the Superstore dataset using **SQLite**.  
It evaluates sales trends, category profitability, customer behavior, discount effects, and regional performance.

The project highlights real-world Data Analyst capabilities including:

- SQL-based data cleaning  
- KPI development  
- Trend & segmentation analysis  
- Insight generation for business decisions  

---

# 🎯 Objectives

- Analyze **sales trends** over time  
- Identify **profitable vs. low-profit categories**  
- Segment customers based on **profitability**  
- Measure the **impact of discounts**  
- Compare **regional performance**  

---

# 🛠 Data Preparation

### **1. Convert date columns into ISO format (`YYYY-MM-DD`)**

The dataset originally contained dates in inconsistent formats (e.g., `11/8/2016`).  
They were transformed into standard ISO format using string functions so SQLite could process them correctly.

### **2. Create a clean view for analysis**

```sql
CREATE VIEW orders_clean AS
SELECT
    *,
    printf('%04d-%02d-%02d', year, month, day) AS order_date,
    strftime('%Y', order_date) AS order_year,
    strftime('%m', order_date) AS order_month
FROM "Sample - Superstore";
