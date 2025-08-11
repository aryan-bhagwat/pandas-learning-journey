# 🐼 Pandas Learning Journey

This repository contains daily Pandas practice exercises following a structured 10-day roadmap for fast and practical mastery.

---

## 📅 Day 1 - Series and DataFrame Basics

### Topics Covered:
- Introduction to Pandas
- Creating a `Series` from a list
- Creating a `DataFrame` from:
  - A dictionary
  - A list of dictionaries

### 📂 Files:
- `day01_series_dataframe.py` - Practice script for Series and DataFrame creation

### ✅ Tasks Performed:
- Created a Series of daily expenses
- Created a DataFrame using subject marks
- Created a DataFrame using friends’ names and ages

---

## 📅 Day 2 - Data Inspection & Basic Operations

### Topics Covered:
- Viewing top and bottom rows of data
- Getting column names, shape, and data types
- Summarizing with `.info()` and `.describe()`
- Renaming columns

### 📂 Files:
- `day02_inspection_basics.py` - Day 2 practice script
- `datasets/daily_expenses.csv` - Sample CSV file

### ✅ Tasks Performed:
- Loaded data from CSV
- Printed top and bottom rows
- Inspected structure, columns, and datatypes
- Renamed columns
- Displayed summary statistics

---

# 📅 Day 3 - Indexing, Selection & Filtering

### 📘 Topics Covered:
- Selecting columns using `[]`
- Row selection with `.loc[]` and `.iloc[]`
- Filtering rows with conditions
- Combining multiple conditions

---

### 📂 Files:
- `day03_selection_filtering.py` – Practice file with examples and TODOs
- `datasets/daily_expenses.csv` – Sample data used for filtering

---

### ✅ Tasks Performed:
- Loaded CSV and selected specific columns
- Retrieved rows using `.iloc[]` and `.loc[]`
- Filtered rows using logical conditions
- Practiced combining conditions using `&`, `|`, and `~`
- Added a new column based on condition
- Exported filtered results to a new CSV file

---

### 🧪 Practice Set (TODOs):
- Extract column(s) using different methods
- Use `.loc` and `.iloc` to retrieve specific rows
- Apply filters using comparison operators
- Combine conditions with AND / OR
- Create a new column based on logic
- Save filtered data to a new CSV

---

### 💡 Learnings:
This day focused on accessing and filtering data using Pandas core indexing tools and logic, essential for exploring real-world datasets effectively.


# 📅 Day 4 - Data Cleaning: Handling Missing Values & Duplicates

### 📘 Topics Covered:
- Identifying missing values using `isnull()`
- Dropping missing values with `dropna()`
- Filling missing values with `fillna()`
- Removing duplicate rows using `drop_duplicates()`

---

### 📂 Files:
- `day04_data_cleaning.py` – Practice file with examples and TODOs
- `datasets/dirty_data.csv` – Sample dataset with missing values and duplicates

---

### ✅ Tasks Performed:
- Detected missing data per column
- Dropped and filled missing values with statistical values
- Identified and removed duplicate rows
- Exported cleaned data to new CSV files

---

### 🧪 Practice Set (TODOs):
- Print and count missing rows
- Apply various fill strategies (mean, median, fixed value)
- Drop rows vs. fill values: choose appropriately
- Remove duplicates from the dataset
- Export cleaned and de-duplicated datasets

---

### 💡 Learnings:
Cleaning messy data is one of the most frequent and important tasks in data analysis. Mastering these operations builds a strong foundation for data preprocessing and analysis.


# 📅 Day 5 - Sorting, Resetting Index & Column Operations

### 📘 Topics Covered:
- Sorting by one or multiple columns
- Ascending vs. descending order
- Resetting index after sorting
- Adding, modifying, and deleting columns

---

### 📂 Files:
- `day05_sorting_columns.py` – Practice file with examples and TODOs
- `datasets/sales_data.csv` – Sample dataset for sorting & column operations

---

### ✅ Tasks Performed:
- Sorted by single and multiple columns
- Reset index after sorting
- Created new calculated columns
- Modified column values
- Dropped columns from DataFrame

---

