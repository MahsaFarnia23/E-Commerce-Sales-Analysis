# SQL Queries Documentation

This folder contains all SQL scripts used in the **E-Commerce Sales & Profit Analysis** project.  
Each file focuses on a specific analytical goal such as data cleaning, KPI generation, customer segmentation, and trend analysis.

Click on any script below to open the corresponding SQL file.

---

## 📌 Queries Overview

### 1. [cleaning.sql](./E-Commerce-Sales-Analysis/queries/cleaning.sqbpro)
Prepares the dataset for analysis by converting date formats, standardizing fields, and creating the `orders_clean` view used in all downstream queries.

### 2. [kpis.sql](./queries/overall_KPIs.sqbpro) 
Computes the main business KPIs including total sales, total profit, order count, and profit margins.

### 3. [yearly_performance.sql](./queries/Sale_yearly.sqbpro)  
Aggregates sales and profit by year to evaluate overall business performance over time.

### 4. [category_performance.sql](./queries/sale_category.sqbpro)
Analyzes revenue and profitability across major product categories such as Technology, Furniture, and Office Supplies.

### 5. [monthly_trend.sql](./queries/monthly_trend.sqbpro)
Generates month-level sales and profit metrics to identify seasonal patterns and monthly trends.

### 6. [regional_analysis.sql](./queries/regional_analysis.sql)
Compares regions by total orders, sales, profit, discount levels, and margin percentage.

### 7. [top_customers.sql](./queries/top_customers.sqbpro)
Identifies the top 10 most profitable customers using aggregated sales and profit metrics.

### 8. [unprofitable_customers.sql](./queries/unprofitable_customers.sqbpro)
Finds all customers with negative total profit and highlights margin erosion patterns.

---

## 📘 How to Use These Queries

1. Load the dataset into SQLite or DB Browser for SQLite.  
2. Run **`cleaning.sqbpro` first** to generate the `orders_clean` view.  
3. After that, each SQL script can be executed independently.  
4. The scripts are ordered logically from preparation → KPI generation → trend analysis → customer segmentation.

---

## 📎 Notes

- All queries are modular and do not overwrite each other.  
- The project follows a clear analytical flow: *clean → aggregate → analyze → segment → interpret*.  
- For insights and interpretation of results, refer to the main project `README.md` in the root directory.

---

