#!/usr/bin/python
# -*- coding=utf-8 -*-
cent = 0
import os
def cheng(num):
    for i in num:
        if not i.isdigit():
            return False
        else:
            return True

for a in os.listdir('/proc'):
    if cheng(a):
        cent += 1
print(cent)



