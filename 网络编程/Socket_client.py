#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2018/6/2 10:25


import socket  #引入socket模块

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',8909))
while True:
    msg = input(">>:").strip()
    if len(msg)==0:continue
    client.send(b"Hello WOrld!")
    data = client.recv(1024)
    client.close()
    print('recv',data)
client.close()



