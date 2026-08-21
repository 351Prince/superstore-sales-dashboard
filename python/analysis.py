import pandas as pd

# Load dataset
file_path = "data/superstore.csv"
df = pd.read_csv(file_path)

# =============================
# KEY KPIs
# =============================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order.ID"].nunique()
total_customers = df["Customer.ID"].nunique()

profit_margin = (total_profit / total_sales) * 100
average_order_value = total_sales / total_orders

print("\n========== KEY KPIs ==========")
print(f"Total Sales        : ${total_sales:,.2f}")
print(f"Total Profit       : ${total_profit:,.2f}")
print(f"Total Orders       : {total_orders:,}")
print(f"Total Quantity     : {total_quantity:,}")
print(f"Total Customers    : {total_customers:,}")
print(f"Profit Margin      : {profit_margin:.2f}%")
print(f"Average Order Value: ${average_order_value:,.2f}")


# =============================
# REGION ANALYSIS
# =============================

region_analysis = (
    df.groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print("\n========== REGION ANALYSIS ==========")
print(region_analysis)

best_region = region_analysis["Sales"].idxmax()
best_region_sales = region_analysis.loc[best_region, "Sales"]
best_region_profit = region_analysis.loc[best_region, "Profit"]

print(f"\nBest Region: {best_region}")
print(f"Best Region Sales: ${best_region_sales:,.2f}")
print(f"Best Region Profit: ${best_region_profit:,.2f}")


# =============================
# CATEGORY ANALYSIS
# =============================

category_analysis = (
    df.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print("\n========== CATEGORY ANALYSIS ==========")
print(category_analysis)

best_category = category_analysis["Sales"].idxmax()
best_category_sales = category_analysis.loc[best_category, "Sales"]
best_category_profit = category_analysis.loc[best_category, "Profit"]

print(f"\nBest Category: {best_category}")
print(f"Best Category Sales: ${best_category_sales:,.2f}")
print(f"Best Category Profit: ${best_category_profit:,.2f}")


# =============================
# SUB-CATEGORY ANALYSIS
# =============================

subcategory_analysis = (
    df.groupby("Sub.Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Profit", ascending=False)
)

print("\n========== SUB-CATEGORY ANALYSIS ==========")
print(subcategory_analysis)

best_subcategory = subcategory_analysis["Profit"].idxmax()
worst_subcategory = subcategory_analysis["Profit"].idxmin()

print(f"\nMost Profitable Sub-Category: {best_subcategory}")
print(
    f"Profit: ${subcategory_analysis.loc[best_subcategory, 'Profit']:,.2f}"
)

print(f"\nLeast Profitable Sub-Category: {worst_subcategory}")
print(
    f"Profit: ${subcategory_analysis.loc[worst_subcategory, 'Profit']:,.2f}"
)


# =============================
# SEGMENT ANALYSIS
# =============================

segment_analysis = (
    df.groupby("Segment")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print("\n========== SEGMENT ANALYSIS ==========")
print(segment_analysis)

best_segment = segment_analysis["Sales"].idxmax()

print(f"\nBest Customer Segment: {best_segment}")
print(
    f"Best Segment Sales: ${segment_analysis.loc[best_segment, 'Sales']:,.2f}"
)


# =============================
# PRODUCT ANALYSIS
# =============================

product_analysis = (
    df.groupby("Product.Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

print("\n========== TOP 5 PRODUCTS BY SALES ==========")
print(
    product_analysis
    .sort_values("Sales", ascending=False)
    .head(5)
)

print("\n========== TOP 5 PRODUCTS BY PROFIT ==========")
print(
    product_analysis
    .sort_values("Profit", ascending=False)
    .head(5)
)

print("\n========== TOP 5 LOSS-MAKING PRODUCTS ==========")
print(
    product_analysis
    .sort_values("Profit")
    .head(5)
)


# =============================
# DISCOUNT ANALYSIS
# =============================

discount_analysis = (
    df.groupby("Discount")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_index()
)

print("\n========== DISCOUNT ANALYSIS ==========")
print(discount_analysis)


# =============================
# SHIPPING MODE ANALYSIS
# =============================

shipping_analysis = (
    df.groupby("Ship.Mode")
    .agg(
        Orders=("Order.ID", "nunique"),
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Orders", ascending=False)
)

print("\n========== SHIPPING MODE ANALYSIS ==========")
print(shipping_analysis)


# =============================
# MONTHLY TREND ANALYSIS
# =============================

df["Order.Date"] = pd.to_datetime(df["Order.Date"])

monthly_analysis = (
    df.groupby(df["Order.Date"].dt.to_period("M"))
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

print("\n========== MONTHLY SALES & PROFIT ==========")
print(monthly_analysis)


# =============================
# SAVE BUSINESS SUMMARY
# =============================

summary = {
    "Total Sales": total_sales,
    "Total Profit": total_profit,
    "Total Orders": total_orders,
    "Total Quantity": total_quantity,
    "Total Customers": total_customers,
    "Profit Margin (%)": profit_margin,
    "Average Order Value": average_order_value,
    "Best Region": best_region,
    "Best Category": best_category,
    "Best Sub-Category": best_subcategory,
    "Worst Sub-Category": worst_subcategory,
    "Best Segment": best_segment
}

summary_df = pd.DataFrame([summary])

summary_df.to_csv(
    "report/business_summary.csv",
    index=False
)

print("\n========================================")
print("Analysis completed successfully!")
print("Summary saved to:")
print("report/business_summary.csv")
print("========================================")