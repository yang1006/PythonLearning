#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# 定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型错误 应该是int 或float')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))

# pass pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass

age = 10
if age >= 18:
    pass

# my_abs('A')  抛出异常

# 返回多个值
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 其实返回的是一个tuple, 多个变量可以同时接收一个tuple，按位置赋给对应的值
r = move(100, 100, 60, math.pi / 6)
print(r)

# exercise 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#  ax2 + bx + c = 0 的两个解。
def quadratic(a, b, c):
    if not isinstance(a, (int, float))or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('参数类型错误 应该是int 或float')
    # print('计算 %dx²+%dx+%d=0 结果如下' % (a, b, c))
    if b * b - 4 * a * c < 0:
        return TypeError('b²- 4ac < 0 无解')
    if a == 0:
        return -c / b
    else:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 / a
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 / a
        return x1, x2

# print(quadratic(1, 8, 4))


# 测试:
print('')
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
