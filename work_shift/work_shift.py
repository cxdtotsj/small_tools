# -*- coding: utf-8 -*-
# @Data : 2020-11-04


import time
from datetime import datetime, timedelta

# now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# print(now_time)

# work_times = 

# 中午 12 点是白班

first_work_time = datetime(year=2020, month=11, day=28, hour=6, minute=0, second=0)

work_day_time = 15

at_work = 15

at_home = 21

work_night_time = 15


# first_home_time = first_work_time + timedelta(hours=15)
# last_home_time = first_home_time + timedelta(hours=21)

# print(first_home_time.strftime('%Y-%m-%d %H:%M:%S'))
# print(last_home_time.strftime('%Y-%m-%d %H:%M:%S'))


def word_shift(first_work_time, shifts):

    '''
    first_work_time: 开始工作的初始日期
    shifts: 工作班次

    假设: 工作时长为 15h, 在家时间为 21h, 白班和夜班是一致的
    
    '''

    at_home_time = []
    for i in range(shifts):
        first_home_time = first_work_time + timedelta(hours=15)
        first_work_time = first_home_time + timedelta(hours=21)
        at_home_time.append('{}--{}'.format(first_home_time.strftime('%Y-%m-%d %H:%M:%S'), first_work_time.strftime('%Y-%m-%d %H:%M:%S')))
    return at_home_time



if __name__ == "__main__":
    first_work_time = datetime(year=2020, month=11, day=28, hour=6, minute=0, second=0)
    print(word_shift(first_work_time, 3))

    print('在家的时间段')
    for w in word_shift(first_work_time, 100):
        print(w)