### 🧪 Practice Set (TODOs):
- Sort data based on different columns and orders
- Create new columns from existing data
- Modify existing column values
- Drop unnecessary columns
- Save sorted results to CSV

---

### 💡 Learnings:
Sorting and managing columns help in organizing data for analysis and presentation. Resetting the index keeps the DataFrame tidy after reordering.


# 📅 Day 6 - GroupBy & Aggregations

### 📘 Topics Covered:
- Grouping data by one or multiple columns
- Aggregating data using sum, mean, max, min
- Applying multiple aggregations to different columns
- Resetting index after groupby

---

### 📂 Files:
- `day06_groupby_aggregations.py` – Practice file with examples and TODOs
- `datasets/sales_records.csv` – Sample dataset for groupby & aggregation

---

### ✅ Tasks Performed:
- Grouped sales data by Region and Product
- Calculated totals, averages, and maximums
- Applied multiple aggregations
- Reset index for cleaner grouped DataFrames

---

### 🧪 Practice Set (TODOs):
- Find total quantity per product
- Find average sales per region
- Find min and max sales per product
- Group by multiple columns and calculate total sales and quantities
- Save grouped results to CSV

---

### 💡 Learnings:
GroupBy is one of Pandas' most powerful tools, enabling summarization and aggregation of large datasets efficiently.


# 📅 Day 7 - Merging & Joining DataFrames

### 📘 Topics Covered:
- Inner, Left, Right, Outer joins in Pandas
- Merging on one column or different column names
- Combining datasets for analysis

---

### 📂 Files:
- `day07_merging_joining.py` – Example code + practice tasks
- `datasets/customers.csv` – Customers data
- `datasets/orders.csv` – Orders data

---

### ✅ Tasks Performed:
- Merged datasets with different join types
- Practiced merging on the same and different column names
- Learned to combine datasets similar to SQL joins

---

### 🧪 Practice Set (TODOs):
- Merge and select specific columns
- Fill missing values after join
- Group and calculate aggregated results
- Save merged outputs

---

### 💡 Learnings:
Merging and joining helps combine related datasets into a single table, enabling more powerful data analysis.


## 📅 Day 8 - Time Series in Pandas

### Topics Covered:
- Converting strings to datetime
- Extracting year, month, day, weekday
- Setting datetime as index
- Filtering by date range
- Resampling (monthly, weekly, yearly)

### 📂 Files:
- `day08_time_series.py` - Day 8 practice script
- `datasets/sales_timeseries.csv` - Sample dataset

### ✅ Tasks Performed:
- Converted date column to datetime
- Extracted year, month, weekday
- Set date as index
- Filtered specific months
- Resampled sales data by month and week


## 📅 Day 9 - Real Dataset & File I/O

### Topics Covered:
- Reading from different file formats (`CSV`, `Excel`, `JSON`)
- Writing DataFrames to files (`to_csv`, `to_excel`, `to_json`)
- Handling large files with `chunksize`
- Basic file exploration before loading
- Using `os` module to check file details

### 📂 Files:
- `day09_file_io.py` - Day 9 practice script
- `datasets/sales_data.csv` - Sample CSV file
- `datasets/sales_data.xlsx` - Sample Excel file
- `datasets/sales_data.json` - Sample JSON file

### ✅ Tasks Performed:
- Loaded data from CSV, Excel, JSON
- Saved DataFrames to CSV, Excel, JSON
- Processed large CSV files in chunks
- Checked file size before loading


## 🧠 Daily Progress Tracker
| Day | Topic                             | Status  |
|-----|-----------------------------------|---------|
| 1   | Series & DataFrames               | ✅ Done |
| 2   | Data Inspection & Basics          | ✅ Done |
| 3   | Indexing & Filtering              | ✅ Done |
| 4   | Data Cleaning                     | ✅ Done |
| 5   | Data Transformation               | ✅ Done |
| 6   | Grouping & Aggregation            | ✅ Done |
| 7   | Merging, Concatenation, Sorting   | ✅ Done |
| 8   | Time Series                       | ✅ Done |
| 9   | Real Dataset & File I/O           | ✅ Done |
| 10  | Mini Projects                     | ⏳ Pending |

---

## 📌 Note
All code is written in beginner-friendly style and explained using comments.
