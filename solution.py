# solution.py

import pandas as pd

# Step 1: Load the Data
# Load the data from 'employee_data.csv'
data = pd.read_csv('employee_data.csv')

# Step 2: Inspect the Data
# Display the first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# Display missing values count for each column
print("\nMissing values in the dataset:")
print(data.isnull().sum())

# Identify duplicate rows
duplicates = data[data.duplicated()]
print("\nDuplicate rows in the dataset:")
print(duplicates)

# Step 3: Data Cleaning
# Remove rows with missing values
data_cleaned = data.dropna()

# Drop duplicate rows
data_cleaned = data_cleaned.drop_duplicates()

# Step 4: Data Analysis
# Department with the highest average salary
highest_avg_salary_department = data_cleaned.groupby('Department')['Salary'].mean().idxmax()
highest_avg_salary = data_cleaned.groupby('Department')['Salary'].mean().max()
print(f"\nDepartment with the highest average salary: {highest_avg_salary_department} (ZAR {highest_avg_salary:.2f})")

# Number of employees in each department
department_counts = data_cleaned['Department'].value_counts()
print("\nNumber of employees in each department:")
print(department_counts)

# Step 5: Data Export
# Save the cleaned data to 'cleaned_emplData.xlsx'
data_cleaned.to_excel('cleaned_emplData.xlsx', index=False)

# Instructions: take a screenshot of this output to submit as required.
