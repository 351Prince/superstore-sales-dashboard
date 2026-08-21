import pandas as pd

file_path = r"C:\Users\hp\Desktop\E-Commerce-Sales-Analytics\data\superstore.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Rows and Columns:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- SUMMARY STATISTICS ---")
print(df.describe())

print("\n--- TOTAL SALES ---")
print(df["Sales"].sum())

print("\n--- TOTAL PROFIT ---")
print(df["Profit"].sum())

print("\n--- TOTAL QUANTITY ---")
print(df["Quantity"].sum())

print("\n--- TOTAL ORDERS ---")
print(df["Order.ID"].nunique())

print("\n--- TOTAL CUSTOMERS ---")
print(df["Customer.ID"].nunique())

print("\n--- SALES BY CATEGORY ---")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

print("\n--- PROFIT BY CATEGORY ---")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

print("\n--- SALES BY REGION ---")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

print("\n--- PROFIT BY REGION ---")
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))

# Convert date columns
df["Order.Date"] = pd.to_datetime(df["Order.Date"])

# Create Year-Month column
df["Year-Month"] = df["Order.Date"].dt.to_period("M").astype(str)

# Monthly Sales and Profit
monthly = df.groupby("Year-Month").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).reset_index()

print("\n--- MONTHLY SALES & PROFIT ---")
print(monthly.to_string(index=False))

# Best sales month
best_sales_month = monthly.loc[monthly["Sales"].idxmax()]

print("\n--- BEST SALES MONTH ---")
print(best_sales_month)

# Best profit month
best_profit_month = monthly.loc[monthly["Profit"].idxmax()]

print("\n--- BEST PROFIT MONTH ---")
print(best_profit_month)
# Top 10 products by sales
top_products_sales = (
    df.groupby("Product.Name")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Sales", ascending=False)
      .head(10)
)

print("\n--- TOP 10 PRODUCTS BY SALES ---")
print(top_products_sales)

# Top 10 products by profit
top_products_profit = (
    df.groupby("Product.Name")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Profit", ascending=False)
      .head(10)
)

print("\n--- TOP 10 PRODUCTS BY PROFIT ---")
print(top_products_profit)

# Loss-making products
loss_products = (
    df.groupby("Product.Name")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .query("Profit < 0")
      .sort_values("Profit")
)

print("\n--- LOSS-MAKING PRODUCTS ---")
print(loss_products.head(10))
# Discount vs Profit Analysis

discount_analysis = (
    df.groupby("Discount")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .reset_index()
      .sort_values("Discount")
)

print("\n--- DISCOUNT VS PROFIT ---")
print(discount_analysis)

# Average profit by discount
avg_profit_discount = (
    df.groupby("Discount")["Profit"]
      .mean()
      .reset_index()
      .sort_values("Discount")
)

print("\n--- AVERAGE PROFIT BY DISCOUNT ---")
print(avg_profit_discount)