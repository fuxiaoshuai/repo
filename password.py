#!/usr/bin/python 
#-*- coding:utf-8 -*-
user = ''
password = ''
a = 0
while user != 'devops' and password != '123':
    user = input("into our name:")
    password = input("into your password:")
    if user.lower() == 'devops' and password == '123':
        print('ojbk')
    else:
        a += 1
        print('wandan cuole')
    if a == 3:
        print("time out")
        break

