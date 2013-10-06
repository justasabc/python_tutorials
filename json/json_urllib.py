import json
import urllib2

url = "http://date.jsontest.com/"
f = urllib2.urlopen(url)
python_data = json.load(f)
print(python_data)
