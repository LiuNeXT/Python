#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2018/6/5 17:25

import threading
import time


class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n

    def run(self):
        print("running Task", self.n)
        time.sleep(2)

t1 = MyThread("T1")
t2 = MyThread("T2")

t1.start()
t1.join()  #=wait()
t2.start()
