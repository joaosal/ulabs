// start the shell with this command:
// spark-shell --master local[2]

import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.StreamingContext._
import org.apache.spark.streaming.Seconds

// Configure the Streaming Context based on the shell's Spark Context 
// with a 1 second batch duration
var ssc = new StreamingContext(sc,Seconds(1))

// Create a DStream of log data from the server at localhost:1234  
val logs = ssc.socketTextStream("localhost",1234)

// Filter the DStream to only include lines containing the string “KBDOC”.
val kbreqs = logs.filter(line => line.contains("KBDOC"))

// Print out the count of each batch RDD in the stream
kbreqs.foreachRDD(rdd => println("Number of KB requests: ", rdd.count()))

// Save the filters logs
kbreqs.saveAsTextFiles("file:/home/training/exercises/kblogs/kblogs")

// Challenge: every two seconds, display the total number of KB Requests over the 
// last 10 seconds
ssc.checkpoint("logcheckpt")
kbreqs.countByWindow(Seconds(10),Seconds(2)).print()

// Start the Streaming Context and await completion of all threads
ssc.start()
ssc.awaitTermination()

