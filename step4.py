"""
Step 4: Remove string in array with a certain prefix
"""

import requests
import post_request
from credentials import base_url, registration_details

def remove_strings_with_prefix(prefix_array_dict):
	prefix = prefix_array_dict['prefix']
	array = prefix_array_dict['array']
	new_array = []
	for string in array:
		if not (string.startswith(prefix)):
			new_array.append(string)
	return new_array

def main():
	specific_endpoint = 'prefix'
	response = post_request.retrieval(specific_endpoint)

	prefix_array_dict = response.json()
	new_array = remove_strings_with_prefix(prefix_array_dict)

	return_value = {'array' : new_array}
	post_request.validation(specific_endpoint, return_value)

if __name__ == '__main__':
    main()