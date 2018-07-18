#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）

# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
print(10 / 3)
print(9 / 3)

# // 地板除 整数除法结果是整数 相当于java 里的 /
print(10 // 3)
print(9 // 3)

# % 取余数
print(10 % 3)
print(9 % 3)
print("")

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
print('中文能显示正常吗')
print('abc转换成bytes ', 'abc'.encode('utf-8'))
print('b\'abc\'转换成str ', b'abc'.decode('utf-8'))

print(ord('A'))
print(chr(65))
print('len(\'abc\')=', len('abc'))
print('len(\'中文\')=', len('中文'))
print('len(\'中文\'.encode(\'utf-8\'))=', len('中文'.encode('utf-8')))
print('')


# 占位符 %d 整数，%f 浮点数， %s 字符串，%x 16进制整数
# 整数和浮点数还可以指定是否补0和整数与小数的位数
# %% 转义来表示一个%
print('%3d-%03d' % (3, 1))
print('%.2f' % 3.14159)

s1 = 72
s2 = 85
growth = (s2 - s1) / s1
s = 'growth rate: %.1f%%' % (growth * 100)
print(s)
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))


# exercise
print("")
print(123)
print(456.789)
print('\'Hello,world\'')
print('\'Hello, \\\'Adam\\\'\'')
print('r\'Hello,\"Bart\"\'')
print('r\'\'\'Hello')
print('Lisa!\'\'\'')

