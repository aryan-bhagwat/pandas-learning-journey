# Day 9 : Real Dataset & File I/O

import pandas as pd
import os

# 1. Reading CSV File

df_csv = pd.read_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\sales_data.csv')
print(f"DataFrame from CSV:\n{df_csv.head()}\n")

# 2. Reading Excel File
df_excel = pd.read_excel("C:\Aryan\GitHub Repo\pandas-learning-journey\sales_data.xlsx")
print(f"DataFrame from Excel:\n{df_excel.head()}\n")

# 3. Reading JSON File
df_json = pd.read_json("C:\Aryan\GitHub Repo\pandas-learning-journey\sales_data.json")
print(f"DataFrame from JSON:\n{df_json.head()}\n")

# 4. Writing to files

df_csv.to_csv("C:\Aryan\GitHub Repo\pandas-learning-journey\output_sales_data.csv", index=False)
df_excel.to_excel("C:\Aryan\GitHub Repo\pandas-learning-journey\output_sales_data.xlsx", index=False)
df_json.to_json("C:\Aryan\GitHub Repo\pandas-learning-journey\output_sales_data.json", orient='records')

# 5. Handline large files with chunks
chunk_size = 1000

for chunk in pd.read_csv("C:\Aryan\GitHub Repo\pandas-learning-journey\sales_data.csv", chunksize=chunk_size):
    print(f"Chunk of DataFrame:\n{chunk.shape}\n")

# 6. Check file size before loading

file_path = "C:\Aryan\GitHub Repo\pandas-learning-journey\sales_data.csv"
print(f"File Size: {os.path.getsize(file_path)/1024:.2f} KB")


## 1-9 Practice Tasks:

import pandas as pd
import os
import glob

# 1. Read the full CSV file and print its number of rows and columns
csv_path = 'datasets/sales_data.csv'
df_csv = pd.read_csv(csv_path)
print("Number of rows and columns in 'sales_data.csv':", df_csv.shape)

# 2. Read only selected columns: 'Date', 'Sales', and 'Region' to save memory and load time
df_selected = pd.read_csv(csv_path, usecols=['Date', 'Sales', 'Region'])

# 3. Read the Excel file (specifically Sheet1) and display the first 3 rows
df_excel = pd.read_excel('datasets/sales_data.xlsx', sheet_name='Sheet1')
print("Top 3 rows from 'sales_data.xlsx':\n", df_excel.head(3))

# 4. Read a JSON file formatted as a list of records and display column names and data types
df_json = pd.read_json('datasets/sales_data.json')
print("Schema (column names and dtypes) of 'sales_data.json':\n", df_json.dtypes)

# 5. Save the original CSV DataFrame to a new CSV file without including the index column
df_csv.to_csv('outputs/sales_output.csv', index=False)

# 6. Save the same DataFrame to a gzip-compressed CSV file for space efficiency
df_csv.to_csv('outputs/sales_output.csv.gz', index=False, compression='gzip')

# 7. Process a large CSV file in chunks of 500 rows, summing up the 'Sales' column incrementally
total_sales = 0
for chunk in pd.read_csv('datasets/large_sales.csv', chunksize=500):
    total_sales += chunk['Sales'].sum()
print("Total Sales computed from 'large_sales.csv':", total_sales)

# 8. While reading the CSV, parse the 'Date' column as datetime and use it as the DataFrame index
df_with_date_index = pd.read_csv(csv_path, parse_dates=['Date'], index_col='Date')

# 9. Specify data types explicitly to reduce memory usage (e.g., 'Sales' as float32, 'Region' as category)
dtypes = {'Sales': 'float32', 'Region': 'category'}
df_optimized = pd.read_csv(csv_path, dtype=dtypes)

# 10. Load only the first 1000 rows from the CSV to get a quick snapshot, then measure memory usage
df_1000 = pd.read_csv(csv_path, nrows=1000)
memory_usage = df_1000.memory_usage(deep=True).sum()
print("Memory usage of first 1000 rows in bytes:", memory_usage)

# 11. Combine all CSV files located in 'datasets/multi_csvs/' into one single DataFrame and save it
all_files = glob.glob('datasets/multi_csvs/*.csv')
df_list = [pd.read_csv(f) for f in all_files]
df_combined = pd.concat(df_list, ignore_index=True)
df_combined.to_csv('outputs/combined.csv', index=False)

# 12. Filter rows from the combined DataFrame where 'Sales' is greater than 1000, then save to CSV
df_high_sales = df_combined[df_combined['Sales'] > 1000]
df_high_sales.to_csv('outputs/high_sales.csv', index=False)

# 13. Export the full combined DataFrame and the high-sales subset to an Excel file with two sheets
with pd.ExcelWriter('outputs/sales_data_export.xlsx') as writer:
    df_combined.to_excel(writer, sheet_name='All_Data', index=False)
    df_high_sales.to_excel(writer, sheet_name='High_Sales', index=False)

# 14. Read the CSV again but treat specific strings as NaN (missing values), then count missing values per column
df_with_na = pd.read_csv(csv_path, na_values=['NA', 'N/A', 'null', ''])
missing_counts = df_with_na.isna().sum()
print("Missing values per column after treating specific strings as NaN:\n", missing_counts)

# 15. Take a random 5% sample of the original CSV data and save it as a new CSV file
df_sample = df_csv.sample(frac=0.05, random_state=42)
df_sample.to_csv('outputs/sample_5pct.csv', index=False)
