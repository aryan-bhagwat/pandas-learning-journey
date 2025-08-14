# 🐼 Pandas Quick Revision — Days 1–10

## 📂 1. Reading & Writing Files
| Function | Purpose |
|----------|---------|
| `pd.read_csv("file.csv")` | Load CSV file into DataFrame |
| `pd.read_excel("file.xlsx")` | Load Excel file |
| `df.to_csv("file.csv", index=False)` | Save DataFrame to CSV |
| `df.to_excel("file.xlsx", index=False)` | Save DataFrame to Excel |
| `pd.read_json("file.json")` | Load JSON file |
| `df.to_json("file.json")` | Save DataFrame to JSON |

---

## 📄 2. Data Inspection
| Function | Purpose |
|----------|---------|
| `df.head(n)` | First `n` rows (default 5) |
| `df.tail(n)` | Last `n` rows (default 5) |
| `df.shape` | Rows & columns count |
| `df.columns` | Column names |
| `df.index` | Row index values |
| `df.dtypes` | Data types of columns |
| `df.info()` | Summary of DataFrame |
| `df.describe(include='all')` | Summary statistics (numeric + object) |
| `df.sample(n)` | Random sample of rows |
| `df.memory_usage()` | Memory usage of DataFrame |

---

## 🛠 3. Selecting Data
| Function | Purpose |
|----------|---------|
| `df['col']` | Select single column (Series) |
| `df[['col1', 'col2']]` | Select multiple columns |
| `df.loc[row_labels, col_labels]` | Label-based indexing |
| `df.iloc[row_index, col_index]` | Position-based indexing |
| `df.at[row_label, col_label]` | Fast access single value (label) |
| `df.iat[row_index, col_index]` | Fast access single value (position) |
| `df.filter(like='pattern', axis=1)` | Filter columns by name pattern |

---

## 🔍 4. Filtering & Conditional Selection
| Function | Purpose |
|----------|---------|
| `df[df['col'] > 50]` | Filter rows by condition |
| `(df['col1'] > 50) & (df['col2'] < 100)` | Multiple conditions |
| `df.query("col > 50 and other < 100")` | Query syntax |
| `df.isnull()` / `df.notnull()` | Check missing values |
| `df[df['col'].isin([1, 2, 3])]` | Filter by values in list |

---

## 🧹 5. Data Cleaning
| Function | Purpose |
|----------|---------|
| `df.dropna()` | Remove missing values |
| `df.fillna(value)` | Fill missing values |
| `df.duplicated()` | Find duplicates |
| `df.drop_duplicates()` | Remove duplicates |
| `df.replace(old, new)` | Replace values |
| `df.astype(dtype)` | Change column type |
| `df.rename(columns={'old': 'new'})` | Rename columns |
| `df.clip(lower, upper)` | Limit values within range |
| `df.str.strip()` | Remove whitespace from strings |

---

## 🔄 6. Transformation
| Function | Purpose |
|----------|---------|
| `df['col'].apply(func)` | Apply function to Series |
| `df.apply(func, axis=1)` | Apply function to rows |
| `df.map(func)` | Map values in Series |
| `df.assign(new_col=value)` | Add new column |
| `df['col'] = df['col'].str.lower()` | String methods |
| `df['col'] = df['col'].round(2)` | Round numeric values |
| `df['col'].astype(int)` | Convert column type |

---

## 📊 7. Grouping & Aggregation
| Function | Purpose |
|----------|---------|
| `df.groupby('col')` | Group rows by column |
| `.sum()`, `.mean()`, `.count()`, `.max()`, `.min()` | Aggregations |
| `.agg({'col1': 'sum', 'col2': 'mean'})` | Multiple aggregations |
| `df.pivot_table(values, index, columns, aggfunc)` | Pivot table |
| `df.groupby(['col1', 'col2']).size()` | Group size counts |

---

## 📎 8. Merging, Joining, Concatenation
| Function | Purpose |
|----------|---------|
| `pd.merge(df1, df2, on='col')` | Merge DataFrames |
| `pd.concat([df1, df2])` | Concatenate DataFrames |
| `.sort_values(by='col')` | Sort by column |
| `.sort_index()` | Sort by index |
| `df.join(other_df)` | Join by index |

---

## 🕒 9. Time Series
| Function | Purpose |
|----------|---------|
| `pd.to_datetime(df['date'])` | Convert to datetime |
| `df['date'].dt.year` | Extract year |
| `df['date'].dt.month` | Extract month |
| `df['date'].dt.day` | Extract day |
| `df['date'].dt.weekday` | Extract weekday |
| `df.set_index('date')` | Set date as index |
| `df.resample('M').sum()` | Resample by month |
| `df.resample('D').mean()` | Resample by day |

---

## 📈 10. Miscellaneous
| Function | Purpose |
|----------|---------|
| `df.value_counts()` | Frequency counts |
| `df.corr()` | Correlation matrix |
| `df.nunique()` | Unique value counts |
| `df.sort_values()` | Sort by column |
| `df.sort_index()` | Sort by index |
| `df.eq()` | Compare values element-wise |

---

✅ **Tip:** Most Pandas operations can be chained together for cleaner, more concise code.
