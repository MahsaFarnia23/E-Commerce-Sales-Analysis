import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DB_PATH = r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore\superstore.db"
OUT_PATH = Path(r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore\images\profitable_customers_profit.png")

sql = """
SELECT
  customer_id,
  customer_name,
  SUM(profit) AS total_profit
FROM orders_clean
GROUP BY customer_id, customer_name
ORDER BY total_profit DESC;
"""

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql(sql, conn)

#customers with high profit
df = df[df["total_profit"] > 0].copy()

df["cum_profit"] = df["total_profit"].cumsum()
df["cum_profit_pct"] = 100 * df["cum_profit"] / df["total_profit"].sum()
df["rank"] = range(1, len(df) + 1)

plt.figure(figsize=(12, 6))

# Bar: profit
plt.bar(df["rank"], df["total_profit"])
# Line: cumulative %
plt.plot(df["rank"], df["cum_profit_pct"], marker="o")

plt.axhline(80, linestyle="--")
plt.title("Pareto Analysis (80/20): Customer Contribution to Total Profit")
plt.xlabel("Customer Rank (sorted by profit)")
plt.ylabel("Profit / Cumulative Profit (%)")
plt.tight_layout()

OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUT_PATH, dpi=200)
plt.show()
