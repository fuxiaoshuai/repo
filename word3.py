#!/usr/bin/python
# -*- coding=utf-8 -*-
import os
import random
import shutil
import sys
#为打开一个相应的文件并调用shell命令
tem = (os.popen("cat /proc/meminfo | awk -F' ' 'NR==1{ print $2 }'").read())
返回值为1或零
os.system()

