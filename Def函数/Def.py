#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# def func1():
#     print("This is Func1")
# func1()
#
#
# def func2():
#     return 0
# func2()
#
# def func3():
#     return ([0,1,1,2,2,])
# func3()
#
#
# def fun4(x,y):
#     print(x)
#     print(y)
#     t = x*y
#     print(t)
# fun4(4,5)

#函数调用
def func0(n):
    print(int(n))
    return func0(int(n/2))

func0(10)