import psycopg2

# Database connection details
host = "my-first-aicore-rds-db.ccner1cnvq9i.eu-west-2.rds.amazonaws.com"
port = "5432"
database = "postgres"
user = "postgres"
password = "Alireza13"

# Establish the connection
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

# Perform database operations using the connection
# ...

# Close the connection when finished
#conn.close()