"""
This is a simple application buit for testing the API
"""

import requests
import json

login_url = "http://localhost:8000/auth/login/"  # Replace with your login URL
login_data = {"username": "admin", "password": "admin"}

session = requests.Session()

response = session.post(login_url, data=login_data)

print(response)

if response.status_code == 200:
    print("Login successful!")
else:
    print("Login failed:", response.status_code)



# https://stackoverflow.com/questions/23687643/how-can-i-use-sessionauthentication-to-make-a-login-rest-api-with-django-rest-fr