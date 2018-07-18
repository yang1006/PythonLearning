#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用 __slots__      python 支持多重继承

# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。

class Student(object):
    __slots__ = ('name', 'age')    # 用tuple定义允许绑定的属性名称
    pass

s = Student()
s.name = 'yll'
# s.score = 90     报错，不能绑定该属性

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的


# 使用 @property  可以让调用者写出简短的代码，同时保证对参数进行必要的检查
# 把一个getter方法变成属性，只需要加上 @property 就可以了，
# 此时，@property 本身又创建了另一个装饰器 @score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

class Student1(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student1()
s.score = 70       # ok 实际转化为 s.set_score(60)
print(s.score)     # ok 实际转化为 s.get_score()
# s.score = 999    报错


# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):

    @property
    def birth(self):            # birth 可读可写
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
        pass

    @property
    def age(self):             # age 只读
        return 2018 - self._birth

# Exercise 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):

    @property
    def width(self):
        return self._width         # 不用写self.width 会循环调用方法本身

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')