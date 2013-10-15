# class nesting
"""
In fact, it is often recommended against using nested classes, since the nesting does not imply any particular relationship between the inner and outer classes.
"""

class Outer(object):
	def __init__(self):
    		self.outer_var = 1

  	def get_inner(self):
    		# "self.Inner" is because Inner is a class attribute of this class
    		return self.Inner(self)

  	class Inner(object):
    		def __init__(self, outer):
      			self.outer = outer

    		def inner_var(self):
      			return self.outer.outer_var

outer = Outer()
print outer.outer_var
inner= outer.get_inner()
print inner.inner_var()

