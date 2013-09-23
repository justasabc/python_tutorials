from urllib import urlopen,urlretrieve
page = urlopen('http://python.org/')
text = page.read()
#print(text)
urlretrieve("http://python.org","python.html")
