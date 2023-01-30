import requests
import json

params = {
  'api_key': 'APIKEY_HERE',
  'params1': 'value1'
}
method = 'ping'
api_base = 'http://airlabs.co/api/v9/'
api_result = requests.get(api_base+method, params)
api_response = api_result.json()

print(json.dumps(api_response, indent=4, sort_keys=True))
