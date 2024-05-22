"""
This is a simple application buit for testing the API
"""

import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"
data = {"name": "Nouman", "roll": 27, "city": "Lahore"}
json_data = json.dumps(data)  # convert to json
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
