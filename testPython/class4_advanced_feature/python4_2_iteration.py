#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代 Iteration

# Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
# dict 迭代出的结果顺序可能不一样
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

# 可以同时迭代 key 和 value
for key, value in d.items():
    print(key, value)

# 字符串可以迭代
for ch in 'ABC':
    print(ch)

# 判断一个对象是否可以迭代
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# 下标迭代 enumerate函数可以把一个list变成索引-元素对
for i, key in enumerate(d):
    print(i, key)

# 同时引用两个变量，很常见
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)

# exercise 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if not isinstance(L, Iterable) or len(L) == 0:
        return (None, None)
    min_value = L[0]
    max_value = L[0]
    for x in L:
        if min_value > x:
            min_value = x
        if max_value < x:
            max_value = x
    return (min_value, max_value)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
