#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 内置了很多函数 http://docs.python.org/3/library/functions.html#abs

# 使用 help(函数名) 查看函数的帮助信息
help(abs)

print(max(1, 2, 3, 5, 10))
print(min(1, 2, 3, 5, 10))

# 数据转换
print('')
print(int('123'))
print(int(12.34))
print(float('12.33'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
print('')
a = abs
print(a(-100))

# exercise 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
# n1 = 255, n2 = 1000
print('')
print(hex(255))
print(hex(1000))


