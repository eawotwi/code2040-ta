"""
Step 2: Reverse a string
"""

import requests
import post_request
from credentials import base_url, registration_details

def reverse_string(string):
	reversed_string = string[::-1]
	return reversed_string

def main():
	specific_endpoint = 'reverse'
	response = post_request.retrieval(specific_endpoint)

	original_string = response.text
	reversed_string = reverse_string(original_string)

	return_value = {'string' : reversed_string}
	post_request.validation(specific_endpoint, return_value)

if __name__ == '__main__':
    main()