# Day 5 : Data Transformation - Sorting, Resetting Index & Column Operations

import pandas as pd

# 1. Load the Dataset
df = pd.read_csv('C:\\Aryan\\GitHub Repo\\pandas-learning-journey\\sales_data.csv')
print(f"\nInitial DataFrame:\n{df}")

# 2. Sorting
print(df.sort_values(by="Price"))

# Sort values by one column (Descending)
print(df.sort_values(by="Price", ascending = False))

# Sort by multiple columns
print(df.sort_values(by = ["Category", "Price"]))

# 3. Resetting Index
sorted_df = df.sort_values(by="Price").reset_index(drop=True)
print(f"\nDataFrame after sorting by Price and resetting index:\n{sorted_df}")

# 4. Column Operations

# Add New Column : Total = Price * Quantity
df['Total'] = df['Price'] *df['Quantity']
print(f"\nDataFrame after adding Total column:\n{df}")

# Modify Existing Column : Increase Price by 10%
df['Price'] = df['Price'] * 1.10
print(f"\nDataFrame after increasing Price by 10%:\n{df}")

# Drop a Column
df_dropped = df.drop(columns=['Total'])
print(f"\nDataFrame after dropping Total column:\n{df_dropped}")


## PRACTICE TASKS (TODOs)

# TODO 1: Sort products by Quantity (descending)
df_sorted_quantity = df.sort_values(by="Quantity", ascending = False)
print(f"\nDataFrame sorted by Quantity (descending):\n{df_sorted_quantity}")

# TODO 2: Sort by Category ascending, Quantity descending
df_sorted_category_quantity = df.sort_values(by=["Category", "Quantity"], ascending = [True, False])
print(f"\nDataFrame sorted by Category (ascending) and Quantity (descending):\n{df_sorted_category_quantity}")

# TODO 3: Reset index after sorting by Total_Sales (descending)
df_sorted_total_sales = df.sort_values(by="Total", ascending=False).reset_index(drop=True)
print(f"\nDataFrame sorted by Total Sales and reset index:\n{df_sorted_total_sales}")

# TODO 4: Add a new column 'Discounted_Price' (10% off from Price)
df['Discounted_Price'] = df['Price'] * 0.90
print(f"\nDataFrame after adding Discounted_Price column:\n{df}")

# TODO 5: Drop the 'Category' column
df_dropped_category = df.drop(columns=['Category'])
print(f"\nDataFrame after dropping Category column:\n{df_dropped_category}")

# TODO 6: Save sorted DataFrame to 'datasets/sorted_sales.csv'
df_sorted_quantity.to_csv('C:\\Aryan\\GitHub Repo\\pandas-learning-journey\\sorted_sales.csv', index=False)
print("\nSorted DataFrame saved to 'sorted_sales.csv'.")