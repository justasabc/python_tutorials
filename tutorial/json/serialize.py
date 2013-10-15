# http://stackoverflow.com/questions/3768895/python-how-to-make-a-class-json-serializable


import json

class MyEncoder(json.JSONEncoder):
    	def default(self, o):
		if isinstance(o,FileItem):
        		return o.__dict__ 
        	return json.JSONEncoder.default(self, o)

def default(o):
	# for encoder
      	return o.__dict__ 

def object_hook(json_object):
	# for decoder
	if 'fname' in json_object:
       		return FileItem(json_object['fname'])

class FileItem:
	"file item class"
    	def __init__(self, fname):
        	self.fname = fname

    	def __unicode__(self):
        	return u'fname: {0}'.format(self.fname)

	def __str__(self):
		return self.__unicode__().encode('utf-8')

	def __repr__(self):
		return 'FileItem(fname=%s)' % (self.fname)

def main():
	print('-'*30)
	f = FileItem('kezunlin')
	print f.__class__
	print f.__doc__
	print f.__dict__ # {'fname':'kezunlin'}
	print '******************'
	print f
	print str(f)
	print repr(f)
       	#print f == eval(repr(f))
	print '******************'
	print 'WAY 1'
	print MyEncoder().encode(f)
	print json.dumps(f,cls=MyEncoder)
	print json.dumps(f,default=default)
	print('-'*30)
	print '******************'
	f = json.JSONDecoder(object_hook = object_hook).decode('{"fname": "/foo/bar"}')
	print f
	print '******************'
	print 'WAY 2'
	#json.JSONEncoder.default = default
        #json._default_decoder = json.JSONDecoder(object_hook = object_hook)
	f.fname ='XXXXXXXXXXXXXXX'
	#print json.dumps(f)
	#f = json.loads('{"fname": "YYYYYYYYYYYYY"}')
	#print f

if __name__=="__main__":
	main()
