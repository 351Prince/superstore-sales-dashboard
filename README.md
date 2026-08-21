# 📊 Superstore Sales Analytics Dashboard

An end-to-end **E-Commerce Sales Analytics project** built to analyze sales performance, profitability, customer behavior, product performance, regional trends, and the impact of discounts.

The project combines **Python, SQL, MySQL, and Power BI** to transform raw Superstore data into actionable business insights.

---

## 🚀 Project Overview

This project focuses on analyzing an E-Commerce Superstore dataset to answer important business questions such as:

* Which regions generate the highest sales and profit?
* Which categories and sub-categories perform best?
* Which products generate losses?
* How do discounts affect profitability?
* Which customer segments contribute the most revenue?
* How do sales and profit change over time?
* Which shipping modes are most frequently used?

The analysis was performed using **Python and SQL**, while **Power BI** was used to create an interactive business intelligence dashboard.

---

## 🛠️ Tech Stack

| Technology   | Purpose                                 |
| ------------ | --------------------------------------- |
| Python       | Data analysis and preprocessing         |
| Pandas       | Data cleaning and manipulation          |
| SQL          | Business analysis and querying          |
| MySQL        | Data storage and SQL analysis           |
| Power BI     | Interactive dashboard and visualization |
| DAX          | KPI calculations and measures           |
| Git & GitHub | Version control and project management  |

---

## 📈 Power BI Dashboard

The Power BI dashboard provides an interactive view of:

* Sales performance
* Profitability
* Regional performance
* Category & sub-category analysis
* Customer segmentation
* Product performance
* Discount analysis
* Monthly sales and profit trends
* Shipping mode performance

### Dashboard Overview

![Dashboard Overview](screenshots/dashboard_overview.png)

### Sales Analysis

![Sales Analysis](screenshots/sales_analysis.png)

### Profit Analysis

![Profit Analysis](screenshots/profit_analysis.png)

---

## 🔍 Key Business Analysis

### 📍 Regional Analysis

Analyzed sales and profit performance across different regions to identify high-performing and underperforming markets.

### 🛍️ Category & Sub-Category Analysis

Compared sales, profit, and quantity across product categories and sub-categories.

### 📦 Product Analysis

Identified top-performing products based on sales and analyzed products generating negative profit.

### 💰 Discount Analysis

Analyzed the relationship between discount levels, sales, and profitability to identify potentially unprofitable discount strategies.

### 👥 Customer Analysis

Analyzed customer-level sales and profit contribution to identify high-value customers.

### 📅 Time-Series Analysis

Analyzed monthly sales, profit, and quantity trends to understand business performance over time.

### 🚚 Shipping Analysis

Compared different shipping modes based on order volume, sales, and profitability.

### 👤 Segment Analysis

Compared Consumer, Corporate, and Home Office segments based on customers, sales, profit, and quantity.

---

## 🗄️ SQL Analysis

SQL was used to perform business-focused analysis including:

* Regional sales & profit analysis
* Category performance
* Top-selling products
* Loss-making products
* Discount impact
* Monthly sales trends
* Shipping mode analysis
* Customer segment analysis
* Customer performance
* Sub-category performance

### Example SQL Query

```sql
SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;
```

---

## 🐍 Python Analysis

Python and Pandas were used for:

* Data cleaning and preprocessing
* Data validation and quality checks
* Exploratory data analysis
* KPI calculation
* Sales and profit analysis
* Trend analysis
* Business insight generation

Python helped prepare and analyze the dataset before building the Power BI dashboard.

---

## 📊 Key KPIs

The Power BI dashboard tracks important business KPIs including:

* Total Sales
* Total Profit
* Total Orders
* Total Quantity
* Average Order Value
* Profit Margin
* Sales by Region
* Sales by Category
* Sales by Segment

---

## 💡 Business Insights

The analysis helps identify:

* High-performing and underperforming regions
* Profitable and loss-making product categories
* Top-performing products
* The impact of discounts on profitability
* High-value customer segments
* Monthly sales and profit trends
* Shipping modes and their business impact

---

## 📁 Project Structure

```text
E-Commerce-Sales-Analytics/
│
├── data/
│   └── superstore.csv
│
├── python/
│   └── analysis.py
│
├── SQL/
│   └── ecommerce_analysis.sql
│
├── dashboard/
│   └── Superstore_Dashboard.pbix
│
├── screenshots/
│   ├── dashboard_overview.png
│   ├── sales_analysis.png
│   └── profit_analysis.png
│
└── README.md
```

---

## 🎯 Project Objective

The objective of this project is to demonstrate an end-to-end data analytics workflow, from raw data preparation and SQL-based analysis to interactive Power BI dashboard development.

The project demonstrates practical skills in **Python, SQL, MySQL, Power BI, DAX, data cleaning, data visualization, KPI development, and business analysis**.

---

## 👨‍💻 Author

**Prince Anand**

Data Analyst | Python | SQL | Power BI | Excel

GitHub: [351Prince](https://github.com/351Prince)
