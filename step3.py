import requests

# HTTP POST request #
url = 'http://challenge.code2040.org/api/haystack'
data = {'token' : 'db9598ec6591292144a2f5ce33caca26'}
response = requests.post(url, json=data)

dictionary = response.json()
haystack = dictionary['haystack']
needle = dictionary['needle']

# determine index of needle in haystack #
needle_index = haystack.index(needle)

# HTTP POST request #
url = 'http://challenge.code2040.org/api/haystack/validate'
data = {
	'token' : 'db9598ec6591292144a2f5ce33caca26',
	'needle' : needle_index
}
requests.post(url, json=data)