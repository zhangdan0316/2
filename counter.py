# -*- coding: UTF-8 -*-
#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import string

chr = raw_input("请输入语句：")
digits = 0
letters = 0
space = 0
others = 0

for i in chr:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    elif i.isspace():
        space += 1
    else:
        others += 1
print 'letters=%d,digits=%d,space=%d,others=%d'%(letters,digits,space,others)



