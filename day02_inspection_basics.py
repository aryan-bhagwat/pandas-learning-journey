# Day 2 : Data Inspection & Basic Operations

import pandas as pd

# 1. Load the CSV file

df = pd.read_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\daily_expenses.csv')

# 2. View Top and Bottom Rows

print("Top 5 rows: ")
print(df.head())

print("\nBottom 5 rows: ")
print(df.tail())

# 3. Explore Structure

print("\nShape of DataFrame: ", df.shape)

print("Columns: ", df.columns.tolist())

print("Data types:\n", df.dtypes)

# 4. Info and Summary

print("\nInfo: ")
df.info()

print("\nSummary Statistics: ")
print(df.describe())

# 5. Rename Columns

df.rename(columns = {'Day': 'Weekday', 'Expenses': 'Daily_Expense'}, inplace = True)

print("\nUpdated Columns: ")
print(df.columns.tolist())

print("\nUpdated DataFrame: ")
print(df.head())


## Practice Tasks

# TODO 1 : Print only the column names
print("\nColumns: ", df.columns.tolist())

# TODO 2 : Print only the index values
print("\nIndex Values: ", df.index.tolist()) 

# TODO 3 : Print the number of rows and columns using .shape
print("\nShape:", df.shape)

# TODO 4 : Print only the "Daily_Expense" column
print("\nOnly Daily_Expense Column: ")
print(df['Daily_Expense'])

# TODO 5 : Find the max and min daily expense
max_expense = df["Daily_Expense"].max()
print(max_expense)
min_expense = df['Daily_Expense'].min()
print(min_expense)

# TODO 6 : Calculate average of daily expense
avg_expense = df['Daily_Expense'].mean()
print(f"{avg_expense:.2f}")

# TODO 7 : Count how many days had expense greater than 200
count_above_200 = (df["Daily_Expense"] > 200).sum()
print("\n", count_above_200)

# TODO 8 : Add a column 'Above_200' with True/False values
df['Above_200'] = df['Daily_Expense'] > 200
print("\nUpdated DataFrame with 'Above_200' :")
print(df)

# TODO 9 : Save the updated DataFrame to 'C:\Aryan\GitHub Repo\pandas-learning-journey\cleaned_expenses.csv'
# Make sure the 'datasets' folder exists, or adjust path as needed
df.to_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\cleaned_expenses.csv', index = True)
print("\nSaved cleaned_expenses.csv to 'pandas-learning-journey'")