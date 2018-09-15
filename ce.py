#!/usr/bin/python 
#-*- coding:utf-8 -*-
print("#"*20)
print("你要买什么水果？\n1.橘子\n2.苹果\n3.香蕉\n4.不想买了，按（Q/q/4）退出！")
print("#"*20)
l1 = ['1','2','3','4','q']
import re
while 1:
    fiurt = input("shu ru ming cheng:")
    if fiurt == '1':
        pice = 5
    elif fiurt == '2':
        pice = 6
    elif fiurt == '3':
        pice = 7
    elif fiurt == '4' or fiurt.lower() == 'q':
        break
    else:
        print("输入有误请重新输入！")
        continue
    weight = input("请输入重量：")
    w = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
    s = w.match(weight)
    if weight.isdigit():
        jia = int(weight) * pice
        print('你需要支付: %s元' %jia)
    elif s:
        jia = float(weight) * pice
        print('你需要支付: %s元' % jia)
    else:
        print("输入有误请重新输入！")
        continue


