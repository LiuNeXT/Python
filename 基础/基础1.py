#!/usr/bin/env python
# -*- coding: utf-8 -*-


#当行注视 ：# 被注释内容
#多行注释 ：""" 被注释内容 """


#世界你好
print("Hello World!")


#声明变量，赋值
name1 = "ALex"
name2 = name1
print(name1,name2)


#用户输入
name = input("What is your name?")
print("Hello，"+name)

#字符串格式化输出
#PS: 字符串是 %s;整数 %d;浮点数%f
print("Hello，%s"%name)

#密码
import getpass
pwd = getpass.getpass("请输入密码：")
print(pwd)

#模块初识
import sys
print(sys.argv)

#列表
name_list = ['alex', 'seven', 'eric']

#元组(不可变列表)
ages = (11, 22, 33, 44, 55)

#6、字典（无序）
person = {"name": "mr.wu", 'age': 18}

#表达式if ... else
# 提示输入用户名和密码

# 验证用户名和密码
#     如果错误，则输出用户名或密码错误
#     如果成功，则输出 欢迎，XXX!

my_age = 28

user_input = int(input("input your guess num:"))

if user_input == my_age:
    print("Congratulations, you got it !")
elif user_input < my_age:
    print("Oops,think bigger!")
else:
    print("think smaller!")

#while循环
count = 0
while True:
    print("你是风儿我是沙,缠缠绵绵到天涯...",count)
    count +=1
    if count == 100:
        print("去你妈的风和沙,你们这些脱了裤子是人,穿上裤子是鬼的臭男人..")
        break


#回到上面for 循环的例子，如何实现让用户不断的猜年龄，但只给最多3次机会，再猜不对就退出程序。
my_age = 28

count = 0
while count < 3:
    user_input = int(input("input your guess num:"))
    if user_input == my_age:
        print("Congratulations, you got it !")
        break
    elif user_input < my_age:
        print("Oops,think bigger!")
    else:
        print("think smaller!")
    count += 1  # 每次loop 计数器+1
    if count == 3:
        continue_confirm = input("do you want to try ")
        if continue_confirm != 'n':
            count = 0
else:
    print("猜这么多次都不对,你个笨蛋.")


#三元运算
result = 值1 if 条件 else 值2


# 打开文件：
file_obj = file("文件路径","模式")
# 打开文件的模式有：
# r，以只读方式打开文件
# w，打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a，打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# w+，打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

with
#当with代码块执行完毕时，内部会自动关闭并释放文件资源
#为了避免打开文件后忘记关闭，可以通过管理上下文，即：

with open('文件名','模式') as f:
    ...

读取文件的内容：
# 一次性加载所有内容到内存
obj.read()

# 一次性加载所有内容到内存，并根据行分割成字符串
obj.readlines()

# 每次仅读取一行数据
for line in obj:
    print line

#写文件的内容：
obj.write('内容')

#关闭文件句柄：
obj.close()


for i in range(0,10,2):#每2个就跳1个打印
    print("loop",i) 步长

for i in range(10):
    if i < 5:
        print("loop",i)
    else:
        continue
    print("呵呵")

#嵌套循环
for i range(10):
    print('--------',i)
    for j in range(10):
        print(j)
        if j > 5:
            break



#对于Python，一切事物都是对象，对象基于类创


