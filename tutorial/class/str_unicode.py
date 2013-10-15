# http://stackoverflow.com/questions/1307014/python-str-versus-unicode

class Person():

	def __init__(self,name,age):
		self.name = name
		self.age = age

	def __unicode__(self):
		# return characters
		print 'unicode'
		return u'{0} {1}'.format(self.name,self.age)

	def __str__(self):
		# return bytes
		# encode: unicode--->str
		# decode: str--->unicode
		print 'str'
		return self.__unicode__().encode('utf-8')

def main():
	p = Person('kezunlin',24)
	print p

main()
