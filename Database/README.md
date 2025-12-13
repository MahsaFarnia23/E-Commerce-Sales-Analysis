## **📥 Dataset Acquisition & Preparation**

The dataset used in this project was originally downloaded from **Kaggle** as a **CSV file**. After downloading, the file was imported into **SQLite** to enable structured SQL analysis.
* **Name**: `Sample - Superstore.csv`  
* **Source**: [Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download)  
* **Content**: 
            * **Order details** (order ID, order date, ship date, shipping mode) 
            * **Customer information** (customer ID, customer name, customer segment)
            * **Geographical data** (country, region, state, city, postal code)
            * **Product details** (product ID, product name, category, sub-category)
            * **Sales and profitability metrics** (sales amount, quantity, discount, profit)

Each row in the CSV file represents a **single product-level transaction within an order**, allowing for detailed analysis of sales performance, customer behavior, and profitability drivers.

This raw CSV file was later imported into **SQLite** and transformed into a clean, query-ready format for SQL-based analysis.
   
### **Steps**

1. **Downloaded the Superstore Sales dataset from Kaggle** in CSV format.
2. **Imported the CSV into SQLite** using the built-in import tools.
3. **Saved the imported table** as a clean and query-ready database file for further analysis.




