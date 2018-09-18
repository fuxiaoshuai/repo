#!/usr/bin/python
# -*- coding=utf-8 -*-
import string
import random
import sys

def main(passwd,times):
    for i in range(times):
        print(''.join(random.choices(string.ascii_lowercase+string.ascii_letters,k=passwd)))


main(int(sys.argv[1]),int(sys.argv[2]))


