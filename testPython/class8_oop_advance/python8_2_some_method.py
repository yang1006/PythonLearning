#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定制类  class 中和__slots__，__len__()这样的更多有特殊用途的函数

# __str__

class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):     # 返回用户看到的字符串
        return 'Student object (name: %s)' % self.name

    def __repr__(self):    # 返回开发者看到的字符串，为调试服务的
        return 'Student object (name: %s)' % self.name


# __iter__ 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

# 以斐波那契数列为例，写一个Fib类，可以作用于for循环
class Fib(object):
    def __init__(self):      # 初始化2个计数器 a,b
        self.a = 1
        self.b = 1

    def __iter__(self):      # 实例本身就是迭代对象，所以返回自己
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b   # 计算下一个值
        if self.a > 1000:                          # 退出循环的条件
            raise StopIteration()
        return self.a                              #返回下一个值

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a

# for n in Fib():
#     print(n)


#  __getitem__ 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

f = Fib()
print(f[0])
print(f[10])

# 但是 list 有切片方法  list(range(100))[5:10], 所以应该判断传入的是int还是slice

class Fib1(object):
    def __init__(self):      # 初始化2个计数器 a,b
        self.a = 1
        self.b = 1

    def __iter__(self):      # 实例本身就是迭代对象，所以返回自己
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b   # 计算下一个值
        if self.a > 1000:                          # 退出循环的条件
            raise StopIteration()
        return self.a                              #返回下一个值

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib1()
print(f[0:10])

# 但是没有对step参数作处理：也没处理负数
print(f[0:10:2])
