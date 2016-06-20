#!/usr/bin/env python

# Step 1 - create an RDD of integers
mydata = sc.parallelize([1,2,3,4,5])

# Step 2 - loop 200 times
for i in range(200): 
    mydata = mydata.map(lambda myInt: myInt + 1)

# Step 3 - collect and display the data in the RDD
for x in mydata.collect(): print x

# Step 4 - show the final RDD
mydata.toDebugString()

# Steps 5,6 - repeat steps 2 - 4 above until you receive and error

# Note: The steps above demonstrated the error without checkpointing
# The steps below are a simple program to iteratively create child RDDs 
# from parent RDDs. Use iPython %paste to run.

# Step 9 - enable checkpointing.
sc.setCheckpointDir("checkpoints")

# Step 10 - create an RDD of integers
mydata = sc.parallelize([1,2,3,4,5])

# Steps 11, 12 - Iterate to generate a new RDD which descends from prior RDDs
# resulting in a long lineage
for i in range(1000):
   mydata = mydata.map(lambda myInt: myInt + 1)
   print "Iteration",i
   # Every 10 iterations, checkpoint the RDD, and materialize it to save the checkpoint file
   # shorten the lineage
   if i % 10 == 0: 
       print "Checkpoint"
       mydata.checkpoint()
       mydata.count()

# Step 13 - collect the contents of the RDD to an array and display
for x in mydata.collect(): print x
     
# Step 14 -  Display the lineage (formatted)
for rddstring in mydata.toDebugString().split('\n'): print rddstring.strip()

