import requests

# HTTP POST request #
url = 'http://challenge.code2040.org/api/prefix'
data = {'token' : 'db9598ec6591292144a2f5ce33caca26'}
response = requests.post(url, json=data)

dictionary = response.json()
prefix = dictionary['prefix']
array = dictionary['array']

# remove strings with certain prefix
new_array = []
for string in array:
	if not (string.startswith(prefix)):
		new_array.append(string)

# HTTP POST request #
url = 'http://challenge.code2040.org/api/prefix/validate'
data = {
	'token' : 'db9598ec6591292144a2f5ce33caca26',
	'array' : new_array
}
requests.post(url, json=data)