import requests
r = requests.get("http://baidu.com")
r = requests.get("http://httpbin.org")
r = requests.post("http://httpbin.org/post")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")
r.status_code
r.text
r.encoding
r.content

# passing parameters in urls
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print r.url


r = requests.get("http://book.zi5.me/books/detail/100")
r.text # html source code
r.content


"""
u = urllib2.urlopen("http://www.chinanews.com/tp/hd2011/2013/07-04/220870.shtml")
lf = open('1.shtml','w')
lf.write(u.read())
lf.close()
"""
