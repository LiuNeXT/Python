#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2018/6/5 14:44


import socket
client = socket.socket()

client.connect(('localhost',9999))


class FtpClient(object):
    def __init__(self):

        pass

    def connect(self):