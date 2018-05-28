#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 用于序列化的两个模块
#
# json，用于字符串 和 python数据类型间进行转换
# pickle，用于python特有的类型 和 python的数据类型间进行转换
# Json模块提供了四个功能：dumps、dump、loads、load
# pickle模块提供了四个功能：dumps、dump、loads、load


import json
#不同语言的交互，通用
#序列化
info = {'name':'Alex','age':24}
f = open("test.txt","w")
f.write(str(info))
f.close()

#反序列化
f = open("test.txt","r")
data = f.read()
f.close()
print(data)

data = json.loads(f.read())
data = json.dumps(f.read())

import pickle
#python专用
f = open('text1.txt','rb')
data = pickle.loads(f.read())
data = pickle.dumps(f.read())
print(data(data))