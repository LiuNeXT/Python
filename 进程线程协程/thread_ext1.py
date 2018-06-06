#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2018/6/5 15:31

import threading  #线程模块
import time

def run(n):
    print("Task", n)
    time.sleep(2)
    print("task done",n,)
    global num
    num +=1
#
# t1 = threading.Thread(target=run,args=("t1",))
# t1.start()
# t2 = threading.Thread(target=run,args=("t2",))
# t2.start()
start_time = time.time()
t_objs = []
for i in range(10):
    t = threading.Thread(target=run,args=("t-%s" %i,))
    t.setDaemon(True) #把当前线程设置为守护线程
    t.start()
    t_objs.append(t)
for t in t_objs:
    t.join()
print("-----------------all threads has finished")
print("cost time :",time.time()-start_time)

lock = threading.Lock()
num = 0