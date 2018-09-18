#!/usr/bin/python
import os
tem = (os.popen("cat /proc/meminfo | awk -F' ' 'NR==1{ print $2 }'").read())
free = (os.popen("cat /proc/meminfo | awk -F' ' 'NR==2{ print $2 }'").read())
nei = (int(tem) - int(free)) / int(tem)
print("此服务器内存使用率为:%.2f%%" %(nei * 100))

