import sqlite3
import pandas as pd

DB_PATH = r"C:\Users\Mahsa\Mahsa_Farnia\bootcamp\my_projects\1.E-commerce_superstore/superstore.db"
VIEW_NAME = "orders_clean"

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql(f"PRAGMA table_info('{VIEW_NAME}');", conn)

print(df[["name", "type"]])
