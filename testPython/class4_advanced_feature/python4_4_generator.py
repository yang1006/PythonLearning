#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器 generator
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# 避免创建list占用大量内容空间

# 创建list
L = [x * x for x in range(10)]
print(L)
# 创建generator
g = (x * x for x in range(10))
print(g)

# for x in g:
#     print(x)

# 用循环写斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b   # a, b = b, a + b 相当于 a = b, b = a + b
        n = n + 1
    return 'done'
# print(fib(10))

# 函数里有 yield 关键字则函数变成了generator
# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
next(o)
next(o)
next(o)

def fibg(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b   # a, b = b, a + b 相当于 a = b, b = a + b
        n = n + 1
    return 'done'
f = fibg(6)
print(f)

for x in f:
    print(x)

# 用for 循环调用 generator时，拿不到return返回值，需要
g = fibg(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# exercise 把每一行看做一个list，试写一个generator，不断输出杨辉三角的下一行的list：

def triangles():
    l = [1]
    while True:
        yield l
        l = [l[i] + l[i + 1] for i in range(len(l) - 1)]
        l.insert(0, 1)
        l.append(1)

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
# print('results:', results)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')