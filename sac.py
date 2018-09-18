#!/usr/bin/python
# -*- coding=utf-8 -*-
import sys
def function(a):
    for a in '0123456789':
        if a:
            print("是一个纯数字")
            pass
        else:
            print("不是一个纯数字")
            break
    else:
        print("是一个纯数字")

function(sys.argv[1])
