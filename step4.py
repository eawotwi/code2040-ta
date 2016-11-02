import requests
from credentials import base_url, registration_details

"""
Step 4: Remove string in array with a certain prefix
"""

def remove_strings_with_prefix(prefix, array):
	new_array = []
	for string in array:
		if not (string.startswith(prefix)):
			new_array.append(string)
	return new_array

data = {'token' : registration_details['token']}
response = requests.post(base_url + 'prefix', json = data)

dictionary = response.json()
prefix = dictionary['prefix']
array = dictionary['array']
new_array = remove_strings_with_prefix(prefix, array)

data = {
	'token' : registration_details['token'],
	'array' : new_array
}
requests.post(base_url + 'prefix/validate', json = data)