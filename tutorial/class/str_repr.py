# http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python

# http://stackoverflow.com/questions/6005159/when-to-use-r-instead-of-s-in-python
"""
__repr__: representation of python object usually eval will convert it back to that object
obj = eval(repr(obj))

__str__: is whatever you think is that object in text form

print str(object)
"""
import datetime

d = datetime.date.today()
print str(d)
#'2011-05-14'
print repr(d)
#'datetime.date(2011, 5, 14)'
print d == eval(repr(d))
