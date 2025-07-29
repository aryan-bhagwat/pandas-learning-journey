# Day 3 : Indexing, Selection & Filtering

import pandas as pd

df = pd.read_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\cleaned_expenses.csv')


# 1. Selecting Columns

print(df['Daily_Expense'])

print(df[['Weekday', 'Daily_Expense']])

# 2. Row Selection with .loc[] and .iloc[]

print(f"\n{df.loc[2]}")

print(f"\n{df.iloc[2]}")

print(f"\n{df.iloc[2:5]}")

# 3. Filtering Rows (Conditional)

print(f"\n{df[df['Daily_Expense'] > 200]}")

print(f"\n{df[df['Daily_Expense'] < 200]}")

# 4. Combine Conditions

print(f"\n{df[(df['Daily_Expense'] < 200) & (df['Weekday'] != 'Saturday')]}")


## Practice Set

# TODO 1: Select only the 'Weekday' column and print it
print(df['Weekday'])

# TODO 2: Print the row where Weekday is "Friday"
print(df[df['Weekday'] == 'Friday']) 

# TODO 3: Print all rows where Daily_Expense is equal to 150
print(df[df['Daily_Expense'] == 150])

# TODO 4: Use .iloc to print the 5th row
print(df.iloc[4])

# TODO 5: Print the first 3 rows using .iloc
print(df.iloc[0:3])

# TODO 6: Filter and print days where Daily_Expense is greater than or equal to 200
print(df[df['Daily_Expense'] >= 200])

# TODO 7: Filter and print days where Daily_Expense is less than 200 or equal to 210
print(df[(df['Daily_Expense'] < 200) | (df['Daily_Expense'] == 210 )])

# TODO 8: Filter and print rows where Weekday is either 'Monday' or 'Sunday'
print(df[df['Weekday'].isin(['Monday', 'Sunday'])])

# TODO 9: Add a column `Is_Weekend` with True if Weekday is Saturday or Sunday
df['Is_Weekend'] = df['Weekday'].isin(['Saturday', 'Sunday'])
print(df)

# TODO 10: Save the filtered DataFrame (Daily_Expense >= 200) to 'datasets/high_expense.csv'
high_expense_df = df[df['Daily_Expense'] >= 200]

high_expense_df.to_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\high_expenses.csv', index = False)
print("Filtered high expense data saved to 'C:\Aryan\GitHub Repo\pandas-learning-journey\high_expenses.csv'")