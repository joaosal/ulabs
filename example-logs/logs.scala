val mydata = sc.textFile("user/hdfs/ulabs/data/frostroad.txt")
mydata.count()
mydata.collect()

val logfile = "/user/hdfs/data/weblogs/weblogs/2013-09-15.log"
val log = sc.textFile(logfile)

val  jpglog = log.filter(line => line.contains(".jpg"))
jpglog.take(10)

jpglog.count()

log.map(_.length).take(5)

log.map(_.split(' ')).take(5)

val ip = log.map(_.split(' ')(0))

ip.take(5)

ip.take(5).foreach(println)

ip.saveAsTextFile("/user/hdfs/scala/iplist")

// Loading all weblogs IP / UserID

val logfiles = "/user/hdfs/data/weblogs/weblogs/"
val logs = sc.textFile(logfiles)
val htmllogs = logs.filter(_.contains(".html")).map(line => (line.split(' ')(0), line.split(' ')(2)))

htmllogs.take(10).foreach(t => println(t._1 + "/" + t._2))

