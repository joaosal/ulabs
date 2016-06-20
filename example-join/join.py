#!/usr/bin/env python

# Step 1 - Create an RDD based on a subset of weblogs (those ending in digit 6)
logs=sc.textFile("/loudacre/weblogs/*6.log")
# map each request (line) to a pair (userid, 1), then sum the values
userreqs = logs \
   .map(lambda line: line.split()) \
   .map(lambda words: (words[2],1))  \
   .reduceByKey(lambda count1,count2: count1 + count2)
   
# Step 2 - Show the count frequencies
freqcount = userreqs.map(lambda (userid,freq): (freq,userid)).countByKey()
print freqcount

# Step 3 - Group IPs by user ID
userips = logs \
   .map(lambda line: line.split()) \
   .map(lambda words: (words[2],words[0])) \
   .groupByKey()
# print out the first 10 user ids, and their IP list
for (userid,ips) in userips.take(10):
   print userid, ":"
   for ip in ips: print "\t",ip

# Step 4a - Map account data to (userid,[values....])
accountsdata = "/loudacre/accounts.csv"
accounts = sc.textFile(accountsdata) \
   .map(lambda s: s.split(',')) \
   .map(lambda account: (account[0],account))

# Step 4b - Join account data with userreqs then merge hit count into valuelist   
accounthits = accounts.join(userreqs)

# Step 4c - Display userid, hit count, first name, last name for the first 5 elements
for (userid,(values,count)) in accounthits.take(5) : 
    print  userid, count, values[3],values[4]
   
# Bonus Exercise
# key accounts by postal/zip code
accountsByPCode = sc.textFile(accountsdata) \
   .map(lambda s: s.split(','))\
   .keyBy(lambda account: account[8])
 
# map account data to lastname,firstname  
namesByPCode = accountsByPCode\
   .mapValues(lambda account: account[4] + ',' + account[3]) \
   .groupByKey()

# print the first 5 zip codes and list the names 
for (pcode,names) in namesByPCode.sortByKey().take(5):
   print "---" ,pcode
   for name in names: print name
