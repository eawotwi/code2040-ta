from datetime import timedelta, datetime
import requests

# HTTP POST request #
url = 'http://challenge.code2040.org/api/dating'
data = {'token' : 'db9598ec6591292144a2f5ce33caca26'}
response = requests.post(url, json=data)

dictionary = response.json()
datestamp = dictionary['datestamp'] #ISO 8601 format
interval = dictionary['interval'] #in seconds

datestamp_datetime = datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
interval_timedelta = timedelta(seconds=interval)

new_datestamp_datetime = datestamp_datetime + interval_timedelta
new_datestamp = new_datestamp_datetime.strftime("%Y-%m-%dT%H:%M:%SZ") #ISO 8601 format

# HTTP POST request #
url = 'http://challenge.code2040.org/api/dating/validate'
data = {
	'token' : 'db9598ec6591292144a2f5ce33caca26',
	'datestamp' : new_datestamp
}
requests.post(url, json=data)