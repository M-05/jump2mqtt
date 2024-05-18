import paho.mqtt.client as mqtt
from pykafka import KafkaClient

from random import uniform
import time

mqtt_broker = 'mqtt.eclipseprojects.io'
mqtt_client = mqtt.Client('MQTTProducer')
mqtt_client.connect(mqtt_broker)

kafka_client = KafkaClient(hosts='localhost:9092')
kafka_topic = kafka_client.topics['temperature3']
kafka_producer = kafka_topic.get_sync_producer()

while True:
    randNumer = uniform(20.0, 21.0)
    mqtt_client.publish("temperature3", randNumer)
    print(f"MQTT : Just Published {str(randNumer)} to topic temperature3")

    kafka_producer.produce(str(randNumer).encode('ascii'))
    print(f"KAFKA : Just Published {str(randNumer)} to topic temperature3")

    time.sleep(3)



# bin/windows/kafka_topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic temperature3

# bin/wnindows/kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic temperature3 --from-beginning