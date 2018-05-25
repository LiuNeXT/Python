#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 作业一：博客
#-------------------------
# 作业二：编写登陆接口
# 输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后锁定
#----------------------
# 作业三：多级菜单
# 三级菜单
# 可依次选择进入各子菜单
# 所需新知识点：列表、字典


上传到github

#Task1
import getpass
name = "liuzhuyuan"
pwd = "Alex91"

int_name = input("input your name")
int_pwd = getpass.getpass("input passwd")

with open('login','a+') as f:
    f.write('nihao/n')
