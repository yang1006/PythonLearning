#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片 slice 对list，tuple和字符串进行截取

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# L[0:3]表示从0开始取，直到索引3为止，但不包括3
print(L[0:3])
# 如果是从0开始，0还可以省略
print(L[:3])
# 从索引1取到3
print(L[1:3])

# 支持取倒数第几个元素
# 倒数第2个元素到最后一个元素
print(L[-2:])

# 倒数第2个元素到最后一个元素（不含最后一个元素）
print(L[-2:-1])

L = list(range(100))
print(L)
# 可以使用切片轻松取出某一段数列
print(L[:10])    # 前10个数
print(L[-10:])   # 后10个数
print(L[10:20])  # 第11-20个数

print(L[0:10:2])  # 前10个数，每两个取一个
print(L[::5])     # 所有数，每5个取一个

L1 = L[:]         # 直接复制一个list
print(L1)

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print((1, 2, 3, 4, 5)[0:3])

# 字符串也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串

print('ABCDEFG'[0:3])
print('ABCDEFG'[::2])

# 左后一个参数为负数，表示逆序
print('ABCDEFG'[::-1])
print('ABCDEFG'[::-2])

# exercise 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法

def trim1(s):
    if not isinstance(s, str):
        raise TypeError('input must be str')
    st = 0
    length = len(s)
    end = length - 1
    while st < length and s[st:st+1] == ' ':
        st += 1

    while end >= 0 and s[end:end+1] == ' ':
        end -= 1

    if st < end:
        s = s[st: end+1]
    else:
        s = ''
    print(s)
    return s

# 更简洁
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')