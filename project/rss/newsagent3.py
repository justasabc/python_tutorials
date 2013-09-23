from pprint import pprint
import nntplib
from nntplib import NNTP
from time import strftime,time,localtime
import re
import urllib.request 
day = 24*60*60

class NewsItem:
	"""
	news item containing title and body
	"""
	def __init__(self,title,body):
		self.title = title
		self.body = body

class NNTPSource:
	"""
	the nntp source
	"""
	def __init__(self,servername,groupname,window):
		self.servername = servername
		self.groupname = groupname
		self.window = window
	
	def getItems(self):
	#	yesterday = localtime(time()-self.window*day)
	#	date = strftime('%y%m%d',yesterday)
	#	time = strftime('%H%M%S',yesterday)
		# create a nntp server
		s = NNTP(self.servername)	
		resp,count,first,last,name = s.group(self.groupname)
		resp,overviews = s.over((last-1,last))
		for num,over in overviews:
			title = over.get('subject')
			resp,body = s.body(num)
			# create a generator to iterate news 
			if title and body:
				yield NewsItem(title,body)
		s.quit()	

class SimpleWebSource:
	"""
	simple web source
	"""
	def __init__(self,url,titlePattern,bodyPattern):
		self.url = url
		self.titlePattern = re.compile(titlePattern)
		self.bodyPattern = re.compile(bodyPattern)

	def getItems(self):
		text = urllib.request.urlopen(self.url).read()
		titles = self.titlePattern.findall(text)
		bodies = self.bodyPattern.findall(text)
		for title,body in zip(titles,bodies):
			if title and body:
				yield NewsItem(title,body)

class HTMLDestination:
	"""
	html destination
	"""
	def __init__(self,filename):
		self.filename = filename

	def receiveItems(self,items):
		# print >> file, "xxx"
		out = open(self.filename,'w')
		out.write("""
		<html>
			<head>
				<title>Today's news</title>
			</head>
			<body>
				<h1>Today's news</h1>
		""")
		out.write('<ul>')
		id = 0
		for item in items:
			id +=1
			#print(id, item.title,item.body)
			#print('-'*100)
			out.write("<li><a href=\"#{0}\">{1}</a></li>".format(id,item.title))
		out.write('</ul>')

		id = 0
		for item in items:
			id +=1
			out.write("<h2><a name=\"#{0}\">{1}</a></h2>".format(id,item.title))
			out.write("<pre>{0}</pre>".format(item.body))
		out.write("""
			</body>
		</html>
		""")

class PlainDestination:
	"""
	output to plain text
	"""
	def receiveItems(self,items):
		for item in items:
			print(item.title)
			print('-'*len(item.title))
			print(item.body)

class NewsAgent:
	"""
	core class. get news items from sources and output to destinations
	"""
	def __init__(self):
		self.sources = []
		self.destinations = []

	def addSource(self,source):
		self.sources.append(source)

	def addDestination(self,dest):
		self.destinations.append(dest)

	def distribute(self):
		"""	
		distribute news from source to destination
		"""
		items = []
		for source in self.sources:
			items.extend(source.getItems())
		for dest in self.destinations:
			dest.receiveItems(items)


def runDefaultSetup():
	agent = NewsAgent()
	# source from nntp
	servername = 'news.gmane.org'
	groupname = 'gmane.comp.python.apple'
	window = 7
	nntp_src = NNTPSource(servername,groupname,window)
	# plain text destination
	plain_dest = PlainDestination()

	# source from web
	url = 'http://www.google.com'
	titlePattern = b'<a\s*href=[\'|"](.*?)[\'"].*?>'
	bodyPattern = b'<a\s*href=[\'|"](.*?)[\'"].*?>'
	web_src = SimpleWebSource(url,titlePattern,bodyPattern)
	# html destination
	html_dest = HTMLDestination('mynews.html')

	# add source and destination
	#agent.addSource(nntp_src)
	agent.addSource(web_src)
	#agent.addDestination(plain_dest)
	agent.addDestination(html_dest)
	# distribute news items
	agent.distribute()

def main():
	runDefaultSetup()
	
if __name__ == '__main__':
	main()
