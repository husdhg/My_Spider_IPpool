#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:任向民
# datetime:2019/4/3 16:36
# software: PyCharm

from Scheduling import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()