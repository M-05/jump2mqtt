# 메세지 게시 Publish
import paho.mqtt.client as mqtt
import sys
# MQTT 브로커 서버 주소
broker_address = "localhost"

# 클라이언트 인스턴스 생성
client = mqtt.Client()

# 브로커 서버에 연결
if client.connect(host=broker_address, port=1883, keepalive=60) != 0:
    print("Could not connect to MQTT Broker")
    sys.exit(-1)

client.publish(topic="test/status", payload="Hello World from paho-mqtt", qos=0)

client.disconnect()