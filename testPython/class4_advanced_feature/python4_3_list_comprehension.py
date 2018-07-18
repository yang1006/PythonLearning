#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式 List Comprehensions， 是Python内置的非常简单却强大的可以用来创建list的生成式。

import os
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
L = [x * x for x in range(1, 11)]
print(L)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

# 还可以使用两层循环，可以生成全排列：
L = [x + y for x in 'ABC' for y in 'XYZ']
print(L)


# 列出当前目录所有文件和目录
L = [d for d in os.listdir('.')]
print(L)

# 列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
L = [k + '=' + v for k, v in d.items()]
print(L)

# 把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
L = [d.lower() for d in L]
print(L)

# exercise 修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [d.lower() for d in L1 if isinstance(d, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')