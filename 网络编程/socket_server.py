#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2018/6/2 11:13


import socket
server = socket.socket()
server.bind(("localhost",8909))  #绑定端口
server.listen() #监听
print("服务在侦听")
while True:
    conn,addr = server.accept()#等待客户端进来
    #conn就是客户端过来而在服务器端为其生成的一个连接实列
    data = conn.recv(1024)
    print("revi",data)
    conn.send(data.upper())
server.close()

