"""
Step 1: Connect to the registration endpoint
"""

import requests, post_request
from credentials import base_url, registration_details

def main():
	specific_endpoint = 'register'
	return_value = {'github' : registration_details['github']}
	post_request.validation(specific_endpoint, return_value)

if __name__ == '__main__':
    main()
