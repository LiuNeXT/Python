#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2018/6/2 17:19


import socket
import os
server = socket.socket()

server.bind(('localhost',9999))
server.listen()
while True:
    conn, addr = server.accept()
    print("new conn:", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令", data)
        cmd_res = os.popen(data.decode()).read()
        print("before send", len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd hao no output..."

        conn.send(cmd_res.encode("utf-8"))
        print("send done")
server.close()