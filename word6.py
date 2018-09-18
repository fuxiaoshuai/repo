#!/usr/bin/python
# -*- coding=utf-8 -*-
unti = """
1.面包
2.米饭
3.水饺
4.退出
请输入:"""
while True:
    input1 = input(unti)
    if input1 == "1":
        print("面包不好吃")
    elif input1 == "2":
        print("米饭还行")
    elif input1 == "3":
        print("水饺芹菜馅")
    elif input1 == "4" or input1 == 'q':
        break
    else:
        print("输入错误：重新输入")

