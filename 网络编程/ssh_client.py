#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2018/6/5 10:43

import socket

client = socket.socket()
client.connect(('localhost',9999))
while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode("utf-8"))
    cmd_rev = client.recv(1024)
    print(cmd_rev.decode())
