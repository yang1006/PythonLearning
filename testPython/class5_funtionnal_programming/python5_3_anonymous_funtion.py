#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 匿名函数  lambda
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

map(lambda x: x * x, [1, 2, 3])

# 匿名函数 lambda x: x * x 实际就是

def f(x):
    return x * x

# 可以把匿名函数赋值给一个变量
f1 = lambda x: x * x
print(f1)

# 也可以把匿名函数作为返回值返回

def build(x, y):
    return lambda: x * x + y * y

q = build(2, 3)
print(q())

# Exercise 请用匿名函数改造下面的代码：

def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)

