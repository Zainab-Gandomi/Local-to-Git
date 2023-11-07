from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("pyspark SQL Hive").
                    config("spark.some.config.option", " some-value").
                    enableHiveSupport().getOrCreate( )
















                    