import re
from pyspark import SparkConf, SparkContext

def normalizedWords(text):
    return re.compile(r'\W+', re.UNICODE).split(text.lower())

conf = SparkConf().setMaster("local").setAppName("wordCounts")
sc = SparkContext( conf  = conf)

dataInput = sc.textFile("path")
words = dataInput.flatMap(normalizedWords)
wordCount = words.countByValue()

for word, count in wordCount.items():
    cleanWord = word.encode('ascii','ignore')
    if (cleanWord):
        print  cleanWord, count






from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").seAppName("totalCostomerSpend")
sc = SparkContext( conf = conf )

def costomerDataextract(line):
    fields = line.split()
    return int(fields[0]), float(fields[2])

inputData = sc.textFile("path")
mapInput = inputData.map(costomerDataextract)
totalByCustomer = mapInput.reduceByKey(lambda x, y: x + y )

results = totalByCustomer.collect()
for result in results:
    return result








