#!/usr/bin/python
# -*- coding=utf-8 -*-
import os
import shutil
input_path = input("输入你想创建的目录:")
if not os.path.exists(input_path):
    print("文件夹或者文件不存在%s" %(input_path))
    print('*' * 30)
    os.makedirs(input_path)
    if os.path.exists(input_path):
        print("创建成功%s" %(input_path))
elif not os.listdir(input_path):
    print("文件夹为空%s" %(input_path))
