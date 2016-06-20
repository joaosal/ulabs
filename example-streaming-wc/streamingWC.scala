// start the shell with this command:
// spark-shell --master local[2]
//
// in a separate terminal
// nc -lkv 1234

import org.apache.spark.streaming._
import org.apache.spark.streaming.StreamingContext._
import org.apache.spark.streaming.Seconds

val ssc = new StreamingContext(sc,Seconds(5))
val mystream = ssc.socketTextStream("localhost",1234)
val words = mystream.flatMap(line => line.split("\\W"))
val wordCounts = words.map(word => (word, 1)).reduceByKey((v1,v2) => v1+v2)
wordCounts.print()

ssc.start()
ssc.awaitTermination()

