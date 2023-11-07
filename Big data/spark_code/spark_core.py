# to start python spark shell
pyspark 

# command to all the argumen you need for adjusting driver, executer , yarn ,,...
--help

--master yarn

## to run spark with yarn and specific configuration
pyspark2 --master yarn --num-executers 4 --executor-memory 2g

### this comamand show all configuration for spark inside the shell
sc._conf.getAll()

## create rdd 

from pyspark import SparkContext, SQLContext,SparkConf, StorageLevel
import  numpy as np
from __future__ import division
from decimal import Decimal
import matplotlib.pyplot as plt

sparkconf = SparkConf().setAppName("myapp").setMaster("local[3]")
sc = SparkContext(conf= SparkConf)

##to repartition rdd 
myvariable = sc.textfile("path", "no of partition like" 4,use_nuicode=False ).repartition(6)
 
# to see data
myvariable.take(10)

##to apply schema rdd
## its convert everything to row object

field = ("name", "countray", "career", "matches", "won", "lost", "ties", "toss")
from collections import namedtuple
captian = namedtuple('Captian', fields)
def parseRecs( line ):
    fields = line.split(",")
    return Captain( fields[0], fields[1], fields[2], int( fields[3]), int( fields[4]), int( fields[5]), int(fields[6]), int( fields[7]) )
captians = myvariable.map( lambda rec: parseReccs(rec) )

captians.take(5)

## gives the captain name play more than 100 game

captains_100 = captians.filter( lambda rec: rec.maches > 100 )

captains_100.take(10)

captians_more_win = captains_100.filter( lambda rec : rec.win > rec.lost)
## from captain_more_win can extract the any data like country , name, ...

country_name = captians_more_win.map(lambda rec: (rec.country, rec.name) )
country_name.collect()

## for number of maches for country 
country_maches = country_name.reduceByKey( lambda a, b : a + b )
country_maches.collect()

## to sort the name of county
country_maches.sortByKey(ascending = False).collect()

## when want to collect statistic

captains_1001 = captains_100.filter( lambda rec: rec[1] > 0)
captains_100_percent_win = captains_1001.map( lambda rec: (rec.name, float(rec.win/rec.maches)))
captains_100_percent_win.collect()

## we save the resule in varialbe like results to can use matplotlib to draw a chart by using action operation like collect

results = captains_100_percent_win.sortBy( lambda rec : rec[1], ascending=False).collect()
 
## to draw pie chart

mylist = []
mylist1 = []

for (a,b) in results:
    mylist.append(a)
    mylist1.append(b)

plt.pie(mylist1, labels=mylist)

plt.axis('equal')
plt.show()


## when you want to execution became faster cn use cache and its remain until during execution
## like when you have a some 


## to start sprk shell 
## local [2] means that two proccessor we need
## local [*] means that we dont know how many proccessor we can access and they use they mximum available

pyspark2 --master local[2]
pyspark2 --master local[*]

## to convert any python collection like range, list,dictionary, .. to rdd
a = sc.parllelize(range(1,100))

a.collect()

## to find the number of prtition
a.getNumPartitions()
## depens on the how many proccessor cores you have give you number of partiton

## to crete rdd with the exact number of partition like 10
a = sc.parllelize(range(1,100),10)

## to reprtition create another rdd
b = a.reprtition(12)    ## to increase
c = a.coalesce(6)        ## to decrease


#######################################
## to run spark for job need some configuration anything want cn find from --help
pysprk2 --master yarn --driver-memory 1g --executer-memory 500m --executer-core 2 --num-executor 3

## to read text file
book = sc.textFile("path")

## some action can use especilly to check that file is load
book.take(8)
book.count()
book.first()

## to word count
a = book.flatMap( lambda line: line.split(" "))
a = book.map( lambda line: line.split(" "))

## diferetbetween map and flat map is that as result mp give nested list and it mk difficult for word count but flatmap give the split flt word in one list
## so its better ust flatmap for spliting the word

a = book.flatMap( lambda line: line.split(" "))
b = a.map( lambda word: (word,1) )
c = b.reducByKey( lambda x, y : x + y)

###OR

counts = text_file.flatMap(lambda line: line.split(" "))
                  .map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b )