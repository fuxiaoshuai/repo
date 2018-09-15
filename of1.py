#!/usr/bin/python 
#-*- coding:utf-8 -*-
import os
a = (os.popen("cat /proc/meminfo | awk -F' ' 'NR==1{ print $2 }'").read())

