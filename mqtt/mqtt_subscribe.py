import paho.mqtt.client as mqtt
import time

mqtt_broker = 'mqtt.eclipseprojects.io'
mqtt_client = mqtt.Client('MQTTConsumer')
mqtt_client.connect(mqtt_broker)

def on_message(client, userdata, message):
    msg_payload = str(message.payload)
    print(f"Receviced MQTT message {msg_payload}")

mqtt_client.loop_start()
mqtt_client.subscribe('temperature3')
mqtt_client.on_message = on_message
time.sleep(300)

mqtt_client.loop_stop()