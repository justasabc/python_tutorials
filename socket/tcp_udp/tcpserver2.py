from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):

	def handle(self):
		addr = self.request.getpeername()
		print("Get connection from %s" % addr)
		self.wfile.write("Thank you for connecting")

address = ''
port = 1234
t = (address,port)
server = TCPServer(t,Handler)
print("Server is running on %s" % port)
server.serve_forever()
