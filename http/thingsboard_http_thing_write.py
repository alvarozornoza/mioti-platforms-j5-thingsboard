import requests
import random
import time
import json

TIMES = 10
ACCESS_TOKEN = ''

url = f'https://thingsboard.cloud/api/v1/{ACCESS_TOKEN}/telemetry'

headers = {
    "content-type": "application/json"
}

for i in range(TIMES):
    payload = {
        "temperature": round(random.uniform(20, 30), 2)
    }

    print('Sending data to Thingsboard...')
    print(json.dumps(payload, indent=4))
    
    response = requests.post(url, json=payload, headers=headers)
    time.sleep(2)

    print(response.text)