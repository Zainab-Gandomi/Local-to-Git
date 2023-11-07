####### get tweets in real time using twitter API
# we are using tweepy library to rout all the live tweets to a TCP socket server.
# this server is hosted in cloud

import tweepy

# OAuthHandler used for Authentication protocol(OAuth) of twitter API.

from tweepy import OAuthHandler

# import stream and streamListener
# this actually listen to streaming data getting fom the socket

from tweepy import Stream
from tweepy.streaming import StreamListener

# import socket use to create socket connection with localhost like local server
# import json used because data comes in json format.
 
import socket
import json

#to connect to twitter API, need 4 keys

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""


#### class tweetsListener
#1. it is listening to the stream via streamListener
#2. construcor function (init) : initilizing the socket
#3. data contains the tweets json coming from the stream
#4. in this json object field 'text' contains the actual tweet
#5. the actual tweet is  extracted & send to the client socket
#6. error handling is doen to cach & throw errors.

class TweetsListener(StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket
    def on_data(self, data):
        try:
            msg = json.loads (data)
            print ( msg ['text'].encode('utf-8'))
            # print (msg ['created at'].encode('utf-8'))
            self.client.socket.send( msg ['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print ("error on data : %s" % str(e))    
        return True
    def on_errror(self, status):
        print(status)
        return True


#### function sendData()
#1. auth is doing Authentication check using Oauthhandler. it uses 4 keys of Twitter APIs.
#2. consumer_key & consumer_secret are like username 
# access_token & access_secret are like password
#3. twitter_stream will get the actual twitter live stream data.
#4. it will call stream with auth & call the class tweetsListener & pass c_socket info to the class
#5. from the stream of tweets, filter & take only tweets which contains "Trump"

def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track=['Trump'])


#### socket creation
#1. socket is created by using socket function
#2. host is localhost, 
#3. port is 5555 ( it can be anything, unique for this service)
#4. now bind host & port to the socket

s =socket.socket()     #create a socket object
host = "127.0.0.1"     # get local machine name
port = 9999            # reserve a port for your service.
s.bind((host, port))
print("Listening on port: %s" % str(port))

# socket will wait and listen for few seconds.
# after that connection is made

s.listen(5)                  # now wait for client connection
c, addr = s.accept()         # establish connection with client
print ("receied request from: " + str(addr))

####### send live tweets in real time to the socket
## function sendData will send all the tweets cotaining word'trump' to socket 'c' in real time.
## this will be consumed in the nex code of Spark Streaming to do Trend analysis.

# to see the tweet context
sendData( c )


###################################################
###### trend analysis on Twitter live data using Spark Streaming

##import sparkContext & streamingContext from pyspark library.

from __future__ import print_function
from pyspark import SparContext
from pyspark.streaming import StreamingContext

# create a sparkContext with Appname "streamingTweeterAnalysis"
# setting the LogLevel of sparkcontext to ERROE. this will not print all the logs wich are INFP or WARN level.
# create Spark Streaming Context using SC(spark context). parameter 10 is the batch interval.
# every 10 second the analysis will be done.

sc = SparkContext(appName = "streamingTweeterAnalysis")
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 10)

# Connect to socket broker using ssc (spark streaming context)
# host : "127.0.0.1" & port : 9999
# with socketTextstream we make a reciver, this responsible for monitoring the port and getting data

socket_stream = ssc.socketTextStream("127.0.0.", 9999)

# window function parameter sets the window length. all the analysis will be done on tweets stored for 60 secs.

lines = socket_stream.window( 60 )

# sliding interval means when the analysis have to happen 
# for this analysis because we did not set sliding interval , by default will be 10 second likebatch interval.

##### process the stream
#1. receives tweet message, stored in lines. INput Dstream
#2. splits te message into words. Apply transformation on DStream: flatMap
#3. filter all the words which start with a hashtag(#). transformation: filter
#4. convert the words to lowercase. transformation : map
#5. map each tag to (word, 1). transformation : map
#6. then reduce and count occurrences of each hash tag. (action: reduceByKey)hastags = output Dstream

hashtags = lines.flatMap( lambda text : text.split(" "))
                .filter(lambda word: word.lower().startwith("#"))
                .map(lambda word: (word.lower(), 1))
                .reduceByKey( lambda a , b: a + b)

# sort the hashtags base on the counts in decreasing order             

counts_sort_dstream = hashtags.transform(lambda a:a.sortBy(lambda x: x[0].lower()).sortBy(lambda x:x[1], ascending = False) )

# print the final analysis; most popular hashtags on streaming twitter data

counts_sort_dstream.pprint()

########now starting the spark streaming
# all spark streaming code we have written till now will not execute, untill we start the ssc.
# ssc.start() will start spark streaming context. this is the action for the whole code.
# now it will create the linage & DAG & do the lazy evaluation & start running the whole sequence of code.

ssc.start()

# awaitTermination() is very important to stop the SSC.
# when we kill this python process then this signal will be sent to awaitTermination() fuction.
#  it will finally stop the spark streaming job.

ssc.awaitTermination()



