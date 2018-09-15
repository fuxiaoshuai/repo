#!/usr/bin/python 
#-*- coding:utf-8 -*-
with open('/proc/meminfo') as f1:
    for f in f1:
        if f.startswith('MemTotal'):
            a = int(f.split()[1])
            print(a)
            continue
        if f.startswith('MemFree'):
            b = int(f.split()[1])
            print(b)
            break
print("%.2f%%" %((a - b) / a * 100))
