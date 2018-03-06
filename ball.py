# -*- coding:utf8 -*-

#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

# -*- coding:utf8 -*-
hlist = [100, ]
h = 100
for i in range(1, 11):
    h /= 2.0
    hlist.append(2*h)
    print h, sum(hlist)

