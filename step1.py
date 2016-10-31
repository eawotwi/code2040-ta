import requests

url = 'http://challenge.code2040.org/api/register'
registration_details = {
	'token' : 'db9598ec6591292144a2f5ce33caca26',
	'github' : 'https://github.com/eawotwi/code2040-tech-assessment'
}
r = requests.post(url, json=registration_details)