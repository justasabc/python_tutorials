# http://stackoverflow.com/questions/308999/what-does-functools-wraps-do
# http://stackoverflow.com/questions/1782843/python-decorator-problem-with-docstrings/1782888#1782888
# http://docs.python.org/2/library/functools.html#functools.wraps

def logged(f):
    def with_logging(*args, **kwargs):
        print f.__doc__ + " is docstring"
        print f.__name__ + " was called"
        return f(*args, **kwargs)
    return with_logging

@logged
def f(x):
	"does some math"
	return x*x
#print f(5)
print f.__name__ # with_logging
print f.__doc__ # None

# equal to the following
def f2(x):
	"does some math"
	return x*x

f2 = logged(f2)
#print f2(5)
print f2.__name__ # with_logging
print f2.__doc__ # None


# solution to save __name__ __doc__ etc.
from functools import wraps

def logged3(f):
	@wraps(f)
    	def with_logging(*args, **kwargs):
        	print f.__doc__ + " is docstring"
        	print f.__name__ + " was called"
        	return f(*args, **kwargs)
    	return with_logging

@logged3
def f3(x):
	"does some math"
	return x*x
#print f3(5)
print f3.__name__ # f3
print f3.__doc__ # does some math
