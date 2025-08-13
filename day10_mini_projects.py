# Day 10 : Mini Projects

import pandas as pd
import os

# Mini Project 1 : Sales Report Genreator

## Read dataset & generate simple summary

sales_df = pd.read_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\sales_data.csv')
print(f"Sales Data Summary:\n{sales_df.describe()}\n")

## Total Sales

total_sales = sales_df['Sales'].sum()
print(f"Total Sales: {total_sales}\n")

## Sales by Region

sales_by_region = sales_df.groupby('Region')['Sales'].sum().reset_index()
print(f"Sales by Region:\n{sales_by_region}\n")

## Save Report

sales_by_region.to_csv('C:\Aryan\GitHub Repo\pandas-learning-journey\sales_by_region_report.csv', index=False)
