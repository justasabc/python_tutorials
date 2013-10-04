from SimpleXMLRPCServer import SimpleXMLRPCServer
import socket

SimpleXMLRPCServer.allow_reuse_address = 1
PORT = 12345
quit = False
def start():
	global PORT
	try:
		t = ('',PORT)
		s = SimpleXMLRPCServer(t,allow_none=True)
		def twice(x):
			return x*2
		def hello():
			return None
		s.register_function(twice)
		s.register_function(hello)
		print('Server is running on port {0}...'.format(PORT))
		s.serve_forever()
		# while not quit:
			#s.handle_request()
		# s.shutdown()
	except socket.error,e:
		#print 'socket error'
		#print e
		# address in use,so change another port
		PORT = PORT + 1
		start()
	except Exception,e:
		print 'excpetion'
		print e

if __name__ == "__main__":
	start()
