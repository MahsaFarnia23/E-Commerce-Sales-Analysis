import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DB_PATH = r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore\superstore.db"
OUT_PATH = Path(r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore\images") / "regional_sales.png"

sql = """
SELECT
  region,
  COUNT(DISTINCT order_id) AS total_orders,
  SUM(sales)  AS total_sales,
  SUM(profit) AS total_profit
FROM orders_clean
GROUP BY region
ORDER BY total_sales DESC;
"""

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql(sql, conn)

plt.figure(figsize=(9, 5))
sns.barplot(data=df, x="region", y="total_sales")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales (USD)")
plt.tight_layout()
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUT_PATH, dpi=200)
plt.show()
