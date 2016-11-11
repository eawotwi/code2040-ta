"""
Step 5: Add an time interval in seconds to a datestamp with ISO 8601 format
"""

import requests, post_request
from credentials import base_url, registration_details
from datetime import timedelta, datetime

def add_interval_to_datestamp(interval_datestamp_dict):
	interval = interval_datestamp_dict['interval'] 
	datestamp = interval_datestamp_dict['datestamp']

	datestamp_datetime = datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
	interval_timedelta = timedelta(seconds = interval)

	new_datestamp_datetime = datestamp_datetime + interval_timedelta
	new_datestamp = new_datestamp_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
	
	return new_datestamp

def main():
	specific_endpoint = 'dating'
	response = post_request.retrieval(specific_endpoint)

	interval_datestamp_dict = response.json()
	new_datestamp = add_interval_to_datestamp(interval_datestamp_dict)

	return_value = {'datestamp' : new_datestamp}
	post_request.validation(specific_endpoint, return_value)

if __name__ == '__main__':
    main()