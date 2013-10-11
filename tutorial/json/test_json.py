import json
from pprint import pprint


data = [ { 'Hola':'Hello', 'Hoi':"Hello", 'noun':"hello" } ]
# dump: python object --->json object
json_encoded = json.dumps(data)
print json_encoded
# load: json object --->python object
python_data = json.loads(json_encoded)
print python_data

with open('data.json') as data_file:    
	data = json.load(data_file)
	pprint(data)
