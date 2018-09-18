#!/usr/bin/python
# -*- coding=utf-8 -*-
def a():
    name = input("请输入你的名字：")
    pas = input("请输入你的密码：")
b = 0
while b < 3:
    a()
    if name == 'devops' and pas == '123':
        print("登陆成功")
        break
    else:
        print("输入错误，请重新输入：")
        b += 1
        a()
    if b == 3:
        print("输入超过三次，强制退出！")
        break
