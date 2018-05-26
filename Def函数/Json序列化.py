#!/usr/bin/env python
# -*- coding: utf-8 -*-
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