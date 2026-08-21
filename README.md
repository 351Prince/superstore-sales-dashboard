# 📊 Superstore Sales Analytics Dashboard

An end-to-end **E-Commerce Sales Analytics project** built to analyze sales performance, profitability, customer behavior, product performance, regional trends, and the impact of discounts.

The project combines **Python, SQL, MySQL, and Power BI** to transform raw Superstore data into actionable business insights.

---

## 🚀 Project Overview

This project analyzes an E-Commerce Superstore dataset to answer key business questions:

* Which regions generate the highest sales and profit?
* Which categories and sub-categories perform best?
* Which products generate losses?
* How do discounts affect profitability?
* Which customer segments contribute the most revenue?
* How do sales and profit change over time?
* Which shipping modes are most frequently used?

**Python and SQL** were used for data preparation and analysis, while **Power BI** was used to build an interactive business intelligence dashboard.

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
* Category and sub-category analysis
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

Analyzed sales and profit performance across regions to identify high-performing and underperforming markets.

### 🛍️ Category & Sub-Category Analysis

Compared sales, profit, and quantity across product categories and sub-categories to identify strong and weak product areas.

### 📦 Product Analysis

Identified top-performing products based on sales and analyzed products generating negative profit.

### 💰 Discount Analysis

Analyzed the relationship between discount levels, sales, and profitability to identify potentially unprofitable discount strategies.

### 👥 Customer Analysis

Analyzed customer-level sales and profit contribution to identify high-value customers.

### 📅 Time-Series Analysis

Analyzed monthly sales, profit, and quantity trends to understand business performance over time.

### 🚚 Shipping Analysis

Compared shipping modes based on order volume, sales, and profitability.

### 👤 Segment Analysis

Compared Consumer, Corporate, and Home Office segments based on customers, sales, profit, and quantity.

---

## 🗄️ SQL Analysis

SQL was used to perform business-focused analysis including:

* Regional sales and profit analysis
* Category and sub-category performance
* Top-selling products
* Loss-making products
* Discount impact analysis
* Monthly sales trends
* Shipping mode analysis
* Customer segment analysis
* Customer performance
* Regional profitability

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

### SQL Concepts Used

* SELECT
* WHERE
* GROUP BY
* HAVING
* ORDER BY
* Aggregate Functions
* CASE Statements
* Subqueries
* Date Functions
* JOINs

---

## 🐍 Python Analysis

Python and Pandas were used for:

* Data cleaning and preprocessing
* Data validation
* Missing-value analysis
* Exploratory data analysis
* KPI calculations
* Sales and profit analysis
* Trend analysis
* Business insight generation

Python was used to prepare and analyze the dataset before visualization in Power BI.

---

## 📊 Key KPIs

The Power BI dashboard tracks important business KPIs including:

* **Total Sales**
* **Total Profit**
* **Total Orders**
* **Total Quantity**
* **Average Order Value**
* **Profit Margin**
* **Sales by Region**
* **Sales by Category**
* **Sales by Segment**

---

## 💡 Business Insights

The analysis helps identify:

* High-performing and underperforming regions
* Profitable and loss-making product categories
* Top-performing and loss-making products
* The relationship between discounts and profitability
* High-value customer segments
* Monthly sales and profit trends
* Shipping modes with different business impacts

> **Note:** Specific numerical insights can be added here based on the final Power BI analysis.

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

The objective of this project is to demonstrate an **end-to-end data analytics workflow**, from raw data preparation and SQL-based analysis to interactive Power BI dashboard development.

The project demonstrates practical skills in:

**Python • Pandas • SQL • MySQL • Power BI • DAX • Data Cleaning • Data Visualization • KPI Development • Business Analysis**

---

## 📌 Skills Demonstrated

* Data Cleaning & Preprocessing
* Exploratory Data Analysis
* SQL Business Analysis
* MySQL
* Power BI Dashboard Development
* DAX Measures
* KPI Development
* Data Visualization
* Business Intelligence
* Git & GitHub

---

## 👨‍💻 Author

**Prince Anand**

**Data Analyst | Python | SQL | Power BI | Excel**

* GitHub: [351Prince](https://github.com/351Prince)
* LinkedIn: [Prince Anand](https://www.linkedin.com/in/prince-anand-b32414258/)

---

⭐ If you found this project useful, feel free to star the repository.
