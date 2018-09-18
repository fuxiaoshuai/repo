#!/usr/bin/python
# -*- coding=utf-8 -*-
import os
count = 0
l1 = os.listdir('/proc')
def name(num):
    for i in num:
        if i.isdigit():
            pass
        else:
            global count
            count += 1
            break
    else:
        l2 = (l1.remove(num))
    print(l2)
for a in l1:
    name(a)
print("文件夹数量为：%s" %count)
#print("程序号为：%s" %d)
