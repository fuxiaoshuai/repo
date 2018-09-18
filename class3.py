#!/usr/bin/python
# -*- coding=utf-8 -*-
class meat():
    def __init__(self):
        self.name = "肉"
        self.weight = 2

class hu(meat):
    def __init__(self):
        super().__init__()
        self.name = "火腿"


class persion():
    def eat(self,obj):
        print("喜欢吃：%s" %obj.name)

rou = meat()

