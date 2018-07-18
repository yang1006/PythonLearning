#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 偏函数 Partial function

print(int('12345'))    # 默认按10进制转换
print(int('12345', base=8))  # base参数，按 N 进制转换
print(int('12345', base=16))    # 按16进制转换

# 转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去

def int2(x, base=2):
    return int(x, base=base)
print(int2('10'))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单

import functools

int2 = functools.partial(int, base=2)
print(int2('10'))
print(int2('10', base=10))  # 依然可以传入其他值

# 创建偏函数时，实际上可以接收函数对象、*args 和 **kw 这3个参数，当传入：
# int2 = functools.partial(int, base=2)
# 相当于：
# kw = { 'base': 2 }
# int('10010', **kw)

# 当传入
max2 = functools.partial(max, 10)
# 时，实际上会把10作为*args的一部分自动加到左边

max2(5, 6, 7)   # 相当于

args = (10, 5, 6, 7)
max(*args)

