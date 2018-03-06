# -*- coding:utf8 -*-
#题目：斐波那契数列。
#程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

a = [0, 1]
n = int(raw_input("请输入数列长度："))
for i in range(2, n):
    b = a[i-1] +a[i-2]
    a.append(b)
print a



