import requests
from credentials import base_url, registration_details

"""
Post Request: Handles post requests necessary for steps 2-5 CODE2040 TA 
"""

token = registration_details['token']
data = {'token' : token}

def retrieval(specific_endpoint):
	response = requests.post(base_url + specific_endpoint, json = data)
	return response

def validation(specific_endpoint, return_value):
	data.update(return_value)
	if not (specific_endpoint == 'register'): #excludes step 1
		specific_endpoint += '/validate'

	response = requests.post(base_url + specific_endpoint, json = data)
	print response.text