#!/usr/bin/python
# -*- coding=utf-8 -*-
def file(path,newpath):
    with open(newpath,'w') as d:
        try:
            with open (path,'r') as f:
                for a in f:
                    b = a
                    d.write(b)
        except FileNotFoundError:
            print("正确输入文件路径：")
        else:
             print("已经复制完成")


file('/proc/meminfo','/a')


