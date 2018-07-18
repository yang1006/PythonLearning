#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数式编程 Functional Programming
# 一个变量可以指向一个函数，并且可以调用
print(abs(-10))
print(abs)
f = abs
print(f)
print(f(-10))
# 函数名也是变量,函数名其实就是指向函数的变量,对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！

# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, -6, abs))

def plus(x):
    return x + 1

print(add(1, 1, plus))

# 高阶函数 Higher-order function：  map/reduce, filter, sorted
# map: map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5])
print(list(r))               # 使用list()函数把惰性序列都计算出来并返回一个list

# 把list里所有数据转成字符串，只要一行代码
print(list(map(str, [1, 2, 3, 4, 5, 6])))


# reduce: reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是: reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 序列求和
from functools import reduce

def add(x, y):
    return x + y
print(reduce(add, [1, 2, 3, 4, 5]))  # 求和运算可以直接用Python内建函数sum()，没必要动用reduce。

# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

# map 和 reduce 结合写一个strToInt 函数

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn, map(char2num, "123144214")))

# exercise1 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[:1].upper() + name[1:].lower()
    # return str.capitalize(name)
    pass

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# exercise2 Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def multiply(x, y):
        return x * y
    return reduce(multiply, L)
    pass


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# exercise3 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456:
def str2float(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    p = s.split('.')
    # print(p[0], p[1])
    return reduce(fn, list(map(char2num, p[0]))) + reduce(fn, list(map(char2num, p[1]))) * 10 ** (-len(p[1]))  # **表示乘方

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')