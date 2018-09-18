#!/usr/bin/python
# -*- coding=utf-8 -*-
class dog():
    def __del__(self):
        print("let me did! plese! come on!")
    def __init__(self,name,legs,age,color):
        self.name = name
        self.leg = legs
        self.age = age
        self.color = color

    def __str__(self):
        return ("不要，不可以那样！亚麻跌")
    def show(self):
        return ("名字:%s,腿的数量:%s,年龄:%s,颜色:%s" %(self.name,self.leg,self.age,self.color))
class da(dog):
    def show(self):
        return ("理发")



dog1 = da("老狗","12","3","black")
print("第一条老狗===>" + dog1.show())
print(dog1)
print(da.__mro__)
