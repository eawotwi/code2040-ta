import requests
from credentials import base_url, registration_details

"""
Step 1: Connect to the registration endpoint
"""

requests.post(base_url + 'register', json = registration_details)