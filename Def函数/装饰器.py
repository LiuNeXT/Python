#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# def bar():
#     print("in the bar")
# def foo():
#     bar()
#     print("in the foo")
# foo()
#
# #匿名函数
# calc = lambda x:x*3
# print(calc(3))

#语糖法，基本装饰器
def func0(deco):
    def warpper(*args,**kwargs):
        return deco(*args,**kwargs)
        print("Hello，It my pleasure")
    return warpper

@func0  #func0 = func0(func1)
def func1(name,age):
    print("I am Husband: %s"%name,age)

@func0
def func2(name,age):
    print("I am Wife: %s"%name,age)

func1("Alex",27)
func2("Fiona",26)

#登陆接口装饰器
def login(func):  # 把要执行的模块从这里传进来

    def inner(*args, **kwargs):  # 再定义一层函数
        _username = "alex"  # 假装这是DB里存的用户信息
        _password = "abc!23"  # 假装这是DB里存的用户信息
        global user_status

        if user_status == False:
            username = input("user:")
            password = input("pasword:")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")

        if user_status == True:
            func(*args, **kwargs)  # 看这里看这里，只要验证通过了，就调用相应功能

    return inner  # 用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数



#三层装饰器
user_status = False #用户登录了就把这个改成True

def login(auth_type): #把要执行的模块从这里传进来
    def auth(func):
        def inner(*args,**kwargs):#再定义一层函数
            if auth_type == "qq":
                _username = "alex" #假装这是DB里存的用户信息
                _password = "abc!23" #假装这是DB里存的用户信息
                global user_status

                if user_status == False:
                    username = input("user:")
                    password = input("pasword:")

                    if username == _username and password == _password:
                        print("welcome login....")
                        user_status = True
                    else:
                        print("wrong username or password!")

                if user_status == True:
                    return func(*args,**kwargs) # 看这里看这里，只要验证通过了，就调用相应功能
            else:
                print("only support qq ")
        return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数

    return auth

def home():
    print("---首页----")

@login('qq')
def america():
    #login() #执行前加上验证
    print("----欧美专区----")

def japan():
    print("----日韩专区----")

@login('weibo')
def henan(style):
    '''
    :param style: 喜欢看什么类型的，就传进来
    :return:
    '''
    #login() #执行前加上验证
    print("----河南专区----")

home()
# america = login(america) #你在这里相当于把america这个函数替换了
#henan = login(henan)

# #那用户调用时依然写
america()




