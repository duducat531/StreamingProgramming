class MetricApi(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "wyn", "123456", "ebay_log", autocommit=True)