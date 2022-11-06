import paho.mqtt.client as mqtt
import random
import time
import json

TIMES = 10
ACCESS_TOKEN = ''

client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)
client.connect("mqtt.thingsboard.cloud",1883,60)

topic = 'v1/devices/me/telemetry'
for i in range(TIMES):

    msg = {
        "temperature": round(random.uniform(20, 30), 2)
    }

    print('Sending data to Thingsboard...')
    print(json.dumps(msg, indent=4))

    client.publish(topic, json.dumps(msg))
    time.sleep(2)

client.disconnect()

