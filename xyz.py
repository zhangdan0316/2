# -*- coding:utf8 -*-
#题目：输入三个整数x,y,z，请把这三个数由小到大输出。

x = int(raw_input("请输入x："))
y = int(raw_input("请输入y："))
z = int(raw_input("请输入z："))

if x > y and x > z:
    if y > z:
        print z, y, x
    else:
        print y, z, x
elif y < x <z:
    print y, x, z
elif x < y and x < z:
    if y < z:
        print x, y, z
    else:
        print x, z, y
else:
    print z, x, y



