#!/usr/bin/python
# -*- coding=utf-8 -*-
import string
import random
import sys
def pas(num,time):
    while time:
        print(''.join(random.choices(string.ascii_lowercase+string.ascii_letters,k=num)))
        time -= 1


pas(8,6)



