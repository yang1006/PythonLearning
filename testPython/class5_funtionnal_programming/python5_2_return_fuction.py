#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 返回函数 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数

f = lazy_sum(1, 2, 3, 4)
print(f)

# 调用f时，才真正的计算
print(f())

# 闭包 Closure
# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力

# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

f1 = lazy_sum(1, 2, 3, 4)
f2 = lazy_sum(1, 2, 3, 4)
print(f1 == f2)

# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其 <!!!内部的局部变量还被新函数引用!!!>

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())     # 结果全是9， 因为i一直被引用，执行的时候已经变成了3

# 所以 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))     # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# exercise 利用闭包返回一个计数器函数，每次调用它返回递增整数:
def createCounter():     # 1创造一个生成器
    def add1():
        n = 0
        while True:
            n = n + 1
            yield n
    f = add1()
    def counter():
        return next(f)     # 不能直接next(add1())，因为createCounter 返回的是 counter 这个函数，而此时 f() 并没有执行并返回一个生成器对象。
    return counter         # 所以每次 createCounter() 都会得到一个 counter 函数，而执行 counter()，都会执行 f() 而生成一个新的生成器对象

def createCounter1():   # 2使用列表（列表list是全局变量）
    fs = [0]
    def counter():
        fs[0] = fs[0] + 1
        return fs[0]
    return counter

def createCounter2():    # 3使用nonlocal关键字，将局部变量变成全局变量
    n = 0
    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())    # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')