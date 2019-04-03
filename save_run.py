#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:任向民
# datetime:2019/4/3 15:03
# software: PyCharm

from redisdb import RedisClient
from get_ip import *

POOL_UPPER_THRESHOLD = 10000

class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('开始执行')
        if not self.is_over_threshold():
            a = self.crawler.__CrawlFuncCount__
            for callback_lable in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_lable]
                proxies = self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)
