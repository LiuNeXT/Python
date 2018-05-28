#!/usr/bin/env python
# -*- coding: utf-8 -*-

#事列
# class Role(object):
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         self.name = name
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money
#
#     def shot(self):
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#
#
# r1 = Role('Alex', 'police', 'AK47’) #生成一个角色
# r2 = Role('Jack', 'terrorist', 'B22’)  #生成一个角色


#继承事列
# !_*_coding:utf-8_*_
# __author__:"Alex Li"


class SchoolMember(object):
    members = 0  # 初始学校人数为0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        pass

    def enroll(self):
        '''注册'''
        SchoolMember.members += 1
        print("\033[32;1mnew member [%s] is enrolled,now there are [%s] members.\033[0m " % (
        self.name, SchoolMember.members))

    def __del__(self):
        '''析构方法'''
        print("\033[31;1mmember [%s] is dead!\033[0m" % self.name)


class Teacher(SchoolMember):
    def __init__(self, name, age, course, salary):
        super(Teacher,self).__init__(name,age)
        self.course = course
        self.salary = salary
        self.enroll()

    def teaching(self):
        '''讲课方法'''
        print("Teacher [%s] is teaching [%s] for class [%s]" % (self.name, self.course, 's12'))

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' % (self.name, 'Oldboy', self.course)
        print(msg)


class Student(SchoolMember):
    def __init__(self, name, age, grade, sid):
        super(Student, self).__init__(name, age)
        self.grade = grade
        self.sid = sid
        self.enroll()

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' % (self.name, self.grade, 'Oldboy')
        print(msg)


if __name__ == '__main__':
    t1 = Teacher("Alex", 22, 'Python', 20000)
    t2 = Teacher("TengLan", 29, 'Linux', 3000)

    s1 = Student("Qinghua", 24, "Python S12", 1483)
    s2 = Student("SanJiang", 26, "Python S12", 1484)

    t1.teaching()
    t2.teaching()
    t1.tell()

class Role(object):
    def __init__(self,name,role,swaper):
        self.name=name
        self.role=role
        self.swaper=swaper

    def buy_shot(self):
        print("%s have a %s" %(self.name,self.swaper))

    def printname(self):
        print("%s" %self.name)

r1 = Role("Alex","Police","AK47")
r1.buy_shot()
r2 = Role("Fiona","Police","M443")
r2.printname()
r2.buy_shot()


c1.talk
d1.talk





