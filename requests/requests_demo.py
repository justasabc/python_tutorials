import requests
import json

# 1 GET
# get 
r = requests.get("http://www.baidu.com")
print(r.status_code)
# status_code
print(requests.codes.ok)
print(r.url)
print(r.encoding)
print(r.apparent_encoding)
print(r.headers)
#print(r.text) # text data
#print(r.content) # binary data

# passing parameters in urls
# get params 
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)
print('-'*40)
print(r.text)
print('-'*40)
# get json()
print(r.json())# json response content
print('-'*40)

# get cookies
url = "http://httpbin.org/cookies"
cookies ={'username':'justasabc','age':'24'}
r =requests.get(url,cookies=cookies)
print(r.text)

# 2 POST 
# post data headers
# custom headers
url ="https://httpbin.org/post"
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type':'application/json'}
r = requests.post(url,data=json.dumps(payload),headers=headers)
print('---request headers---')
# request.headers
print(r.request.headers)
print(r.request.headers['content-type']) # application/json
print('---response headers---')
print(r.headers)
# HTTP Headers are case-insensitive.
print(r.headers['Content-Type']) # application/json
print(r.headers['content-type']) # application/json
print(r.text)
print('-'*40)

# post data
r = requests.post(url,data=payload)
print('---request headers---')
print(r.request.headers)
print(r.request.headers['content-type']) # application/x-www-form-urlencoded
print('---response headers---')
print(r.headers)
print(r.headers['content-type']) # application/json
print(r.text)

# 3 HEAD
print('-'*40)
r = requests.head("http://www.baidu.com")
print(r.status_code)
print('---request headers---')
print(r.request.headers)
print('---response headers---')
print(r.headers)
print(r.headers['content-type']) # application/json
print(r.text)

# redirect and history
# Requests will automatically perform location redirection while using the GET and OPTIONS verbs.
r = requests.get('http://github.com')
print(r.status_code) # 200
print(r.url)#'https://github.com/'
print(r.history) # response 301
print(type(r.history[0])) # requests.models.Response

# If youre using GET or OPTIONS, you can disable redirection handling with the allow_redirects parameter:
r = requests.get('http://github.com',allow_redirects=False)
print(r.status_code) # 301
print(r.url)#'http://github.com/'
print(r.history) # []
