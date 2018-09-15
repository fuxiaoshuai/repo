#!/usr/bin/python 
#-*- coding:utf-8 -*-
yuan = '/usr/bin/ls'
you = '/cp'
s = open(yuan,'rb')
b = open(you,'wb')
while True:
    date = s.read()
    if not date:
        break
    b.write(date)
s.close()
b.close()
