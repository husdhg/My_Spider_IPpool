#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:任向民
# datetime:2019/4/3 15:56
# software: PyCharm

TESTER_CYCLE = 20
GETTER_CYCLE = 20
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True
API_HOST = '127.0.0.1'
API_PORT = 5555

from multiprocessing import Process
from ip_io import app
from save_run import Getter
from Test import Tester
import time

class Scheduler():
    def schedule_tester(self, cycle = TESTER_CYCLE):
        tester = Tester()
        while True:
            print('开始测试')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):

        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        app.run(API_HOST, API_PORT)


    def run(self):
        print('运行代理池')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()