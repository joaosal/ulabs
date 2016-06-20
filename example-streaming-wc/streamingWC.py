#!/usr/bin/env python

# start the shell with this command:
# pyspark --master local[2]
#
# in a separate terminal
# nc -lkv 1234

from pyspark.streaming import StreamingContext

ssc = StreamingContext(sc,5)
mystream = ssc.socketTextStream("localhost",1234)
words = mystream.flatMap(lambda line: line.split())
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda v1,v2: v1+v2)
wordCounts.pprint()

ssc.start()
ssc.awaitTermination()
