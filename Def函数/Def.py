#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func1():
    print("This is Func1")
func1()


def func2():
    return 0
func2()

def func3():
    return ([0,1,1,2,2,])
func3()


def fun4(x,y):
    t = x*y
    print(t)
fun4(4,5)

#函数调用
#int为整数

def func0(n):
    print(int(n))
    if int(n) > 100:
        return 0
    return func0(int(n*2))

func0(1)