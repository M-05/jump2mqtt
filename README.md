# jump2mqtt

## Git Clone
```
git clone https://github.com/M-05/jump2mqtt.git
```
## jump2mqtt 경로 이동 후 라이브러리 설치
```
cd jump2mqtt
pip install -r requirements.txt
```
# Kafka MQTT 실습
<div align='center'>
  <img width="800" alt="kafka_mqtt" src="https://github.com/M-05/jump2mqtt/assets/103846429/ead800c7-ca11-4c09-bace-212168d74b31">
</div>

## Mac OS에서 Kafka 설치
### web get 설치
```
brew install wget
```
```
wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.13-2.8.0.tgz
tar xvf kafka_2.13-2.8.0.tgz
```

## 터미널 창 5개 준비
<div align="center">
  <img src=https://github.com/M-05/jump2mqtt/assets/103846429/d91e2e17-c2a7-4285-a316-2e5da618931a alt=sample_gif2>
</div>

### 3개의 터미널
#### 1.Zookeeper 실행
```
cd kafka_2.13-2.8.0
bin/zookeeper-server-start.sh config/zookeeper.properties
```
#### 2.Kafka 실행
```
cd kafka_2.13-2.8.0
bin/kafka-server-start.sh config/server.properties
```
#### 3-1.Kafka topic 생성
```
cd kafka_2.13-2.8.0
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic temperature3
```
> Created topic temperature3.
#### 3-2.Kafka topic으로 부터 메세지 받기
```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic temperature3 --from-beginning  
```
### 2개의 터미널
#### 4.mqtt_kafka_proucer 실행
```
python mqtt/mqtt_kafka_producer.py
```
#### 5.mqtt_subscribe 실행
```
python mqtt/mqtt_subscribe.py
```

---
# MQTT 실습

## 터미널 창 3개 준비
<div align="center">
  <img src=https://github.com/M-05/jump2mqtt/assets/103846429/7d290465-cbfd-49c6-b9e8-2bd7c40e7d47 alt=sample_gif>
</div>


### Mosquitto MQTT broker 실행
```
mosquitto -v
```
### topic의 메세지 받기
```
mosquitto_sub -t test/status
```

### publish 실행
```
python mqtt/publish.py 
```
---
# 레퍼런스
[Integrate Kafka and MQTT - How to connect MQTT and Kafka](https://www.youtube.com/watch?v=FDCTQ47oXUg)  
[MQTT with Python](https://www.youtube.com/watch?v=cVB3Sk9nAE8&t=2174s)
