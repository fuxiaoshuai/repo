#!/usr/bin/python
# -*- coding=utf-8 -*-
import string
import random
import sys
def pas(num,time):
    while time:
        print(''.join(random.choices(string.digits+string.ascii_letters,k=6)))
        time -= 1


pas(int(sys.argv[1]),int(sys.argv[2])



