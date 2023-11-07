import pandas as pd

dataframe = pd.read_csv("C:/Users/zainab/Downloads/Salaries.csv")

print(dataframe)

#What is the ratio between people in the fire department over people in the police department

# define function to find 'police' 

def find_police(x):
    return "POLICE" in x


# use apply to search for it in JobTitle
dataframe["isPolice"] = dataframe["JobTitle"].apply(find_police)

sum_of_the_police = dataframe["isPolice"].sum()
print(sum_of_the_police)

# define function to find 'fire' 

def find_fire(y):
    return "FIRE" in y

dataframe["isfire"] = dataframe["JobTitle"].apply(find_fire)

sume_of_the_fire = dataframe["isfire"].sum()
print(sume_of_the_fire)

ratio_fire_over_police_deprtment = sume_of_the_fire / sum_of_the_police
print(ratio_fire_over_police_deprtment)


# What is the mean salary of the police department? Use the "BasePay" column.

# Filter the DataFrame for the police department
police_data = dataframe[dataframe["isPolice"]]
#print(police_data)

# Calculate the mean salary for the police department
mean_police_salary = police_data["BasePay"].mean().__round__()
print("Mean salary of the police department is", mean_police_salary)


#What is the mean salary of the fire department? Use the "BasePay" column.
fire_data = dataframe[dataframe["isfire"]]

mean_fire_salary = fire_data["BasePay"].mean()
print("Mean salary of the fire department is", mean_fire_salary)


# How many unique jobs are there? Look at the unique method in pandas

unique_job = dataframe["JobTitle"].unique()
unique_job_sum = dataframe["JobTitle"].nunique()
#print(unique_job)
print("Number of unique job is: ", unique_job_sum)


# Count how many people have the first name "John"
'''
# Split the 'EmployeeName' on spaces and get the first part
first_names = dataframe['EmployeeName'].str.split(' ').str[0]
#print(first_names)

# Count occurrences of 'John' in the first names (case insensitive)
john_count = (first_names.str.lower() == 'john').sum()

print("Number of people with the first name 'John':", john_count)
'''

# Split the 'EmployeeName' on spaces and get the first part
first_names = dataframe['EmployeeName'].str.split(' ').str[0]

# Filter for names that are 'John' (case insensitive)
john_filter = (first_names.str.lower() == 'john')

# Get the count of occurrences of 'John'
john_count = john_filter.sum()

# Get the list of names that are 'John'
john_list = dataframe['EmployeeName'][john_filter]

print("Number of people with the first name 'John':", john_count)
print("List of people with the first name 'John':")
print(john_list)



# Find the surname of everyone whose first name is more than 6 characters long


# Split the 'EmployeeName' on spaces and get the first and last parts
names = dataframe['EmployeeName'].str.split(' ')

# Filter for last names where the first name is more than 6 characters
long_first_name_surnames = names[names.apply(lambda x: len(x[0]) > 6)]

print("Surnames for people with first names longer than 6 characters:")
print(long_first_name_surnames)


# Create a new column called "last_updated" where every value is equal to the current time (use the datetime module and format the date in ISO format).
# Create a new derived column called "time_ratio" in the DataFrame which is the proportion of overtime pay to base pay
# In one line, create a new DataFrame called "new_df" which contains only people who earn more than 100K base salary
# Now create a new derived column in "new_df" that is the sum of their pays, not including base salary
# Append a new row to the DataFrame to represent a made up character (Look up the append method in pandas)
# He/she has no benefits, so set this attribute to not a number using np.nan
# Make up the other column values, but make sure they are standardised to the same convention as the other values in that column