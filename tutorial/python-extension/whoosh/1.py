from whoosh.index import create_in,open_dir
from whoosh.fields import *
import os

schema = Schema(title=TEXT(stored=True),path=ID(stored=True),
		content=TEXT,tags=KEYWORD,icon=STORED)

if not os.path.exists("indexdir"):
	os.mkdir("indexdir")
ix = create_in('indexdir',schema)
#ix = open_dir('indexdir')

writer = ix.writer()
writer.add_document(title=u'1 document',path=u'1.txt',content=u'This is the first document we have added!',tags=u'first short')
writer.add_document(title=u'2 document',path=u'2.txt',content=u'This is the second document we have added!',tags=u'second short')
writer.commit()

from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
	parser = QueryParser('content',ix.schema)
	query = parser.parse(u'added')
	results = searcher.search(query)
	print len(results)
	for r in results:
		print r

# query
query = parser.parse(u'added')
print(query)

query = parser.parse(u'added*')
print(query)

query = parser.parse(u'added deleted updated')
print(query)

query = parser.parse(u'added deleted OR (title:xxx keyword:yyy)')
print(query)

from whoosh.query import *
query = And([Term('content',u'apple'),Term('content','orange')])
print(query)

# calling create_in for 2 times will clear the index
#ix = create_in('indexdir',schema)
