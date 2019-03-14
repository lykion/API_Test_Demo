# -*- coding:utf-8 -*-
import logging


class logger:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # 设置log输出格式
        self.formatter = logging.Formatter('[%(asctime)s] -- %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S')

        self.consle = logging.StreamHandler()   # StreamHandler将log输出到控制台
        self.consle.setFormatter(self.formatter)
        self.consle.setLevel(logging.INFO)
        self.logger.addHandler(self.consle)

    def info(self, msg):
        self.logger.info(msg)
        self.logger.removeHandler(self.consle)

    def debug(self, msg):
        self.logger.debug(msg)
        self.logger.removeHandler(self.consle)

    def error(self, msg):
        self.logger.error(msg)
        self.logger.removeHandler(self.consle)

    def critical(self, msg):
        self.logger.critical(msg)
        self.logger.removeHandler(self.consle)

    def warning(self, msg):
        self.logger.warning(msg)
        self.logger.removeHandler(self.consle)


if __name__ == '__main__':
    logger().info('中国的天府之国是四川')
