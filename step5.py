import requests
from credentials import base_url, registration_details
from datetime import timedelta, datetime

"""
Step 5: Add an time interval in seconds to a datestamp with ISO 8601 format
"""

def add_interval_to_datestamp(interval, datestamp):
	datestamp_datetime = datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
	interval_timedelta = timedelta(seconds = interval)

	new_datestamp_datetime = datestamp_datetime + interval_timedelta
	new_datestamp = new_datestamp_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
	
	return new_datestamp

data = {'token' : registration_details['token']}
response = requests.post(base_url + 'dating', json = data)

dictionary = response.json()
datestamp = dictionary['datestamp']
interval = dictionary['interval'] 
new_datestamp = add_interval_to_datestamp(interval, datestamp)

data = {
	'token' : registration_details['token'],
	'datestamp' : new_datestamp
}
requests.post(base_url + 'dating/validate', json = data)