#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:任向民
# datetime:2019/4/3 14:21
# software: PyCharm
MAX_SCORE = 100
MIN_SCORE = 0
INITAL_SCORE = 10
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'root'

import redis
from random import choice


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITAL_SCORE):
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, score, proxy)

    def random(self):
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise Exception('无代理ip使用')

    def decrease(self, proxy):
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        return self.db.zadd(REDIS_KEY, MIN_SCORE, proxy)

    def count(self):
        return self.db.zcard(REDIS_KEY)

    def all(self):
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)


