# Day 10 : Mini Projects

import pandas as pd
import os

# Mini Project 1 : Sales Report Generator

## Read dataset & generate simple summary
sales_df = pd.read_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\day10_sales_data.csv')
print(f"Sales Data Summary:\n{sales_df.describe()}\n")

## Total Sales
total_sales = sales_df['Sales'].sum()
print(f"Total Sales: {total_sales}\n")

## Sales by Region
sales_by_region = sales_df.groupby('Region')['Sales'].sum().reset_index()
print(f"Sales by Region:\n{sales_by_region}\n")

## Save Report
sales_by_region.to_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\sales_by_region_report.csv', index=False)


# Mini Project 2 : Student Grade Analysis

## Load Dataset
grades_df = pd.read_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\student_grades.csv')

## Calculate average score per subject
average_scores = grades_df.mean(numeric_only=True).reset_index()
average_scores.columns = ['Subject', 'Average Score']
print(f"Average Scores per Subject:\n{average_scores}\n")


# PRACTICE TODOs (Do these yourself — no answers here)

## Mini Project 1 TODOs:

# TODO 1: From sales_df, find the top 5 products by total sales.
top_products = sales_df.groupby('Product')['Sales'].sum().nlargest(5).reset_index()
print(f"Top 5 Products by Sales:\n{top_products}\n")

# TODO 2: Find the month with the highest total sales.
highest_month = sales_df.groupby(sales_df['Date'].str[:7])['Sales'].sum().idxmax()
print(f"Month with Highest Sales: {highest_month}\n")

# TODO 3: Calculate average sales per region and save to outputs/avg_sales_by_region.csv.
avg_sales_by_region = sales_df.groupby('Region')['Sales'].mean().reset_index()
avg_sales_by_region.to_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\ avg_sales_by_region.csv', index=False)

# TODO 4: Filter rows where Sales > 1000 and save them to outputs/high_value_sales.csv.
high_value_sales = sales_df[sales_df['Sales'] > 1000]
high_value_sales.to_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\high_value_sales.csv', index=False)

## Mini Project 2 TODOs:
# TODO 5: From grades_df, find the student with the highest total score.
top_student = grades_df.loc[grades_df['Math'] + grades_df['Science'] + grades_df['English'] ==
                          (grades_df['Math'] + grades_df['Science'] + grades_df['English']).max()]
top_student = top_student[['Name', 'Math', 'Science', 'English']]
print(f"Top Student:\n{top_student}\n")

# TODO 6: Calculate pass rate if pass mark is 40 for each subject.
pass_rate = (grades_df[['Math', 'Science', 'English']] >= 40).mean() * 100
pass_rate = pass_rate.reset_index()
print(f"Pass Rate per Subject:\n{pass_rate}\n")

# TODO 7: Find subject with the highest average score.
highest_avg_score = grades_df[['Math', 'Science', 'English']].mean().idxmax()
print(f"Subject with Highest Average Score: {highest_avg_score}\n")

# TODO 8: Save a sorted list of students by total score (descending) to outputs/top_students.csv.
top_students = grades_df.assign(Total=grades_df[['Math', 'Science', 'English']].sum(axis=1))
top_students = top_students.sort_values(by='Total', ascending=False)[['Name', 'Total']]
top_students.to_csv('C:\Aryan\GitHub Repo\pandas-learning-journey/top_students.csv', index=False)

## Mini Project 3: E-commerce Orders
# TODO 9: Load datasets/orders.csv and datasets/customers.csv.
# TODO 10: Merge orders with customers on 'CustomerID'.
# TODO 11: Find the total orders per country.
# TODO 12: Save a pivot table of country vs month showing order counts.


# Tips:
# - Use groupby() + sum()/mean() for aggregations.
# - pd.merge(df1, df2, on='col') to join datasets.
# - df.sort_values(by=..., ascending=False) for ranking.
# - pd.pivot_table() for summaries.