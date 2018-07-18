#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sorted 排序算法

l = [1, 5, 2, -10, 29, 56, -33]
print(sorted(l))

print(sorted(l, key=abs))

l1 = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(l1))
print(sorted(l1, key=str.lower))

# 反向排序
print(sorted(l1, key=str.lower, reverse=True))


# exercise 一组tuple表示学生名字和成绩： L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 用sorted()对上述列表分别按名字排序：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    if isinstance(t, tuple):
        return str(tuple(t)[0]).lower()

def by_score(t):
    if isinstance(t, tuple):
        return int(-tuple(t)[1])

print(sorted(L, key=by_name))
print(sorted(L, key=by_score))
