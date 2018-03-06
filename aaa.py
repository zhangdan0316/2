# -*- coding:utf8 -*-
#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

n = int(raw_input("请输入位数："))
b = raw_input("请输入一位数字：")
s = 0

for i in range(1, n+1):
    s += int(b*i)
print s


class a:
    def d(self):
        b = a()
