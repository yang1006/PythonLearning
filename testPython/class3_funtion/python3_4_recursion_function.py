#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 递归函数

# 计算阶乘

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(6))

# 尾递归形式： 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 如果尾递归做了优化是可以解决递归调用栈溢出的
# 但是 Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

def fact1(n):
    return fact_item(n, 1)
    pass

def fact_item(num, product):
    if num == 1:
        return product
    return fact_item(num - 1, num * product)

# exercise  汉诺塔的移动
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
# https://www.zhihu.com/question/37152936 

def move(n, a='A', b='B', c='C'):
    if n == 1:
        print(a, '--->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
    pass

move(3)

