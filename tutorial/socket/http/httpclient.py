#!/usr/bin/env python

import httplib
import sys
import argparse

#get http server ip
address =  '127.0.0.1'
port = 8080

parser = argparse.ArgumentParser(description='get html from server')
parser.add_argument('-a', '--address',help='set ip address')
parser.add_argument('-p', '--port',help='set port')
args = parser.parse_args()
# wrong!
#if len(args)) < 2:
#print len(sys.argv)
# python xxx.py -a 127.0.0.1 -p 8080
if len(sys.argv)<5:
	parser.print_help()
else:
	address = args.address
	port = args.port
	#create a connection
	conn = httplib.HTTPConnection(address,port)

	while 1:
	    cmd = raw_input('input command (ex. GET index.html): ')
	    cmd = cmd.split()
	
	    if cmd[0] == 'exit': #tipe exit to end it
	        break
	    #request command to server
	    conn.request(cmd[0], cmd[1])
	    #get response from server
	    rsp = conn.getresponse()
	    #print server response and data
	    print(rsp.status, rsp.reason)
	    data_received = rsp.read()
	    print(data_received)

	conn.close()
	
