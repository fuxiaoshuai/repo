#!/usr/bin/python
# -*- coding=utf-8 -*-
w = '/root/ls'
r = '/bin/ls'
w1 = open(w,'wb')
r1 = open(r,'rb')
while True:
    date = r1.read()
    if not date:
        break
    else:
        w1.write(date)
w1.close()
r1.close()
