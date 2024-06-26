# 메세지 구독 Subscribe
import sys, os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

load_dotenv()
BROKER_HOST = os.getenv("BROKER_HOST")
BROKER_PORT = int(os.getenv("BROKER_PORT"))
KEEPALIVE = 60
TOPIC = "test/status"

def on_message(client, userdata, message):
    print(f"Received message `{str(message.payload.decode('utf-8'))}` on topic `{message.topic}`")

client = mqtt.Client()
client.on_message = on_message

if client.connect(host=BROKER_HOST, port=BROKER_PORT, keepalive=KEEPALIVE) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.subscribe(topic=TOPIC)

try:
    print("Press CTRL + c to exit... ")
    client.loop_forever()
except:
    print("Disconnecting from broker")

client.disconnect()