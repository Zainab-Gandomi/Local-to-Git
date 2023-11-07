import pandas as pd
import yaml

def yaml_to_dataframe(file_path):
    """
    Convert a YAML file to a pandas DataFrame.

    Parameters:
    file_path (str): Path to the YAML file.

    Returns:
    pandas.DataFrame: DataFrame created from the YAML data.
    """
    # Read the YAML file
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # Convert YAML data to DataFrame
    try:
        # Assuming the YAML data is a list of dictionaries
        df = pd.DataFrame(yaml_data)
    except Exception as e:
        print(f"Error: {e}")
        return None

    return df

# Example usage
yaml_file_path = 'example.yaml'  # Replace with your YAML file path
df = yaml_to_dataframe(yaml_file_path)

# Print the resulting DataFrame
if df is not None:
    print(df)

