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
# 18289
groupname = 'gmane.comp.python.apple'
s = NNTP(servername)

# group
'Return a tuple (response, count, first, last, name) where count is the (estimated) number of articles in the group, first is the first article number in the group, last is the last article number in the group, and name is the group name. The numbers are returned as strings.'
resp,count,first,last,name = s.group(groupname)
print('Group', name, 'has', count, 'articles, range', first, 'to', last)

# over
'Return a pair (response, overviews). overviews is a list of (article_number, overview) tuples, one for each article selected by message_spec'
resp,overviews = s.over((last-1,last))
for num,over in overviews:
	print(num)# 1-100
	#print(over)
	# print(over.keys())
	# ['xref', 'from', ':lines', ':bytes', 'references', 'date', 'message-id', 'subject']
	print(over.get('date'))
	print(nntplib.decode_header(over.get('from')))
	print(over.get('message-id'))
	print(over.get('subject'))

# stat
'Return a triple (response, number, id) where number is the article number and id is the message id.'
resp,num,msg_id = s.stat(last)
print(num,msg_id)

# article
'Return a tuple (response, info) where info is a namedtuple with three attributes number, message_id and lines (in that order).'
print('-'*10)
resp,info = s.article(last)
print(info.number,info.message_id,len(info.lines))

# head
'Same as article(), but sends a HEAD command. The lines returned (or written to file) will only contain the message headers, not the body.'
print('-'*10)
resp,info = s.head(last)
print(info.number,info.message_id,len(info.lines))

# body
'Same as article(), but sends a BODY command. The lines returned (or written to file) will only contain the message body, not the headers.'
print('-'*10)
resp,info = s.body(last)
print(info.number,info.message_id,len(info.lines))

# newgroups
'Return a pair (response, groups) where groups is a list of group names that are new since the given date and time'
#resp,groups = s.newgroups(date,time)
#print len(groups)
#pprint(groups)

#newnews
'Return a pair (response, articles) where articles is a list of message idsThis command is frequently disabled by NNTP server administrators.'
#resp,ids = s.newnews(groupname,date,time)
