import csv
import requests
import json

import requests
import json
from datetime import datetime

JWT_TOKEN = ''
DEVICE_ID = ''
LIMIT = 100
START_DATE = '2022-01-01T00:00:00.000Z'
END_DATE = '2022-12-31T23:59:59.999Z'

start_ts = int(datetime.strptime(START_DATE, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp())*1000
end_ts = int(datetime.strptime(END_DATE, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp())*1000

def getResourceKeys():
    url = f'https://thingsboard.cloud/api/plugins/telemetry/DEVICE/{DEVICE_ID}/keys/timeseries'
    headers = {
        "Content-Type": "application/json",
        "X-Authorization": JWT_TOKEN
    }
    response = requests.get(url, headers=headers)
    parsed = json.loads(response.text)
    return parsed

def getResourceValues(key):
    url = f'https://thingsboard.cloud/api/plugins/telemetry/DEVICE/{DEVICE_ID}/values/timeseries?keys={key}&startTs={start_ts}&endTs={end_ts}'
    headers = {
        "Content-Type": "application/json",
        "X-Authorization": JWT_TOKEN
    }
    response = requests.get(url, headers=headers)
    parsed = json.loads(response.text)
    data = []
    for key in parsed:
        for obj in parsed[key]:
            data.append([obj['ts'], key, obj['value']])

    return data

with open('thingsboard_data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    header = ['datetime', 'key', 'value']
    # write the header
    writer.writerow(header)

    resource_keys = getResourceKeys()
    for key in resource_keys:
        data = getResourceValues(key)
        # write multiple rows
        writer.writerows(data)