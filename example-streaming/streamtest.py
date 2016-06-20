#!/usr/bin/env python
# Parameters:
#     host: the host name or IP to bind to (e.g. localhost)
#     port: the port to listen on
#     lines-per-second: how fast to send the data
#     files: one or more files (e.g. datadirectory/*)
#
# Note: script makes no attempt to recover from a broken connection; restart the script.

import sys
import time
import socket

if __name__ == "__main__":
  if len(sys.argv) < 4:
    print >> sys.stderr, "Usage: streamtest <host> <port> <lines-per-second> <files>"
    exit(-1)

  host = sys.argv[1]
  port = int(sys.argv[2])
  sleeptime = 1/float(sys.argv[3])
  filelist = sys.argv[4:]
  
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.bind((host,port))
  serversocket.listen(1)

  while(1):
    print "Waiting for connection on",host,":",port
    (clientsocket,address) = serversocket.accept()
    print "Connection from",address
    for filename in filelist: 
      print "Sending",filename
      for line in open(filename): 
        print line
        clientsocket.send(line)
        time.sleep(sleeptime)

