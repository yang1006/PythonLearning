#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 注释 有关代码缩进
# :号结尾时，缩进的语句视为代码块
# 按照约定俗成的管理，应该始终坚持使用4个空格的缩进。
# Python程序是大小写敏感的
a = 100
if a >= 0:
	print(a)
else:
	print(-a)

# 允许用r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')

# Python允许用'''...'''的格式表示多行内容
print('''line
line2
line3''')

print(r'''hello,\n
world''')

print(3 > 2)
print(3 < 2)

print(True and False)
print(True or False)
print(not True)

# python 里空值用 None 表示
print(None)

# 这里b 还是指向 'ABC'
a = 'ABC'
b = a
a = 'XYZ'
print(b)


