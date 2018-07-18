#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，
# 还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# 1、默认参数 必选参数在前，默认参数在后，否则Python的解释器会报错
# 定义默认参数要牢记一点：默认参数必须指向不变对象！不然下次调用时内容就变了
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5, 3))

print('')
def enroll(name, gender, age=6, city='北京'):
    print('name:', name)
    print('gender', gender)
    print('age', age)
    print('city', city)

enroll('Jack', 'Male')
enroll('Rose', 'Female', city='上海')

# 坑 默认参数必须指向不变对象！不然下次调用时内容就变了
def add_end(L=[]):
    L.append('END')
    print(L)

add_end()
add_end()  # 这里会打印['END', 'END']


def add_end1(L=None):
    if L is None:
        L = []
    L.append('END')
    print(L)

add_end1()
add_end1()  # 这里就不会有问题

# 2、可变参数 参数前面加了 * 号,number接收到的是一个tuple
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*number):
    s = 0
    for n in number:
        s = s + n
    print(s)
    return s

calc()
calc(1)
calc(1, 2, 3)
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
num = [1, 2, 3, 4]
calc(*num)

# 3、关键字参数  参数前面加 **
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# 可以只传必选参数
person("yang", 20)

# 也可以传任意个数的关键字参数
person("zhang", 10, city='bj', job='teacher')
person('li', 20, city='sh', job='doctor', salary='3000')

# 和可变参数一样，也可以先组装一个dict，然后把dict转换层关键字参数传进去
extra = {'city': '北京', 'job': 'doctor', 'salary': "4000"}
person('wang', 25, **extra)

# 4、命名关键字函数 限制关键字参数的名字
# *后面的参数被视为命名关键字参数。
# 可以有默认值，有默认值时就可以不传，其他时候都必须传
def person1(name, age, *, city='北京', job):
    print(name, age, city, job)

person1('yang', 11, city='北京', job='Doctor')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)

person2('li', 222, 1, 2, 3, city='上滑', job='医生')

# 5、参数组合 顺序必须是  必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def fun1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def fun2(a, b, c=0, *d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    pass

fun1(1, 2)
fun1(1, 2, c=3)
fun1(1, 2, 3, 'a', 'b')
fun1(1, 2, 3, 'a', 'b', x='x', y='y')
fun2(1, 2, d=99, ext=None)

# exercise 接收1个或多个数并计算乘积
def product(*list):
    result = 1
    for y in list:
        if not isinstance(y, (int, float)):
            raise TypeError('参数类型错误 应该是int 或float')
        else:
            result = result * y

    print('计算结果:', result)
    return result


product(1, 2, 3, 4, 5)