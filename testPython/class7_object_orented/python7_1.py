#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一个类
# 类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
class Student(object):    # 访问限制
    # 直接在class中定义的属性时类属性，归Student所有
    # 千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
    __name_s = ''           # 实例的变量名如果以__开头，就变成了一个私有变量（private）
    __score_s = 0           # 不能用__name__、__score__这样的变量名。
    _name = ""             # 虽然我可以被访问，但是，请把我视为私有变量，不要随意访问
    def __init__(self, name, score):   #相当于构造方法
        self.__name = name
        self.__score = score

    def print_scroe(self):
        print('name: %s score %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

student = Student('yll', 100)
student.print_scroe()
print(student.get_grade())


# Exercise 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):   # 同一个文件里两个相同名字的类，后者会把前者覆盖？

    name = ''
    __gender = ''

    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
