#!/usr/bin/env python

import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

def printRDDcount(rdd): print "Number of KB requests: "+str(rdd.count())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: StreamingLogs <hostname> <port>"
        exit(-1)
    
    hostname = sys.argv[1]
    port = int(sys.argv[2])
     
    sc = SparkContext()   
    
    # Configure the Streaming Context with a 1 second batch duration
    ssc = StreamingContext(sc,1)

    # Create a DStream of log data from the server at hostname:port  
    logs = ssc.socketTextStream(hostname,port)

    # Filter the DStream to only include lines containing the string KBDOC
    kbreqs = logs.filter(lambda line: "KBDOC" in line)

    # Print out the count of each batch RDD in the stream
    kbreqs.foreachRDD(lambda t,r: printRDDcount(r))

    # Save the filters logs
    kbreqs.saveAsTextFiles("logoutput/kblogs")

    # Bonus: every two seconds, display the total number of KB Requests over the 
    # last 10 seconds
    ssc.checkpoint("logcheckpt")
    kbreqs.countByWindow(10,2).pprint()
    
    ssc.start()
    ssc.awaitTermination()
    sc.stop()

