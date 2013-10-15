# http://stackoverflow.com/questions/3768895/python-how-to-make-a-class-json-serializable


import json

class FileItem:
	"file item class"
    	def __init__(self, fname):
        	self.fname = fname

    	def __unicode__(self):
        	return u'fname: {0}'.format(self.fname)

	def __str__(self):
		return self.__unicode__().encode('utf-8')

	def __repr__(self):
		return json.dumps(self.__dict__)

	def jsonify(self):
		return json.dumps(self.__dict__,indent=4)

	@classmethod
	def unjsonify(cls,json_object):
		dt = json.loads(json_object)	
		f = cls(dt.get('fname'))
		return f

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
	json_object= f.jsonify()
	print json_object
	print '******************'
	f2 = FileItem.unjsonify(json_object)
	print type(f2)
	print f2
	print str(f2)
	print repr(f2)
	print '******************'

if __name__=="__main__":
	main()
