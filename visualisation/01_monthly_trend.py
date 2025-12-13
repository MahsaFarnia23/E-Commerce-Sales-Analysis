import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DB_PATH = r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore/superstore.db"
OUT_PATH = Path(r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore/images/monthly_trend.png")

sql = """
SELECT
  order_year,
  order_month,
  (order_year || '-' || order_month) AS year_month,
  SUM(sales)  AS monthly_sales,
  SUM(profit) AS monthly_profit
FROM orders_clean
GROUP BY order_year, order_month
ORDER BY order_year, order_month;
"""

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql(sql, conn)

# To display right on the x-axis
df["year_month"] = pd.to_datetime(df["year_month"] + "-01")

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="year_month", y="monthly_sales", label="Sales")
sns.lineplot(data=df, x="year_month", y="monthly_profit", label="Profit")

plt.title("Monthly Sales and Profit Trend")
plt.xlabel("Year-Month")
plt.ylabel("Amount (USD)")
plt.tight_layout()
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUT_PATH, dpi=200)
plt.show()
