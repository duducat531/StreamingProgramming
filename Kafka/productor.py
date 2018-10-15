# MetricCollector
from kafka import KafkaProducer
import json

topicName = 'ebay_metric'
serverAddr = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=serverAddr, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def SendData(metricData):
    producer.send(topicName, metricData)