#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用 type()

# 基本类型都可以用type()判断
print(type(123))
print(type('abc'))
print(type(None))


# 如果一个变量指向函数或者类，也可以用type()判断：

class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

def fn(x):
    pass

print(type(abs))
a = Animal()
print(type(a))
dog = Dog()
print(type(dog))

# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：

print(type(123) == int)
print(type('abc') == str)

# 判断一个对象是否是函数怎么办？ 可以使用types模块中定义的常量：
import types
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
print(type(abs) == types.FunctionType)


# 使用isinstance(), 能用type()判断的基本类型也可以用isinstance()判断：
# 优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

a = Animal()
dog = Dog()
h = Husky()

print('husky is Dog ?', isinstance(h, Dog))
print('husky is Animal ?', isinstance(h, Animal))
print('dog is Husky ?', isinstance(dog, Husky))

# 使用 dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('abc'))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len('abc'))
print('abc'.__len__())

# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
setattr(obj, 'x', 10)
print(getattr(obj, 'x', 0))

print(getattr(obj, 'y', -1))     # 不设置默认值-1时，如果没有该属性会报错 AttributeError

# 也可以获得对象的方法：
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
