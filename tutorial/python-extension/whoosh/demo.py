#!/usr/bin/python
import os
from whoosh import index
from whoosh.fields import *
from whoosh.qparser import QueryParser

head,tail = os.path.split('files/1.txt')
head = os.path.dirname('files/1.txt')
tail = os.path.basename('files/1.txt')

def list_all_files(rootdir):
	"""
	list all flies in rootdir recursively
	return filepath list
	"""
	allfiles = []
	for root,subFolders,files in os.walk(rootdir):
		for filename in files:
			filepath = os.path.join(root,filename)
			allfiles.append(filepath)
	return allfiles

"""
TEXT: indexed, not stored  (stored=True)
KEYWORD: indexed, not stored (stored=True,lowercase=True,commas=True,scorable=True)
ID: indexed,not stored (stored=True,unique=True)
	used for url or path
	The ID field type simply indexes (and optionally stores) the entire value of the field as a single unit (that is, it doesn’t break it up into individual terms)
	Use ID for fields like url or path (the URL or file path of a document), date, category – fields where the value must be treated as a whole, and each document only has one value for the field.
STORED: stored,not indexed
	This field is stored with the document, but not indexed and not searchable. This is useful for document information you want to display to the user in the search results, but don’t need to be able to search for.

whoosh.fields.NUMERIC
    This field stores int, long, or floating point numbers in a compact, sortable format.
whoosh.fields.DATETIME
    This field stores datetime objects in a compact, sortable format.
whoosh.fields.BOOLEAN
    This simple filed indexes boolean values and allows users to search for yes, no, true, false, 1, 0, t or f.
"""
def get_schema():
	"""
	return default schema
	"""
	return Schema(title=TEXT(stored=True),path=ID(unique=True,stored=True),time=STORED,content=TEXT,tags=KEYWORD(stored=True))

class MySchema(SchemaClass):
	title=TEXT(stored=True)
	path=ID(unique=True,stored=True)
	time=STORED
	content=TEXT
	tags=KEYWORD(stored=True)

def add_file_to_index(writer,filepath):
	"""
	add filepath to index
	"""
	mtime = os.path.getmtime(filepath)
	file_title = os.path.basename(filepath)
	file_content= open(filepath,'rb').read()
	# fields to be indexed must be unicode
	writer.add_document(title=unicode(file_title),path=unicode(filepath),time=mtime,content=unicode(file_content))

def clean_index(index_dir,root_dir):
	"""
	Always create the index from strach
	index_dir: dir to save index infos
	root_dir: dir of all files to be indexed
	"""
	#ix = create_index(index_dir,get_schema())
	if not os.path.exists(index_dir):
		os.mkdir(index_dir)
	# create_in: if index exist,then clear it first and finally create it
	# create_in: otherwise, just create it
	ix = index.create_in(index_dir,schema= get_schema())
	writer = ix.writer()
	for filepath in list_all_files(root_dir):
		add_file_to_index(writer,filepath)
	writer.commit()

def incremental_index(index_dir,root_dir):
	"""
	Only re-index the documents that have changed
	index_dir: dir to save index infos
	root_dir: dir of all files to be indexed
	"""
	if not os.path.exists(index_dir):
		os.mkdir(index_dir)
	index_exist = index.exists_in(index_dir)
	if not index_exist:
		print('index not exist, create it')
		ix = index.create_in(index_dir,schema=get_schema())

	ix = index.open_dir(index_dir)
	# all paths in the index
	indexed_paths = set()
	# all paths we need to re-index
	to_reindex_paths = set()

	with ix.searcher() as searcher:
		writer = ix.writer()
		
		# Loop over the stored fileds in the index
		for fields in searcher.all_stored_fields():
			indexed_path = fields['path']
			indexed_paths.add(indexed_path)	

			if not os.path.exists(indexed_path):
				# This file was deleted since it was indexed
				# So delete from the index
				writer.delete_by_term('path',indexed_path)
			else:
				# Check if this file was changed since it was indexed
				indexed_time = fields['time']
				mtime = os.path.getmtime(indexed_path)
				if mtime > indexed_time:
					# This file has changed since it was indexed
					# So delete from the index
					writer.delete_by_term('path',indexed_path)
					# And add it to the list of files to reindex
					to_reindex_paths.add(indexed_path)

		# Loop over the files in the filesystem
		for filepath in list_all_files(root_dir):
			if filepath not in indexed_paths:
				# This is a new file, so indexed it
				add_file_to_index(writer,filepath)
				print('{0} is a new file'.format(filepath))
			elif filepath in to_reindex_paths:
				# This is file that's changed, so indexed it
				add_file_to_index(writer,filepath)
				print('{0} is a changed file'.format(filepath))
			else:
				# This file has not changed since it was indexed
				print('{0} not changed'.format(filepath))
				pass
		writer.commit()

def index_files(index_dir,root_dir,clean=False):
	"""
	index files
	"""
	if clean:
		clean_index(index_dir,root_dir)
	else:
		incremental_index(index_dir,root_dir)

def search_files(index_dir,content):
	"""
	search file content in index 
	if not hit: return False
	if hit: return results
	"""
	index_exist = index.exists_in(index_dir)
	if not index_exist:
		print('index not exist')
		return False
	ix = index.open_dir(index_dir)
	content = unicode(content)
	with ix.searcher() as searcher:
		parser = QueryParser('content',ix.schema)
		query = parser.parse(content)
		# whoosh.searching.Results
		results = searcher.search(query)
		print(type(results))
		l = len(results)
		print l
		for h in results:
			# whoosh.searching.Hit
			print type(h)
			print h
		return results
	return False

def search_files2(index_dir,content):
	"""
	search file content in index 
	if not hit: return False
	if hit: return results
	"""
	index_exist = index.exists_in(index_dir)
	if not index_exist:
		return False
	ix = index.open_dir(index_dir)
	content = unicode(content)
	with ix.searcher() as searcher:
		parser = QueryParser('content',ix.schema)
		query = parser.parse(content)
		results = searcher.search(query)
		return results
	return False

index_dir = 'indexdir'
root_dir = 'files'

def test_1():
	index_files(index_dir,root_dir,True)
	rtn = search_files(index_dir,'first')
	if rtn == False:
		pass
	else:
		print('-'*30)
		print(len(rtn))
		print(rtn)
		for r in rtn:
			# WRONG! Because searcher has been closed
			#print(r)
			pass

def test_2():
	index_files(index_dir,root_dir,False)
	rtn = search_files(index_dir,'first')
	if rtn == False:
		pass
	else:
		print('-'*30)
		print(len(rtn))
		print(rtn)
		for r in rtn:
			# WRONG! Because searcher has been closed
			#print(r)
			pass

def main():
	#test_1()
	test_2()

if __name__=="__main__":
	main()

