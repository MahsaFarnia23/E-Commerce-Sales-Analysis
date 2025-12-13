# 📊 Data Visualizations

This folder contains Python scripts used to generate all visual insights for the project.
The visualizations are built on top of the cleaned SQLite view (`orders_clean`) and are designed to support the business insights derived from SQL analysis.

All charts are generated using **Pandas**, **Matplotlib**, and **Seaborn**, and the output images are saved in the `/images` directory at the root of the repository.

---

## 📁 Scripts Overview

| Script | Description |
|------|------------|
| `01_monthly_trend.py` | Monthly sales and profit trend over time |
| `02_yearly_trend.py` | Yearly comparison of total sales and profit |
| `03_regional_sales.py` | Total sales by region |
| `04_category_performance.py` | Sales vs profit by product category |
| `05_top_customers_profit.py` | Pareto (80/20) analysis of customer profitability |
| `06_unprofitable_customers.py` | Top unprofitable customers by total loss |

---

## 📂 Data Source

All visualization scripts connect directly to the SQLite database included in this repository:

- **Database:** `data/superstore.db`
- **View used:** `orders_clean`

The `orders_clean` view standardizes date formats and includes derived time attributes (year, month), ensuring consistent and reliable analysis across all charts.

---

## ▶️ How to Run

From the project root directory:

```bash
python visualizations/03_regional_sales.py

