import requests

# Reverse string method #
def find_needle(haystack, needle):
	for index, string in enumerate(haystack):
		if (string == needle):
			return index

	return -1

# HTTP POST request #
url = 'http://challenge.code2040.org/api/haystack'
data = {'token' : 'db9598ec6591292144a2f5ce33caca26'}
response = requests.post(url, json=data)

dictionary = response.json()

# determine index of needle in haystack #
needle_index = find_needle(dictionary['haystack'], dictionary['needle'])

# HTTP POST request #
url = 'http://challenge.code2040.org/api/haystack/validate'
data = {
	'token' : 'db9598ec6591292144a2f5ce33caca26',
	'needle' : needle_index
}
requests.post(url, json=data)