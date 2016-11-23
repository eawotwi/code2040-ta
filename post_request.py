import sys
import requests
from credentials import base_url, registration_details

"""
Post Request: Handles post requests necessary for steps 2-5 CODE2040 TA 
"""

token = registration_details['token']
data = {'token' : token}

def retrieval(specific_endpoint):
	try:
		response = requests.post(base_url + specific_endpoint, json = data)
		response.raise_for_status()
		return response

	except requests.exceptions.RequestException as e:
		print e
		sys.exit('Incomplete step: unable to retrieve information')
		

def validation(specific_endpoint, return_value):
	data.update(return_value)
	if not (specific_endpoint == 'register'): #excludes step 1
		specific_endpoint += '/validate'

	try: 
		response = requests.post(base_url + specific_endpoint, json = data)
		response.raise_for_status()

	except requests.exceptions.RequestException as e:
		print e
		sys.exit('Incomplete step: unable to validate information')