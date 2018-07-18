#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for...in 循环，依次把list或tuple中的每个元素迭代出来
names = ['zhao', 'qian', 'sun']
for name in names:
    print(name)

# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
# range(5) 生成 0-4的list
print(list(range(5)))

sumCount = 0
for x in range(101):
    sumCount += x
    pass
print('1加到100=', sumCount)

# while 循环 计算100以内的奇数之和
n = 99
sumCount = 0
while n > 0:
    sumCount = sumCount + n
    n = n - 2
    pass
print('100以内奇数之和=', sumCount)

# break 提前退出循环， continue 跳过当前循环
n = 0
while n < 1000:
    n = n + 1
    if n % 2 == 1 and n % 4 == 1 and n % 5 == 1 and n % 6 == 3 and n % 7 == 0 and n % 8 == 1 and n % 9 == 0:
        print(n)
        break
