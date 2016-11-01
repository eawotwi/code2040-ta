import requests

# Reverse string method #
def remove_strings_with_prefix(prefix, array):
	new_array = []
	for string in array:
		if (string.startswith(prefix) == False):
			new_array.append(string) 

	return new_array

# HTTP POST request #
url = 'http://challenge.code2040.org/api/prefix'
data = {'token' : 'db9598ec6591292144a2f5ce33caca26'}
response = requests.post(url, json=data)

dictionary = response.json()

# determine index of needle in haystack #
new_array = remove_strings_with_prefix(dictionary['prefix'], dictionary['array']) 

# HTTP POST request #
url = 'http://challenge.code2040.org/api/prefix/validate'
data = {
	'token' : 'db9598ec6591292144a2f5ce33caca26',
	'array' : new_array
}
requests.post(url, json=data)