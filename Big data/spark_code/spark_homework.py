from pyspark import SparkConf, SparkContext

conf = SparkConf.setMaster("local").setAppName("Tempracher")
sc = SparkContext(conf = conf)

def praseLine(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temprature = float(fields[3]) * 0.1 (9.0/5.0) + 32.0
    return (stationID, entryType, temprature)

lines = cs.textFile("path")
prasedLines =lines.map(praseLine)
maxTemps =prasedLines.filter(lambda x: "TMAX" in x[1])
stationTemps = maxTemps.map(lambda x: (x[0], x[2]))
maxtempss = stationTemps.reduceByKey(lambda x, y: max(x,y))
results = maxtempss.collect()


for result in results:
    print result[0] + "\t{:.2f}F".format(result[1])


from pyspark.sql import SparkSession
from pyspark.sql import function as func
from pyspark.sql.type import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("OneConnectionForSuperHero").getOrCreate()

schema = StructType([ StructField("id", IntegerType(), True),\
                      StructField("name", StringType(), True)])

                      







