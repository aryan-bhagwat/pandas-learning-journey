# # Day 8 – Time Series in Pandas

import pandas as pd

# # Sample data

# data = {
#     'Date': ['2025-02-08', '2025-07-30', '2025-07-26', '2025-10-19', '2025-12-15'],
#     'Sales': [200, 220, 250, 275, 300],
# }

# df = pd.DataFrame(data)

# # 1. Covert Date Column to Datetime
# df['Date'] = pd.to_datetime(df['Date'])
# print(f"DataFrame with Date Column as Datetime:\n{df}\n")

# # 2. Extract Year, Month, Day, Weekday
# df['Year'] = df['Date'].dt.year
# df['Month'] =df['Date'].dt.month
# df['Day'] = df['Date'].dt.day
# df['Weekday'] = df['Date'].dt.day_name()
# print(f"DataFrame with Year, Month, Day, and Weekday:\n{df}\n")

# # 3. Set Date as Index
# df.set_index('Date', inplace = True)
# print(f"DataFrame with Date as Index:\n{df}\n")

# # 4. Filter data for February 2025
# feb_data = df.loc["2025-02"]
# print(f"Data for February 2025:\n{feb_data}\n")

# # 5. Resample Montly and get total Sales
# montly_sales = df['Sales'].resample('M').sum()
# print(f"Monthly Sales:\n{montly_sales}\n")

# print(f"Full Details:\n{df}\n")
# print(f"February Sales Details:\n{feb_data}\n")
# print(f"Monthly Sales Details:\n{montly_sales}\n")


##  Practice Tasks

# Create a DataFrame with 10 dates in 2025 and random sales data.
sales_data = {
    'Date' : ['2025-01-01', '2025-02-01', '2025-03-01', '2025-06-16', '2025-05-01', '2025-06-01', '2025-07-01', '2025-08-01', '2025-09-01', '2025-10-01'],
    'Sales': [150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
}

sales_df = pd.DataFrame(sales_data)
print(f"Sales DataFrame:\n{sales_df}\n")

# Convert the date column to datetime and set it as the index.
sales_df['Date'] = pd.to_datetime(sales_df['Date'])
sales_df.set_index('Date', inplace = True)
print(f"Sales DataFrame with Date as Index:\n{sales_df}\n")

# Extract year, month, and weekday names into new columns.
sales_df['Year'] = sales_df.index.year
sales_df['Month'] = sales_df.index.month
sales_df['Weekday'] = sales_df.index.day_name()
print(f"Sales DataFrame with Year, Month, and Weekday:\n{sales_df}\n")

# Filter sales for a specific month of your choice.
june_sales = sales_df.loc['2025-06']
print(f"Sales Data for June 2025:\n{june_sales}\n")

# Resample the data:

#   1. Total sales per month
monthly_sales = sales_df['Sales'].resample('M').sum()
print(f"Monthly Sales:\n{monthly_sales}\n")

#   2. Average sales per week
weekly_sales = sales_df['Sales'].resample('W').mean()
print(f"Weekly Sales:\n{weekly_sales}\n")