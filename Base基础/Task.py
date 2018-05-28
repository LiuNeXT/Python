#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 作业一：博客


#-------------------------
# 作业二：编写登陆接口
# 输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后锁定

import getpass
import codecs
#用户名密码
name = "Alex"
pwd = "Alex91"
#输入窗口
#int_pwd = getpass.getpass(str("input password："))
#判断
count = 0
while count < 3:
        int_name = input(str("input your name："))
        int_pwd = input(str("input password："))
        if name == int_name and pwd == int_pwd:
            print("Login Successful.Welcome")
        else:
            print("It's Worng.Please try again")
        count +=1
        if count == 3:
            with codecs.open('login.txt', 'a+', 'utf-8') as f:
                f.write(int_name)
else:
    print("you accout is lock.账号被写入黑名单")





#----------------------
# 作业三：多级菜单
# 三级菜单
# 可依次选择进入各子菜单
# 所需新知识点：列表、字典



