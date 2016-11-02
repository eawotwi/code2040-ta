import requests
from credentials import base_url, registration_details

"""
Step 3: Locate the index of the needle in the haystack array
"""

def locate_needle(needle, haystack):
	needle_index = haystack.index(needle)
	return needle_index

data = {'token' : registration_details['token']}
response = requests.post(base_url + 'haystack', json = data)

dictionary = response.json()
haystack = dictionary['haystack']
needle = dictionary['needle']
needle_index = locate_needle(needle, haystack)

data = {
	'token' : registration_details['token'],
	'needle' : needle_index
}
requests.post(base_url + 'haystack/validate', json = data)