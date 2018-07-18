#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filter() 函数过滤序列
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素

# 一个list中只保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))


# 计算素数的一个方法是埃氏筛法
def _odd_iter():    # 从3开始的一个无限奇数序列
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda y: y % n > 0    # lambda相当于函数速写，允许在代码中嵌入一个函数的定义

def primes():
    yield 2
    it = _odd_iter()
    while True:
        x = next(it)
        yield x
        it = filter(_not_divisible(x), it)

# 打印100以内的素数:
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break

# exercise 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数:
def is_palindrome_1(n):
    s = str(n)
    s1 = s[::-1]     # 倒序
    return s == s1

def is_palindrome(n):
    ll = list(str(n))
    ll.reverse()
    m = int("".join(ll))
    return m == n


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
