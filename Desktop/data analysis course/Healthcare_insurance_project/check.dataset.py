
import os

# Display the current project folder
print("Healthcare Insurance Project")

# Check whether the dataset exists
file_path = "project_data/insurance_raw_data.csv"

if os.path.exists(file_path):
    print("SUCCESS: Dataset found!")
    print("File location:", file_path)
else:
    print("ERROR: Dataset not found.")
    print("Please check the filename and folder.")






    