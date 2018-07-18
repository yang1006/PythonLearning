#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# list
classmates = ['yang', 'li', 'chen']
print(classmates)
print(len(classmates))

# 下标索引
print(classmates[0], classmates[1], classmates[2])

# -1表示直接获取最后一个元素，类推 -2表示倒数第2个，也有越界
print(classmates[-1])

# 追加元素
classmates.append("wang")
print(classmates)

# 插入元素
classmates.insert(1, 'wen')
print(classmates)

# 删除元素
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)

# 替换元素
classmates[0] = classmates[0] + "替换后"
print(classmates)

# list元素类型可以不同, 元素还可以是一个list
l = [1, "sss", True, [111, 222], classmates]
print(l)
print("")

# tuple 元组. tuple一旦初始化就不能修改,没有 append 和 insert 方法，不可变所以安全
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print(t)

# 只有1个元素的tuple定义时必须加一个逗号 , 来消除歧义
t = (1)  # 这是其实表示是数学公式中的小括号，相当于 t = 1
print(t)
t = (1,)
print(t)  # python 输出时也会输入一个逗号 , 避免你理解成数学中的括号


# exercise
print("")
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])


