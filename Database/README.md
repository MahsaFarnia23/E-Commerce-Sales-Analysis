## 📥 Dataset Acquisition & Preparation

The dataset used in this project was sourced from **Kaggle** and originally provided in **CSV format**.  
It was imported into **SQLite** to enable structured, SQL-based analysis.

### Dataset Details
- **File name:** `Sample - Superstore.csv`
- **Source:** [Superstore Dataset on Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download)
- **Dataset type:** Synthetic e-commerce / retail transactions
- **Number of rows:** 9,994 transaction records
- **Number of columns:** 21 attributes

> ⚠️ *Note:* This is a **synthetic dataset**, commonly used for analytics practice and portfolio projects.  
> While it does not represent real customer data, its structure closely resembles real-world retail transaction systems and is well-suited for business analytics and SQL demonstrations.

### Dataset Content
The CSV file contains detailed transactional records, including:

- **Order details:** order ID, order date, ship date, shipping mode  
- **Customer information:** customer ID, customer name, customer segment  
- **Geographical data:** country, region, state, city, postal code  
- **Product details:** product ID, product name, category, sub-category  
- **Sales & profitability metrics:** sales amount, quantity, discount, profit  

Each row represents a **single product-level transaction within an order**, enabling granular analysis of sales performance, customer behavior, discount impact, and profitability drivers.

### Preparation Steps
1. Downloaded the Superstore dataset from Kaggle in CSV format.  
2. Imported the CSV file into **SQLite** using built-in import tools.  
3. Saved the imported data as a structured, query-ready SQLite database for further analysis.
