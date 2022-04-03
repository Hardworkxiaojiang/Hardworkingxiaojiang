# -*- coding = utf-8 -*-
# @Time : 2022/4/3 10:19
# @Author :蒋大帅
# @File : 利用for和while循环练习九九乘法表.py
# @Software:PyCharm


for a in range(1,10):
    for b in range(1,10):
        if b<=a:
            print(f'{a}*{b}={a*b}',end='\t')
    print('\n')


