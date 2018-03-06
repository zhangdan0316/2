# -*-coding:utf8 -*-
#题目：暂停一秒输出，并格式化当前时间。

import time
for i in range(2):
    print i
    time.sleep(1)
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

