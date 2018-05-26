#!/usr/bin/env python
# -*- coding: utf-8 -*-


#生成器
#
# for i in range(10):
#     print(i)
#
# (i*i for i in range(10))
#
# generator
#
# #取值
# c.__next__()


# #斐波那契数列
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b,a+b
#         n=n+1
#     return 'done'
# fib(10)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        yield b  #保存函数中断状态
        a,b = b,a+b
        n=n+1
    return 'done'
g = fib(10)
print(g)
