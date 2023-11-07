## first for start a sprksession
from pysprk.sql import SparkSession

## now strt sparksession
spark = SparkSession.builder.appName('my app').getOrCreate()

## to create dataframe 
df = spark.read.json(' file path')
df = spark.read.csv(' file path')
df = spark.read.parquet(' file path')

## for reading xml file cn not use this method

## to see data 
df.show()

df.printSchema()

## for initial statistic details
df.describe()

df.describe().show()

## if you need to create the schema specially when does not deal with read. method
##tools you need for that is 

from pyspark.sql.types import StructField,StringType,Integertype,StructType

## need to create the list of Structure fields
   ## param name : String, name of he field
   ## param data tpye : class: datatype of the field
   ## param nullable: boolean, whether the field can be null or not.

data_schema = [StructField("age", Integertype(), True), ("name",StringType(), True)]
final_struct = StructType(fields = data_schema)
df_with_schema = spark.read.json("path ", schema =final_struct)

## grabing data

df['age']

type(df['age'])

df.select('age').show()

new_df = df.select('age')
new_df.show()

##give first three row
df.head(3)

df.select('age','name').show()

## creating new columns
df.withColumn('newage',df['age']).show()
df.withColumn('newage',df['age']+10).show()

## to rename the column
df.withColumnRenamed('age','newage')

####### to use SQL
## register the datafarame as  a SQL temporary view
df.createOrReplaceTempView("name of the table like people")
sql_query = spark.sql("SELECT * FROM people")
sql_query.show()

##################
#### schema inference example
sc = spark.sparkContext

# load a text file and convert each line to a row.
lines = sc.textFile('datasets/people.txt')

# create another rdd and split the data by ,
parts = lines.map( lambda x : x.split(","))

# then take each data and convert it to row object
### people is rdd
people = parts.map( lambda p: Row(name=p[0], age=int(p[1])) )

###### infer the schema automatically and register the Dataframe as a table
### convert rdd(people) into the dataframe
schemaPeople = spark.createDataFrame(people)
schemaPeople.show()
################

#############
### programatic schema example
sc = spark.sparkContext

# load a text file and convert each line to a row.
lines = sc.textFile('datasets/people.txt')
parts = lines.map( lambda x : x.split(","))

# each line i sconverted to a tuple
people = parts.map( lambda p : ( p[0], p[1].strip()))

# need to define schema by providing datatypes of all the columns
schema = StructType ([StructField("name", StringType, True), StructField("age", Integertype, True)])

# apply the schema to the rdd
people_dataframe = spark.createDataFrame(people, schema)


##################

yelp = spark.read.json(" path")

yelp.createOrreplaceTempView("yelp_sql")
## now can use different sql query
spark.sql("select count(1) as counting business from yelp_sql").show()
spark.sql("select * from yelp_sql group by state").show(10)
spark.sql("select * from yelp_sql group by state order by businesses DESC").show()
spark.sql("select state, round(avg(review_count)) as avg_reviews from yelp_sql group by state order by avg_reviews DESC limit 8").show()
spark.sql("select state, count(1) as business from yelp_sql group by state order by business DESC").show(9)
### for nesting structure : first print schema then find where is the data the write query
yelp.printSchema()
spark.sql("select * from yelp_sql where hours.Wednesday.close = '21:00' limit 10").show()


###################

## parquet is compression and good to use in hive 
## to use parquet 

df = spark.read.parquet("path")

## to check how many record there
df.count()
 
df.printSchema()

## to select the specific column
dfSpecColumns = df.select("name", "year")
dfSpecColumns.show()
dfSpecColumns.count()

## example : to query like the most five popular girls name

popular = (df.filter(df['year'] == 1980)
            .filter(df['gender'] == 'F')
            .orderBy(df['total'].desc(), df['firstName'])
            .select("firstName").limit(5))


############
## write a qury to find how popular were the top 10 femalename of 2010 back in 1930
## udf = user define function
## spark SQL does not support SQL LOWER function so:
from pyspark.sql.functions import udf
lower = udf(lambda s: s.lower())

name_2010 = df.filter(df['year'] == 2010).
             select(df['total'].alias("total2010"),
                    df['gender'].alias("gender2010"),
                    df['firstName'].alias("firstName2010"),
                    lower(df['firstName'].alias("name2010")))

name_1930 =df.filter(df['year'] == 1930).
             select(df['total'].alias("total1930"),
                    df['gender'].alias("gender1930"),
                    df['firstName'].alias("firstName1930"),
                    lower(df['firstName'].alias("name1930")))

join_2010_1930 = name_2010.filter(name_2010.gender2010 == "F").
                           join(name_1930.filter(name_1930.gender1930 == "F"),
                           name_1930.name1930 == name_2010.name2010).
                           orderBy(name_2010.total2010.desc()).
                           limit(10).
                           select(name_2010.firstName2010.alias("name"), name_1930.total1930, name_2010.total2010)

join_2010_1930.show()

###############################


## to read the xml file in spark need to restart your spark shell
pyspark2 --master local --package com.dtabricks:spark-xml 2.10:0.4.1

## to read the xml
df = spark.read.format("here mention the package use for read").
          option("inferSchema", "true").
          option("rootTag", "employee").
          option("rowTag", "employee").
          load("path")

df.show()







