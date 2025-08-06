# Day 6 : GroupBy & Aggregations

import pandas as pd

# 1. Load the Dataset
df = pd.read_csv('C:\\Aryan\\GitHub Repo\\pandas-learning-journey\\sales_records.csv')
print(f"\nInitial DataFrame:\n{df}")

# 2. Group by one column
print(df.groupby('Region')['Sales'].sum())

# 3. Group by multiple columns
print(df.groupby(['Region', 'Product'])['Sales'].sum())

# 4. Multiple Aggregations
print(df.groupby('Region').agg({
    'Sales' : ['sum', 'mean', 'max'],
    'Quantity' : ['sum', 'mean']
}))

# 5. Reset Index after GroupBy
grouped_df = df.groupby('Region')['Sales'].sum().reset_index()
print(grouped_df)


## PRACTICE TASKS (TODOs)

# TODO 1: Find total Quantity sold per Product
grouped_product = df.groupby('Product')['Quantity'].sum()
print(f"\nTotal Quantity sold per Product:\n{grouped_product}")

# TODO 2: Find average Sales per Region
grouped_region_avg = df.groupby('Region')['Sales'].mean()
print(f"\nAverage Sales per Region:\n{grouped_region_avg}")

# TODO 3: Find max and min Sales per Product
group_product_stats = df.groupby('Product')['Sales'].agg(['max', 'min'])
print(f"\nMax and Min Sales per Product:\n{group_product_stats}")

# TODO 4: Find total Sales and Quantity for each Region and Product combination
grouped_sales_quantity = df.groupby(['Region', 'Product']).agg({
    'Sales': 'sum',
    'Quantity': 'sum'
}).reset_index()
print(f"\nTotal Sales and Quantity for each Region and Product combination:\n{grouped_sales_quantity}")

# TODO 5: Reset index after grouping by Product and summing Sales
grouped_product_sales = df.groupby('Product')['Sales'].sum().reset_index()
print(f"\nGrouped Product Sales with reset index:\n{grouped_product_sales}")

# TODO 6: Save grouped results to 'datasets/grouped_sales.csv'
grouped_sales_quantity.to_csv('C:\\Aryan\\GitHub Repo\\pandas-learning-journey\\grouped_sales.csv', index=False)
print(f"\nGrouped sales data saved to 'grouped_sales.csv'")