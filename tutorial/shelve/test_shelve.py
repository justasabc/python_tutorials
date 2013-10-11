import shelve

def create_data():
	try:
		db = shelve.open('db.dat','c')
		db['name']= 'kezunlin'
		db['age']=24
		db['x']=['a','b','c']
		# writeback
		temp = db['x']
		temp.append('d')
		db['x'] = temp
		db.close()
	except Exception,e:
		print(e)

def load_data():
	try:
		db = shelve.open('db.dat','r')	
		for item in db.iteritems():
			print item
		db.close()
	except Exception,e:
		print(e)

def main():
	create_data()
	load_data()

if __name__=='__main__':
	main()
