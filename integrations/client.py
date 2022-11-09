import requests
import json

URL = ''

payload = json.dumps({
    "deviceId": "ACBDE0001",
    "payload": "017564030001040000"
})
headers = {
  'Content-Type': 'application/json'
}

print('Sending data to Thingsboard...')
print(json.dumps(payload, indent=4))
response = requests.request("POST", URL, headers=headers, data=payload)

print(response.text)