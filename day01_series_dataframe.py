# Day 1 : Introduction & Data Structures

import pandas as pd

# Pandas Series
s = pd.Series([10,20,30,40])
print(s)

# Pandas DataFrame
data = {
    'Name' : ['Aryan', 'Riya'],
    'Age' : [21, 22]
}
df = pd.DataFrame(data)
print(df)


## Practice Tasks

# Create a Series of your daily expenses for a week
import pandas as pd

expenses = [150, 200, 500, 210, 400, 210, 300]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekly_expenses = pd.Series(data = expenses, index = days)
print(weekly_expenses)

# Create a DataFrame from:
# A dictionary of your marks in 5 subjects.
# A list of dictionary with your 3 friends' names and ages.
import pandas as pd

stu_data = {
    'Subject' : ['Science', 'Maths', 'English', 'Marathi', 'Hindi'],
    'Marks' : [86, 36, 86, 75, 85]
}

friends = [
    {
        'Name' : 'Darsh',
        'Age' : 28
    },
    {
        'Name' : 'Mukesh',
        'Age' : 22
    },
    {
        'Name' : 'Sunil',
        'Age' : 35
    }
]

stu_df = pd.DataFrame(stu_data)
print(stu_df)

friends_df = pd.DataFrame(friends)
print(friends_df)