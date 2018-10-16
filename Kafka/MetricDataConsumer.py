# collect And WriteToDB
from KafkaInstance import DataConsumer
from DBInstance.DBInstance import DBInstance

if __name__ == '__main__':
    metricDataConsumer = DataConsumer(topicName='ebay_metric', serverAddr='localhost:9092',
                                   groupId='test_metric_data_consumer',
                                   dbInstance=DBInstance("localhost", "wyn", "123456", "ebay_metric"))
    metricDataConsumer.ReceiveAndSaveToDB()