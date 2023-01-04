import requests
import json

params = {
  'api_key': '7e94f961-2fcf-44aa-b3ee-f99146a1b053',
  'params1': 'value1'
}
method = 'ping'
api_base = 'http://airlabs.co/api/v9/'
api_result = requests.get(api_base+method, params)
api_response = api_result.json()

print(json.dumps(api_response, indent=4, sort_keys=True))
