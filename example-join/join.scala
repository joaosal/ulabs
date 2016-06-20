// Step 1 - create an RDD based on all the weblogs
var logs=sc.textFile("/loudacre/weblogs/*6.log")

// map each request (line) to a pair (userid, 1) then sum the hits
val userreqs = logs. 
   map(line => line.split(' ')).
   map(words => (words(2),1)).  
   reduceByKey((v1,v2) => v1 + v2)
   
// Step 2 - return a user count for each hit frequency
val freqcount = userreqs.map(pair => (pair._2,pair._1)).countByKey()

// Step 3 - Group IPs by user ID
val userips = logs. 
    map(line => line.split(' ')).
    map(words => (words(2),words(0))).
    groupByKey()
// print out the first 10 user ids, and their IP list
for (pair <- userips.take(10)) {
   println(pair._1 + ":")
   for (ip <- pair._2) println("\t"+ip)
}

// Step 4a - map account data to (userid,[values....])
val accountsdata = "/loudacre/accounts.csv"
val accounts = sc.textFile(accountsdata).
   map(line => line.split(',')).
   map(account => (account(0),account))
   
// Step 4b - Join account data with userreqs then merge hit count into valuelist   
val accounthits = accounts.join(userreqs)

// Step 4c - Display userid, hit count, first name, last name for the first few elements
for (pair <- accounthits.take(10)) {
   printf("%s, %s, %s, %s\n",pair._1,pair._2._2, pair._2._1(3),pair._2._1(4))
}

// Bonus exercises   
// key accounts by postal/zip code
var accountsByPCode = sc.textFile(accountsdata).map(_.split(',')).keyBy(_(8))
 
// map account data to lastname,firstname  
var namesByPCode = accountsByPCode.mapValues(values => values(4) + ',' + values(3)).groupByKey()

// print the first 5 zip codes and list the names 
for (pair <- namesByPCode.sortByKey().take(5)) {
   println("---" + pair._1)
   pair._2.foreach(println)
}

