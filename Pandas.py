import pandas as pd
import numpy as np

# ============================================================
# 1. SERIES - a one dimensional labeled array
# ============================================================

marks = pd.Series([85, 90, 78, 92], index=["Ram", "Sham", "Sita", "Gita"])
print(marks)
print(marks["Sita"])       # access a value by its label
print(marks.values)        # underlying numpy array
print(marks.index)         # the labels


# ============================================================
# 2. DATAFRAME - a 2 dimensional labeled table (like an excel sheet)
# ============================================================

# 2a. Creating a DataFrame from a dictionary of lists
dict1 = {
    "name": ["Ram", "Sham", "Sita", "Gita"],
    "Class": ["9", "7", "6", "10"],
    "marks": [85, 90, 78, 92]
}
df = pd.DataFrame(dict1)
print(df)
#  We can also export the DataFrame to the Csv
df.to_csv("Csv_name.csv")
# We can also export the DataFrame to the CSV without index in it 
df.to_csv("Csv_name.csv",index = False)

# 2b. Creating a DataFrame from a list of lists
rows = [
    ["Ram", "9", 85],
    ["Sham", "7", 90],
    ["Sita", "6", 78],
    ["Gita", "10", 92]
]
df2 = pd.DataFrame(rows, columns=["name", "Class", "marks"])
print(df2)


# ============================================================
# 3. VIEWING / INSPECTING DATA
# ============================================================

print(df.head(2))      # first 2 rows
print(df.tail(2))      # last 2 rows
print(df.shape)        # (rows, columns)
print(df.columns)      # column names
print(df.dtypes)       # data type of each column
print(df.info())       # summary: dtypes, non-null counts, memory
print(df.describe())   # statistical summary of numeric columns


# ============================================================
# 4. SELECTING DATA
# ============================================================

print(df["name"])          # select a single column -> Series
print(df[["name", "marks"]])   # select multiple columns -> DataFrame

# loc -> select by label, iloc -> select by position
print(df.loc[0])           # row with index label 0
print(df.loc[0, "name"])   # single value by label
print(df.iloc[0])          # row at position 0
print(df.iloc[0:2, 0:2])   # first 2 rows, first 2 columns by position


# ============================================================
# 5. FILTERING ROWS (conditional selection)
# ============================================================

print(df[df["marks"] > 85])                       # students who scored above 85
print(df[(df["marks"] > 80) & (df["Class"] == "9")])   # multiple conditions


# ============================================================
# 6. ADDING / REMOVING COLUMNS AND ROWS
# ============================================================

df["passed"] = df["marks"] > 40        # add a new column
print(df)

df_dropped_col = df.drop("passed", axis=1)     # drop a column (axis=1)
df_dropped_row = df.drop(0, axis=0)            # drop a row by index label (axis=0)
print(df_dropped_col)
print(df_dropped_row)


# ============================================================
# 7. RENAMING COLUMNS AND INDEX
# ============================================================

df_renamed = df.rename(columns={"marks": "score"})
print(df_renamed)

# By this command we can change the index names also.
df.index = ["First", "Second", "Third", "Fourth"]
print(df)


# ============================================================
# 8. HANDLING MISSING DATA
# ============================================================

data_with_nan = {
    "name": ["Ram", "Sham", "Sita", "Gita"],
    "marks": [85, np.nan, 78, np.nan]
}
df3 = pd.DataFrame(data_with_nan)

print(df3.isnull())             # True where value is missing
print(df3.isnull().sum())       # count of missing values per column
print(df3.dropna())             # drop rows that contain any NaN
print(df3.fillna(0))            # replace NaN with a fixed value
print(df3.fillna(df3["marks"].mean()))   # replace NaN with the column mean


# ============================================================
# 9. SORTING
# ============================================================

print(df.sort_values("marks"))                 # ascending order by default
print(df.sort_values("marks", ascending=False))
print(df.sort_index())                          # sort by index label


# ============================================================
# 10. GROUPBY - split, apply, combine
# ============================================================

data_group = {
    "Class": ["9", "9", "6", "6", "10"],
    "marks": [85, 60, 78, 92, 88]
}
df4 = pd.DataFrame(data_group)

print(df4.groupby("Class")["marks"].mean())    # average marks per class
print(df4.groupby("Class")["marks"].max())     # highest marks per class
print(df4.groupby("Class").size())             # number of students per class


# ============================================================
# 11. MERGE / CONCAT - combining DataFrames
# ============================================================

students = pd.DataFrame({"id": [1, 2, 3], "name": ["Ram", "Sham", "Sita"]})
scores = pd.DataFrame({"id": [1, 2, 3], "marks": [85, 90, 78]})

merged = pd.merge(students, scores, on="id")   # join like a SQL join
print(merged)

more_students = pd.DataFrame({"id": [4], "name": ["Gita"]})
combined = pd.concat([students, more_students], ignore_index=True)  # stack rows
print(combined)


# ============================================================
# 12. APPLY / LAMBDA - transforming data
# ============================================================

df["grade"] = df["marks"].apply(lambda x: "A" if x >= 85 else "B")
print(df)


# ============================================================
# 13. READING AND WRITING CSV FILES
# ============================================================

df.to_csv("Sample.csv")               # writes with the default index column
df.to_csv("Sample.csv", index=False)  # writes without the index column

sample = pd.read_csv("Sample.csv")
print(sample)


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

# Q1. Create a DataFrame of 5 employees with columns name, department, salary.
#     Find the average salary per department.

# Q2. From the employees DataFrame, filter out everyone earning above the
#     average salary and sort them by salary in descending order.

# Q3. Add a new column "bonus" that is 10% of the salary, then save the
#     result to a CSV file without the index column.
