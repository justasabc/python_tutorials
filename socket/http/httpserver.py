#!/usr/bin/env python

#from SimpleHTTPServer import SimpleHTTPRequestHandler as HandlerClass
#from BaseHTTPServer import HTTPServer as ServerClass

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

# myhandler
class myhandler(BaseHTTPRequestHandler):

    #handle GET command
    def do_GET(self):
        rootdir = './html/' #file location

        try:
			#Check the file extension required and set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(rootdir + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return
            
        except IOError:
		self.send_error(404, 'file not found: %s' % self.path)
    
def run():
    print('http server is starting...')

    #ip and port of servr
    #by default http server port is 80 
    # use port lower than 1024 will cause an error!
# It might be possible that you are trying to run on a port the current user account does not have permission to bind to. This could be port 80 or something. Try increasing the portnumber or use a user with sufficient privileges.
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, myhandler)

    sa = httpd.socket.getsockname()
    print('http server is running on %s port %s...' % (sa[0],sa[1]))
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()


