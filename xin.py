#!/usr/bin/python
# -*- coding=utf-8 -*-

l1 = [0,1]
def name(num):
    for i in range(num - 2):
        l1.append(l1[-1] + l1[-2])

name(10)
print(len(l1))

