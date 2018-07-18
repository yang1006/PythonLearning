#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器 Decorator ： 在代码运行期间动态增加功能, 本质上 decorator 就是一个返回函数的高阶函数

def now():
    print('2018-02-03')

# 函数对象有个 _name_ 方法可以拿到函数的名字
print(now.__name__)

# 定义一个打印日志的 装饰器

def log(func):
    def wrapper(*args, **kwargs):
        print('调用 %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log                 #把 @log 放到 now1() 函数的定义处，相当于执行了语句：now1 = log(now1)
def now1():
    print('2018-02-03 now1')

now1()

f = now1
print(f.__name__)    # 结果是wrapper


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log2(text):
    def decorator(func):
        # @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log2('执行了函数')              #相当于执行 now2 = log2('执行了函数')(now2)
def now2():
    print("2018-02-03 now2")
now2()
print(now2.__name__)           # 结果是wrapper

# 需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# Python内置的 functools.wraps 就是干这个事
# 只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。

import functools, time
def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('调用 %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log3
def now3():
    print("2018-02-03 now3")
now3()
print(now3.__name__)

# Exercise1 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print('%s executed in %s ms' % (fn.__name__, end_time - start_time))
        return result
    return wrapper


# 测试
print('开始测试')
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功')

# Exercise2 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def log_begin_end(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('begin call %s():' % func.__name__)
        func(*args, **kwargs)
        print('end call %s():' % func.__name__)
    return wrapper
@log_begin_end
def test():
    print('test')
test()


# Exercise 3 再思考一下能否写出一个decorator，使它既支持@log, 又支持@log('execute')

def log_perfect(text=None):
    if not isinstance(text, str):     # todo 判断一个参数是函数，这里只简单判断了不是str类型
        @functools.wraps(text)
        def wrapper(*args, **kwargs):
            print('无参数 执行了 %s():' % text.__name__)
            return text(*args, **kwargs)
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print('有参数 %s 执行了 %s():' % (text, func.__name__) )
                return func(*args, **kwargs)
            return wrapper
        return decorator

@log_perfect
def test111():
    print('test111')

test111()

@log_perfect('execute')
def test222():
    print('test222')
test222()





