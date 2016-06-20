#!/usr/bin/env python

logfile = "/user/hdfs/data/weblogs/weblogs/2013-09-15.log"
log = sc.textFile(logfile)

jpglog = log.filter(lambda x: ".jpg" in x)
jpglog.take(10)
jpglog.count()

log.map(lambda s: len(s)).take(5)

log.map(lambda s: s.split()).take(5)

ip = log.map(lambda s: s.split()[0])
ip.take(5)

for x in ip.take(5) : print x

ip.saveAsTextFile("/user/hdfs/python/iplist")

# All logs

logfiles = "/user/hdfs/data/weblogs/weblogs/"
logs = sc.textFile(logfiles)
htmllogs=logs.filter(lambda s: ".htm" in s).map(lambda s: (s.split()[0],s.split()[2]))
for x in htmllogs.take(10): print x[0]+"/"+x.[1]
