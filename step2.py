import requests

# HTTP POST request #
url = 'http://challenge.code2040.org/api/reverse'
data = {'token' : 'db9598ec6591292144a2f5ce33caca26'}
r = requests.post(url, json=data)

# reverse string #
original_string = r.text
reversed_string = original_string[::-1] #reverse string using extended slice operator

# HTTP POST request #
url = 'http://challenge.code2040.org/api/reverse/validate'
data = {
	'token' : 'db9598ec6591292144a2f5ce33caca26',
	'string' : reversed_string
}
requests.post(url, json=data)