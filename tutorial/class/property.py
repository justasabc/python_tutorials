# refs
# http://www.ibm.com/developerworks/cn/opensource/os-pythondescriptors/

"""
string.title:  "hello world"--->"Hello World"
"""

# 1  __get__ __set__ __delete__
class Descriptor(object):

    def __init__(self):
        self._name = ''

    def __get__(self, instance, owner):
        print "Getting: %s" % self._name
        return self._name

    def __set__(self, instance, name):
        print "Setting: %s" % name
        self._name = name.title()

    def __delete__(self, instance):
        print "Deleting: %s" %self._name
        del self._name

class Person(object):
	name = Descriptor()

def test_person():
	p = Person()
	print p.__dict__
	p.name = "hello world"
	print p.name
	del p.name

# 2 fget fset fdel
class Person2(object):
    def __init__(self):
        self._name = ''

    def fget(self):
        print "Getting: %s" % self._name
        return self._name
    
    def fset(self, value):
        print "Setting: %s" % value
        self._name = value.title()

    def fdel(self):
        print "Deleting: %s" %self._name
        del self._name

    name = property(fget, fset, fdel, "I'm the property.")
    #name = property(fget, None, fdel, "I'm the property.")
    # name='xxx' will raise AttributeError because there is no fset method

def test_person2():
	p = Person2()
	print p.__dict__
	p.name = "xxx yyy"
	print p.name
	del p.name

# 3 @property
class Person3(object):

    def __init__(self):
        self._name = ''

    @property
    def name(self):
        print "Getting: %s" % self._name
        return self._name

    @name.setter
    def name(self, value):
        print "Setting: %s" % value
        self._name = value.title()

    @name.deleter
    def name(self):
        print ">Deleting: %s" % self._name
        del self._name

def test_person3():
	p = Person3()
	print p.__dict__
	p.name = "ttt"
	print p.name
	del p.name

# dynamic create property
class DynamicPerson(object):

    def addProperty(self, attribute):
        # create local setter and getter with a particular attribute name 
        setter = lambda self, value: self._setProperty(attribute, value)
        getter = lambda self: self._getProperty(attribute)

        # construct property attribute and add it to the class
        setattr(self.__class__, attribute, property(fget=getter, \
                                                    fset=setter, \
                                                    doc="Auto-generated method"))

    def _setProperty(self, attribute, value):
        print "Setting: %s = %s" %(attribute, value)
        setattr(self, '_' + attribute, value.title())    

    def _getProperty(self, attribute):
        print "Getting: %s" %attribute
        return getattr(self, '_' + attribute)

def test_dynamic_persion():
	p = DynamicPerson()
	p.addProperty('name')
	p.addProperty('phone')
	p.name = 'AAA'
	print p.name
	p.phone = '12345'
	print p.phone
	print p.__dict__

def main():
	print "test_person"
	test_person()
	print "test_person2"
	test_person2()
	print "test_person3"
	test_person3()
	print "test_dynamic_persion"
	test_dynamic_persion()

if __name__=="__main__":
	main()

