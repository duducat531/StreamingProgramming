# collect And WriteToDB

from kafka import KafkaConsumer
from DBInstance.DBInstance import DBInstance

topicName = 'ebay_metric'
serverAddr = 'localhost:9092'

dbInstance = DBInstance()

consumer = KafkaConsumer(topicName)

for metricData in consumer:
    # save metric to mysql
    dbInstance.SaveToDB(metricData)