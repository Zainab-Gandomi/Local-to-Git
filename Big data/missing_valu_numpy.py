# Download the dataset from the following URL: https://aicore-files.s3.amazonaws.com/Data-Eng/Building_Permits.csv

import pandas as pd 
import numpy as np

data = pd.read_csv("https://aicore-files.s3.amazonaws.com/Data-Eng/Building_Permits.csv")

#Load it into a DataFrame

building_df = pd.DataFrame(data)

# Observe the name of the columns and the corresponding dtype

building_df.info()

# Check how many missing values each column has

missing_value = building_df.isnull().sum()

# Calculate the percentage of missing values for each column
missing_percentage = missing_value / len(building_df) *100
print(missing_percentage)

# Using the missingno library, plot the nullity matrix. Do you see any pattern in data missingness?
import missingno as msno
msno.matrix(building_df)

# Create a copy of your DataFrame (call it df_filled_backwards). Use the back fill method to fill in the missing values
df_filled_backwards = building_df.fillna(method="bfill")
# Create a copy of your DataFrame (call it df_filled_forwards). Use the forward fill method to fill in the missing values
df_filled_forwards = building_df.fillna(method="ffill")
# Create a copy of your DataFrame (call it df_filled_linearly). Use the linear fill method to fill in the missing values
df_filled_linearly = building_df.interpolate(method="linear")
# For the three new dataframes, plot the distribution of both 'Street Number Suffix' and 'Zipcode

df_filled_backwards[['Street Number Suffix', 'Zipcode']].plot(kind='hist')
df_filled_forwards[['Street Number Suffix', 'Zipcode']].plot(kind='hist')
df_filled_linearly[['Street Number Suffix', 'Zipcode']].plot(kind='hist')