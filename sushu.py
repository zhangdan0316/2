# -*- coding:utf8 -*-
#题目：判断101-200之间有多少个素数，并输出所有素数。

from math import sqrt

t = 0
for i in range(101, 201):
    k = int(sqrt(i))
    for x in range(2,k+1):
        if i % x == 0:
            break
    if i % x != 0:
        print i
        t += 1
print 'total is %s' % t