
import json
import os 
from pprint import pprint
import requests

subscription_key = 'c4b84197e233477885b9c6185ca8e8b2'
endpoint = 'https://api.bing.microsoft.com/v7.0/search'

query = "Chicago"

mkt = 'en-US'
params = { 'q': query, 'mkt': mkt}
headers = { 'Ocp-Apim-Subscription-Key': subscription_key}

# Call the API
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    print("Headers:")
    print(response.headers)

    # print("JSON Response:")
    pprint(response.json())
    # return response.json()
except Exception as ex:
    raise ex