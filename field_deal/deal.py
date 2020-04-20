# -*- coding: utf-8 -*-
# @Data : 2020-03-30

'''
处理字段，转换成list

'''

import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
fd = os.path.join(path, 'f.txt')

fields = []
with open(fd, 'r') as f:
    for i in f.readlines():
        # i.strip()
        fields.append(i.strip())
print(fields)
print(len(fields))