# 메세지 게시 Publish
import sys, os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

load_dotenv()
BROKER_HOST = os.getenv("BROKER_HOST") # "localhost"
BROKER_PORT = int(os.getenv("BROKER_PORT")) # 1883
KEEPALIVE = 60
TOPIC = "test/status"
PAYLOAD = "Hello World from paho-mqtt"
# 클라이언트 인스턴스 생성
client = mqtt.Client()

# 브로커 서버에 연결
if client.connect(host=BROKER_HOST, port=BROKER_PORT, keepalive=KEEPALIVE) != 0:
    print("Could not connect to MQTT Broker")
    sys.exit(-1)

# def client_publish(topic, payload, qos=0):
client.publish(topic=TOPIC, payload=PAYLOAD, qos=0)
client.disconnect()