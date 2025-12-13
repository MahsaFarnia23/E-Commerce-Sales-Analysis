import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DB_PATH = r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore\superstore.db"
OUT_PATH = Path(r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore\images\yearly_sales_profit.png")

sql = """
SELECT
  order_year AS year,
  SUM(sales)  AS total_sales,
  SUM(profit) AS total_profit
FROM orders_clean
GROUP BY order_year
ORDER BY order_year;
"""

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql(sql, conn)

## Convert to long format for two-variable bar chart
df_long = df.melt(id_vars=["year"], value_vars=["total_sales", "total_profit"],
                  var_name="metric", value_name="amount")

plt.figure(figsize=(10, 5))
sns.barplot(data=df_long, x="year", y="amount", hue="metric")
plt.title("Yearly Sales vs Profit")
plt.xlabel("Year")
plt.ylabel("Amount (USD)")
plt.tight_layout()
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUT_PATH, dpi=200)
plt.show()
