# Day 7 : Merging & Joining

import pandas as pd

# 1. Load the dataset

customers = pd.read_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\customers.csv')
orders = pd.read_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\orders.csv')

print(f"Cutomers :\n{customers}\n")
print(f"Orders :\n{orders}\n")

# 2. Inner Join

inner_join = pd.merge(customers, orders, on = 'CustomerID', how = 'inner')
print(f"Inner Join:\n{inner_join}\n")

# 3. Left Join

left_join = pd.merge(customers, orders, on = 'CustomerID', how = 'left')
print(f"Left Join:\n{left_join}\n")

# 4. Right Join

right_join = pd.merge(customers, orders, on = 'CustomerID', how = 'right')
print(f"Right Join:\n{right_join}\n")

# 5. Outer Join 

outer_join = pd.merge(customers, orders, on = 'CustomerID', how = 'outer')
print(f"Outer Join:\n{outer_join}\n")

# 6. Joining on Different Column Names

# Suppose 'orders.csv' had column 'Cust_ID' instead of 'CustomerID':
# pd.merge(customers, orders, left_on="CustomerID", right_on="Cust_ID")


## PRACTICE TASKS (TODOs)

# TODO 1: Create an inner join between orders and customers showing only Name and Product
order_customer_inner = pd.merge(customers[['CustomerID', 'Name']], orders[['CustomerID', 'Product']], on = 'CustomerID', how = 'inner')
print(f"Inner Join with Name and Product:\n{order_customer_inner}\n")

# TODO 2: Perform a left join but fill NaN values in Product with "No Order"
no_order_left = pd.merge(customers, orders, on = 'CustomerID', how = 'left').fillna({'Product': 'No Order', 'OrderID' : 'No Order', 'Amount': 0})
print(f"Left Join with NaN filled:\n{no_order_left}\n")

# TODO 3: Find total amount spent by each customer using groupby after merging
total_amount = pd.merge(customers, orders, on='CustomerID', how='inner').groupby('CustomerID')['Amount'].sum().reset_index()
print(f"Total Amount Spent by Each Customer:\n{total_amount}\n")

# TODO 4: Perform an outer join and sort by CustomerID
outer_sorted = pd.merge(customers, orders, on = 'CustomerID', how = 'outer').sort_values(by = 'CustomerID')
print(f"Outer Join Sorted by CustomerID:\n{outer_sorted}\n")

# TODO 5: Save left join result to 'datasets/customers_orders_left.csv'
left_join.to_csv('C:\\Aryan\\GitHub Repo\\pandas-learning-journey\\customers_orders_left.csv', index=False)