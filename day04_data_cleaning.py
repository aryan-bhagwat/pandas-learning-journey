# Day 4 : Data Cleaning: Missing Data, Duplicates

import pandas as pd
import numpy as np

# 1. Load the dataset

df = pd.read_csv('C:\\Aryan\\GitHub Repo\\pandas-learning-journey\\dirty_data.csv')
print(f"\nInitial DataFrame:\n{df}")

# 2. Handling Missing Values

print("\nMissing Values (isnull):\n", df.isnull())
print("\nTotal Missing at each column:\n", df.isnull().sum())

# 3. Drop Rows with Missing Values

df_dropped = df.dropna()
print(f"\nDataFrame after dropping rows with missing values:\n{df_dropped}")

# 4. Fill Missing Values

df_filled = df.fillna({'Age' : df['Age'].mean(), 'City' : 'Unknown', 'Salary' : df['Salary'].median()})
print(f"\nDataFrame after filling missing values:\n{df_filled}")


# 5. Remove Duplicates

print(f"\nBefore removing duplicates:\n{df}")
df_duplicates = df.drop_duplicates()
print(f"\nDataFrame after removing duplicates:\n{df_duplicates}")

df_filled = df_duplicates.fillna({'Age' : df['Age'].mean(), 'City' : 'Unknown', 'Salary' : df['Salary'].median()})
print(f"\nDataFrame after filling missing values and removing duplicates:\n{df_filled}")


## Practice Set
import pandas as pd
import numpy as np

# TODO 1: Load the dirty_data.csv file and print the all rows
df = pd.read_csv('C:\\Aryan\\GitHub Repo\\pandas-learning-journey\\dirty_data.csv')
print(f"\nAll rows in the DataFrame:\n{df}")

# TODO 2: Count how many rows have at least one missing value
missing_count = df.isnull().any(axis=1).sum()
print(f"\nNumber of rows with at least one missing value:\n{missing_count}")

# TODO 3: Fill missing values in the 'Age' column with the median age
# TODO 4: Fill missing City with "Not Provided"
# TODO 5: Fill missing Salary with average salary
df_filled = df.fillna(
    {
        'Age' : df['Age'].median(),
        'City' : 'Not Provided',
        'Salary' : df['Salary'].mean()
    }
)
print(f"\nAfter filling Values:\n{df_filled}")

# TODO 6: Save the cleaned DataFrame to a new CSV file named 'cleaned_data.csv'

df_filled.to_csv('C:\\Aryan\\GitHub Repo\\pandas-learning-journey\\cleaned_data.csv', index = False)
print("Cleaned DataFrame saved to 'cleaned_data.csv'.")

# TODO 7: Remove duplicates and save to 'no_duplicates.csv'

df_no_duplicated = df_filled.drop_duplicates()
df_no_duplicated.to_csv('C:\\Aryan\\GitHub Repo\\pandas-learning-journey\\no_duplicates.csv', index = False)
print("DataFrame without duplicates saved to 'no_duplicates.csv'.")