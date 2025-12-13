import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DB_PATH = r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore\superstore.db"
OUT_PATH = Path(
    r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore\images\top_customers_profit.png"
)

sql = """
SELECT
    customer_name,
    SUM(profit) AS total_profit
FROM orders_clean
GROUP BY customer_id, customer_name
HAVING total_profit > 0
ORDER BY total_profit DESC
LIMIT 10;
"""

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql(sql, conn)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=df,
    x="total_profit",
    y="customer_name",
    orient="h"
)

plt.title("Top 10 Most Profitable Customers")
plt.xlabel("Total Profit (USD)")
plt.ylabel("Customer")
plt.tight_layout()

OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUT_PATH, dpi=200)
plt.show()
