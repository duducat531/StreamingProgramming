from kafka import KafkaConsumer
from Sql.DBWriter import DBWriter

topicName = 'ebay_metric'
serverAddr = 'localhost:9092'

dbWriter = DBWriter

consumer = KafkaConsumer(topicName)
for metricData in consumer:
    # save metric to mysql
    dbWriter.save(metricData)