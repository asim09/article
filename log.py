import logging

class Log:
    def __init__(self):
        pass
    @staticmethod
    def init():
        pass
        logging.basicConfig(filename="/tmp/article.log", level=logging.ERROR)

    @staticmethod
    def log_error(msg):
        logging.error(msg)