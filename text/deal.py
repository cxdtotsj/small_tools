# -*- coding: utf-8 -*-
# @Data : 2020-04-10

'''
处理未正确分段落的文本

执行前, updated 文件需要清空
'''

import sys
import os

origin = os.path.join(os.path.dirname(__file__), 'origin.txt')
updated = os.path.join(os.path.dirname(__file__), 'up.txt')

print(origin)
print(updated)

with open(origin, 'r', encoding='utf-8') as ori:
    t = ''
    other = []
    for i in ori.readlines():
        if i is '\n':
            try:
                last_data = other[0]
            except IndexError:
                last_data
            if last_data is '\n':
                continue
            else:
                t += '\n'
        else:
            t += i.replace('\n', '')
        other.insert(0, i)

with open(updated, 'a', encoding='utf-8') as up:
    for i in t.split('\n'):
        # up.write(i+'\n'+'\n')
        up.write(i+'\n')

        