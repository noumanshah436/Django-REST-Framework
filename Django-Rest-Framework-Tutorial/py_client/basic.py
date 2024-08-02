import requests

# HTTP Request (non-api request) -> HTML
# REST API HTTP Request -> JSON

# JavaScript Object Nototion ~ Python Dict

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"

# this will return back my passed json data in the response
# get_response = requests.get(endpoint, json={"query": "Hello World!"})

# this will return back my passed data data in the response
# get_response = requests.get(endpoint, data={"query": "Hello World!"})

# ****************************************************************
#  params will be passed as query parameters
#  json data will be passed as request body

# endpoint = "http://localhost:8000/api/home"
# my_data = {"name": "Nouman"}
# get_response = requests.get(endpoint, params={"abc": 123}, json=my_data)

endpoint = "http://localhost:8000/api/model_instance_to_dic"
get_response = requests.get(endpoint)

# ****************************************************************

# endpoint = "http://localhost:8000/api/"
# my_data = {"title": "Abc123", "content": "Hello world", "price": "abc134"}
# get_response = requests.post(endpoint, json=my_data)  # HTTP Request

# print(get_response.headers)
# print(get_response.text) # print raw text response
# print(get_response.status_code)

# print(get_response.text)
print(get_response.json())  # return a proper python dictionary
# print(get_response.status_code)
