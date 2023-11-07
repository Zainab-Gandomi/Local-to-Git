import psycopg2  # the appropriate database library for database system
import yaml


class DatabaseConnector:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Database connection established.")
        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")

    def upload_data(self, data, table_name):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                # need to replace the following SQL statement with the appropriate INSERT statement for database
                insert_query = f"INSERT INTO {table_name} VALUES (%s, %s, %s)"  # Example SQL statement
                cursor.executemany(insert_query, data)
                self.connection.commit()
                print("Data uploaded successfully.")
            except Exception as e:
                self.connection.rollback()
                print(f"Error uploading data to the database: {str(e)}")

    def __init__(self):
        # Initialize any necessary configuration or parameters for data cleaning here
        self.credentials = self.read_db_creds()
        self.load_credentials()

    def read_db_creds(self):
        try:
            with open('db_creds.yaml', 'r') as file:
                creds = yaml.safe_load(file)
                return creds
        except Exception as e:
            print(f"Error reading database credentials: {str(e)}")
            return {}

    def load_credentials(self):
        if not self.credentials:
            return
        self.host = self.credentials.get('RDS_HOST', '')
        self.database = self.credentials.get('RDS_DATABASE', '')
        self.user = self.credentials.get('RDS_USER', '')
        self.password = self.credentials.get('RDS_PASSWORD', '')
        self.port = self.credentials.get('RDS_PORT', '')

    # ... Other methods for data extraction ...

# Example usage:
# db_connector = DatabaseConnector()
# db_connector.connect()
  













# Example usage:
# db_connector = DatabaseConnector(host='your_host', database='your_database', user='your_user', password='your_password')
# db_connector.connect()
# data_to_upload = [(1, 'John'), (2, 'Alice'), (3, 'Bob')]  # Example data to upload
# db_connector.upload_data(data_to_upload, 'your_table_name')
# db_connector.disconnect()











