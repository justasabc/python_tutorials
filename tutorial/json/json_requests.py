import json
import requests
from pprint import pprint

url = "http://date.jsontest.com/"
r = requests.get(url)
print(r.status_code)
print(r.url)
print(r.encoding)
print(r.headers)
print(r.content)
print(r.text)
print('-'*20)
json_data = r.json()
pprint(json_data)
d = json_data.get('date')
t = json_data.get('time')
print d,t
