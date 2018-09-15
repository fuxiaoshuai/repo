#!/usr/bin/python 
#-*- coding:utf-8 -*-
import random
prompt ="""(0)石头
			(1)剪刀
			(2)布
			请选择（0/1/2）:"""
all_choice = ["石头","剪刀","布"]
win_list = ["石头","剪刀"],["剪刀","布"],["布","石头"]
list = ['1','2','0']
h = 0
c = 0
while h < 2 and c < 2:
    index = input(prompt)
    if index == '':
        break
    elif index in list:
        index = int(index)

        player = all_choice[index]
        comper = random.choice(all_choice)
        print("玩家选择：%s,电脑选择：%s" % (player, comper))
        if (player) == (comper):
            print("平局")
        elif [player, comper] in win_list:
            h += 1
        else:
            c += 1
    else:
        print("请正确输入！")
if h == 2:
    print("you win")
elif c == 2:
    print("you lose")
