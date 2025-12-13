import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


DB_PATH = r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore\superstore.db"
OUT_PATH = Path(r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore\images\top_unprofitable_customers.png")

sql = """
SELECT
  customer_id,
  customer_name,
  SUM(sales)  AS total_sales,
  SUM(profit) AS total_profit,
  COUNT(DISTINCT order_id) AS order_count
FROM orders_clean
GROUP BY customer_id, customer_name
HAVING SUM(profit) < 0
ORDER BY total_profit ASC
LIMIT 15;
"""

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql(sql, conn)

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="customer_name", y="total_profit")
plt.title("Top 15 Unprofitable Customers (Total Profit)")
plt.xlabel("Customer")
plt.ylabel("Total Profit (USD)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUT_PATH, dpi=200)
plt.show()
