import requests
from credentials import base_url, registration_details

"""
Step 2: Reverse a string
"""

def reverse_string(string):
	reversed_string = string[::-1]
	return reversed_string

data = {'token' : registration_details['token']}
response = requests.post(base_url + 'reverse', json = data)

original_string = response.text
reversed_string = reverse_string(original_string)

data = {
	'token' : registration_details['token'],
	'string' : reversed_string
}
requests.post(base_url + 'reverse/validate', json = data)