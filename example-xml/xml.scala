import xml.etree.ElementTree as ElementTree

# Given a string containing XML, parse the string, and 
# return an iterator of activation XML records (Elements) contained in the string

def getactivations(s):
    filetree = ElementTree.fromstring(s)
    return filetree.getiterator('activation')
    
# Given an activation record (XML Element), return the model name
def getmodel(activation):
    return activation.find('model').text 

# Given an activation record (XML Element), return the account number 
def getaccount(activation):
    return activation.find('account-number').text 

# Exercise solution
# Read XML files into an RDD 
files="/user/hdfs/xml/activations/*.xml"
activationFiles = sc.wholeTextFiles(files)

# Parse each file (as a string) into a collection of activation XML records
activationRecords = activationFiles.flatMap(lambda (filename,xmlstring): getactivations(xmlstring))

# Map each activation record to "account-number:model-name"
models = activationRecords.map(lambda record: getaccount(record) + ":" + getmodel(record))

# Save the data to a file
models.saveAsTextFile("/user/hdfs/xml/account-models")
