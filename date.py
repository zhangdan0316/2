# -*- coding: utf8 -*-
#题目：输入某年某月某日，判断这一天是这一年的第几天？

daysa = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = int(raw_input("please input year: "))
month = int(raw_input("please input month: "))
day = int(raw_input("please input day: "))
suma = 0

for i in range(0, month-1):
    if i <= month:
        suma += daysa[i]
if year % 4 == 0 and year % 100 != 0:
    sumb = suma + day + 1
    print '这是%s年的第%s天' % (year,sumb)
elif year % 100 == 0 and year % 400 == 0:
    sumb = suma + day + 1
    print '这是%s年的第%s天' % (year,sumb)
else:
    sumb = suma + day
    print '这是%s年的第%s天' % (year,sumb)



