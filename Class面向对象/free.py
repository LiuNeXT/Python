#!/usr/bin/env python
# -*- coding: utf-8 -*-


class People(object):
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def print_name(self):
        print("%s" % self.name)

    def print_age(self):
        print("%s" % self.__age)

class Family(People):


class Man(People):
    def __init__(self,name,age,sex,job):
        super(Man,self).__init__(name,age)
        self.sex=sex
        self.job=job

    def work(self):
        print("%s work in %s" % (self.name,self.job))

class Woman(People):
    def __init__(self,name,age,sex,shop):
        super(Woman,self).__init__(name,age)
        self.sex=sex
        self.shop=shop

    def shopping(self):
        print("%s go to %s" % (self.name,self.shop))




p1 = People("ALex",22)
m1 = Man("man1",22,"man")
p1.print()
m1.print()
print(len(p1.name))
p1.print_age()
