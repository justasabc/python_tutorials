from pprint import pprint
import nntplib
from nntplib import NNTP
from time import strftime,time,localtime
day = 24*60*60
window = 7
yesterday = localtime(time()-window*day)
date = strftime('%y%m%d',yesterday)
time = strftime('%H%M%S',yesterday)

servername = 'news.gmane.org'
groupname = 'gmane.comp.python.apple'
s = NNTP(servername)

resp,count,first,last,name = s.group(groupname)

resp,overviews = s.over((last-1,last))
for num,over in overviews:
	print(num)# 1-100
	# print(over.keys())
	# ['xref', 'from', ':lines', ':bytes', 'references', 'date', 'message-id', 'subject']
	'''
	resp,h = s.head(num)
	for line in h.lines:
		print(type(line)) # bytes
		print(line)
	'''
	resp,b = s.body(num)
	sj = over.get('subject')
	dt = over.get('date')
	print(dt)
	print(sj)
	print('-'*len(sj))
	#pprint(b)

