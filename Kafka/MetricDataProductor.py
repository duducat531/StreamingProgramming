# MetricCollector
from KafkaInstance.DataProducer import DataProducer
if __name__ == '__main__':
    metricDataConsumer = DataProducer(topicName='ebay_metric', serverAddr='localhost:9092')
    metricData = {'value': 46.0,
                  'name':'cpuUsage',
                  'timestamp':'2017-06-02T04:41:10:383Z'}
    metricDataConsumer.PublishData(metricData)

