from bs4 import BeautifulSoup
import requests
 
url = "http://www.baidu.com" 
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
print(soupp.prettify())
print('-'*50)

for link in soup.find_all('a'):
	#print(link)
	print(link.get('href'))
