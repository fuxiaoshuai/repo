#!/usr/bin/python
# -*- coding=utf-8 -*-
import string
import random
import sys
client = int(input("需要几位密码："))
shu = int(input("需要几位："))
while shu:
    a = ''.join((random.choices(string.ascii_letters+string.digits,k=client)))
    print(a)
    shu -= 1


