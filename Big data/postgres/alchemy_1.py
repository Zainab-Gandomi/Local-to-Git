from sqlalchemy import create_engine
import pandas as pd

database_type = 'postgresql'
dbapi = 'psycopg2'
host = 'localhost'
user = 'postgres'
password = 'Alireza13'
database = 'Pagila'
port = 5432

engine = create_engine(f"{database_type}+{dbapi}://{user}:{password}@{host}:{port}/{database}")

from sqlalchemy import text
# two option for execute sql query as follow:
# this option close the query at the end
with engine.execution_options(isolation_level='AUTOCOMMIT').connect() as con:
    result = con.execute(text("SELECT * FROM actor LIMIT 10"))
    for row in result:
        print(row)

# with this option we need to use engine.close to close the query

#with engine.connect() as connection:
 #   result = connection.execute(text("SELECT * FROM actor LIMIT 10"))
 #   for row in result:
 #       print(row)

# read the data in dataframe
actors = pd.read_sql_table('actor', engine)
print(actors.head(5))
