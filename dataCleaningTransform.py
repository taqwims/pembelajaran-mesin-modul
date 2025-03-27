import pandas as pd

# Reading the database
data = pd.read_csv("students.csv")

# Printing the top 10 rows
print(data.head(10))

# Show dataset info
data.info()

# Missing Value Checking
print(data.isna().sum())

# Filling NaN values
data['lunch'].fillna(data['lunch'].mode()[0], inplace=True)
data['reading score'].fillna(data['reading score'].mean(), inplace=True)
data['grade'].fillna(data['grade'].median(), inplace=True)

# Check the information of the dataset after filling missing values
data.info()
