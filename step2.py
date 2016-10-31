import requests

# Reverse string method #
def reverse(string):
	if len(string) <= 1:
		return string

	return reverse(string[1:]) + string[0]

# HTTP POST request #
url = 'http://challenge.code2040.org/api/reverse'
data = {'token' : 'db9598ec6591292144a2f5ce33caca26'}
r = requests.post(url, json=data)

original_string = r.text
reversed_string = reverse(original_string)

# HTTP POST request #
url = 'http://challenge.code2040.org/api/reverse/validate'
data = {
	'token' : 'db9598ec6591292144a2f5ce33caca26',
	'string' : reversed_string
}
requests.post(url, json=data)