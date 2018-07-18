#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类属性和实例属性

# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student1(object):
    def __init__(self, name):
        self.name = name

s = Student1('Bob')
s.score = 90

class Student(object):
    name = 'Student'
    pass

# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：
s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)

del s.name
print(s.name)

# 从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

# Exercise 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student2(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student2.count = Student2.count + 1

# 测试:
if Student2.count != 0:
    print('测试失败!')
else:
    bart = Student2('Bart')
    if Student2.count != 1:
        print('测试失败!')
    else:
        lisa = Student2('Bart')
        if Student2.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student2.count)
            print('测试通过!')
