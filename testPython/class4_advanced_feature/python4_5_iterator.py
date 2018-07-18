#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代器  Iterator

# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# Iterator 是惰性的，只在next()时计算下一个数据

from collections import Iterable, Iterator

print('是否是可迭代对象 Iterable：')
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print('是否是迭代器 Iterator：')
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print('使用iter()函数把 Iterable 变成 Iterator')
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
