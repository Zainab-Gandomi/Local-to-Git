import pandas as pd
import numpy as np 
 
car_insurance = pd.read_csv("C:/Users/zainab/Downloads/car_insurance.csv")

#Load it into a DataFrame

car_df = pd.DataFrame(car_insurance)
#print(car_df)

# Observe the name of the columns and the corresponding dtype

print(car_df.dtypes)

# Check how many missing values each column has
car_df.info()

missing_values_per_column = car_df.isnull().sum()

print("Missing values per column:")
print(missing_values_per_column)

# Drop the rows containing missing values

data_without_null = car_df.dropna()
print(data_without_null)

# For the numerical values, obtain the mean average value

value_to_impute_age = car_df["Age"].mean().__round__()
car_df["Age"].fillna(value_to_impute_age, inplace= True)

value_to_impute_prevattempt = car_df["PrevAttempts"].mean().__round__()
car_df["PrevAttempts"].fillna(value_to_impute_prevattempt, inplace= True)

print(car_df)

# Observe the Job column. How many categories can you find? What is the most frequent?

print(car_df["Job"].unique())

Job_distribution = car_df["Job"].value_counts()
print(Job_distribution)



# Create a new column with the duration of each call in seconds

from datetime import datetime, timedelta

# Convert the 'call_duration' column to datetime
car_df['CallStart'] = pd.to_datetime(car_df['CallStart'], format='%H:%M:%S')
car_df['CallEnd'] = pd.to_datetime(car_df['CallEnd'], format='%H:%M:%S')

#car_df['CallDuration'] = car_df["CallEnd"] - car_df["CallStart"]

# Function to convert timedelta to seconds
def timedelta_to_seconds(td):
    return td.total_seconds()

# Calculate the duration in seconds
car_df['call_duration_seconds'] = (car_df["CallEnd"] - car_df["CallStart"]).apply(timedelta_to_seconds)

print("Data with call duration in seconds:")
print(car_df)



# What is the average duration of each call?


# For those people contacted during the first half of the year (Jan-June). What is the most common way of communication (telephone, cellular...)?