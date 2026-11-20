import pyodbc
from sqlalchemy import create_engine

server = 'database-server-for-my-test.database.windows.net'
database = 'my-database'
username = 'zizi'
password = 'Alireza13'
driver = '{ODBC Driver 18 for SQL server}'

#create the connection string
connection_string = f'Driver={driver};server=tcp:{server},1433;\
                      Database={database};uid={username};pwd={password};\
                      Encrypt=yes;TrustServerCertification=no;connection Timout=30;'

# Create the engine to connect to the database
engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(connection_string))

#load the csv file
import pandas as pd
df = pd.read_csv("C:/Users/zainab/Downloads/film_actor_pagila.csv")

#write data to the azure SQL db
df.to_sql('film_actors', engine, if_exists='replace')