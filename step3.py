"""
Step 3: Locate the index of the needle in the haystack array
"""

import requests
import post_request
from credentials import base_url, registration_details

def locate_needle(needle_in_haystack_dict):
	haystack = needle_in_haystack_dict['haystack']
	needle = needle_in_haystack_dict['needle']
	needle_index = haystack.index(needle)
	return needle_index

def main():
	specific_endpoint = 'haystack'
	response = post_request.retrieval(specific_endpoint)

	needle_in_haystack_dict = response.json()
	needle_index = locate_needle(needle_in_haystack_dict)

	return_value = {'needle' : needle_index}
	post_request.validation(specific_endpoint, return_value)

if __name__ == '__main__':
    main()