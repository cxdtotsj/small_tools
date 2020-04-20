# -*- coding: utf-8 -*-
# @Data : 2020-04-10

'''
处理未正确分段落的文本

执行前, updated 文件需要清空
'''

import sys
import os

origin = os.path.join(os.path.dirname(__file__), 'origin.txt')
updated = os.path.join(os.path.dirname(__file__), 'updated.txt')

with open(origin, 'r', encoding='utf-8') as ori:
    t = ''
    for i in ori.readlines():
        if i is '\n':
            t += '\n' 
        else:
            t += i.replace('\n', '')

with open(updated, 'a', encoding='utf-8') as up:
    for i in t.split('\n'):
        up.write(i+'\n'+'\n')
        
        