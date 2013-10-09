import socket
import os
import sys

MIN_PORT = 1
MAX_PORT = 65535
WELL_KNOWN = 1024

def increase_byone(ip):
	"""
	increase a given ip by 1
	for example: 192.168.1.199->192.168.1.200
		     192.168.1.255->192.168.2.0
	"""
	ip = ip.split(".")
	d = int(ip[3])+1
	c = int(ip[2])
	b = int(ip[1])
	a = int(ip[0])
	if(d==256):
		c = c+1
		d=0
		if(c==256):
			b= b+1
			c=0
			if(b==256):
				a=a+1
				b=0
				if(a==256):
					sys.stderr.write("ERROR >__>")
	return "{0}.{1}.{2}.{3}".format(a,b,c,d)

def single_scan(ip,maxport):
	"""
	scan a given ip to find port that is opened
	"""
	ports = []
	for p in range(maxport+1):
		if check_port(ip,p):
			ports.append(p)
			print(p)
	return ports

def range_scan(ip,numComputers=1,maxport =MAX_PORT):
	"""
	scan from ip and its continuous n computers
	"""
	ip_ports ={}
	count = 0
	while count<numComputers:
		print('-'*30)
		if ip_exist(ip):
			print("Ports at {0}".format(ip))
			ports = single_scan(ip,maxport)
			ip_ports[ip]=ports
		count +=1
		ip = increase_byone(ip)
	return ip_ports

		
def main():
	clear_screen()
	ip = "192.168.1.197"
	num = 10
	print('range_scan from {0} with {1} computers'.format(ip,num))
	range_scan(ip,num,WELL_KNOWN)

if __name__=="__main__":
	main()

