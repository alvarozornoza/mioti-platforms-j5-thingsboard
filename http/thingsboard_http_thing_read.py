import requests
import json
from datetime import datetime

JWT_TOKEN = ''
DEVICE_ID = ''
RESOURCE_KEY = 'temperature'
LIMIT = 100
START_DATE = '2022-01-01T00:00:00.000Z'
END_DATE = '2022-12-31T23:59:59.999Z'

start_ts = int(datetime.strptime(START_DATE, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp())*1000
end_ts = int(datetime.strptime(END_DATE, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp())*1000

url = f'https://thingsboard.cloud/api/plugins/telemetry/DEVICE/{DEVICE_ID}/values/timeseries?keys={RESOURCE_KEY}&startTs={start_ts}&endTs={end_ts}'

print(url)

headers = {
    "Content-Type": "application/json",
    "X-Authorization": JWT_TOKEN
}

response = requests.get(url, headers=headers)

parsed = json.loads(response.text)

print(json.dumps(parsed, indent=4))

