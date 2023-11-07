import csv
import requests
import boto3

class DataExtractor:

    def __init__(self):
        # Initialize any required configurations or connections here
        pass

    def extract_data_from_csv(self, file_path):
        data = []
        try:
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    data.append(row)
            return data
        except Exception as e:
            print(f"Error extracting data from CSV: {str(e)}")
            return None

    def extract_data_from_api(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"API request failed with status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error extracting data from API: {str(e)}")
            return None

    def extract_data_from_s3_bucket(self, bucket_name, object_key):
        try:
            s3 = boto3.client('s3')
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            data = response['Body'].read().decode('utf-8')
            return data
        except Exception as e:
            print(f"Error extracting data from S3 bucket: {str(e)}")
            return None

# Example usage:
# extractor = DataExtractor()
# csv_data = extractor.extract_data_from_csv('data.csv')
# api_data = extractor.extract_data_from_api('https://api.example.com/data')
# s3_data = extractor.extract_data_from_s3_bucket('my-s3-bucket', 'data.txt')

