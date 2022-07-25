#!/usr/bin/env python

import SocketServer
import socket
import threading
import re

#import PyYadd
#import pysql
import time



def write_file(text):
    filename = "logfile.txt"
    f = open(filename, 'a+')
    #timenow = time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(time.time()))
    log = " ".join((text, "\r\n"))
    f.write(log)
    f.close()

  
    
class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):
   

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        

 #       pysql.load_logger("UDP", "%s : %s" % (data.split(";")[0][1:-1], self.client_address[0]))
        
  #      self.dsc_list = self.make_dsc(data)
        print data
        write_file(data)
    



 
class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass

if __name__ == "__main__":
    #pysql.load_logger("yUDPSERV", "Starting YaDD UDP interface....")
    HOST, PORT = "", 2505

    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)
    ip, port = server.server_address
    server.serve_forever()
    # Start a thread with the server -- 
	# that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    server.shutdown()
