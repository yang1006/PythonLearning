#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# 有关输入 输出 print中有逗号 打印语句会加个空格

print('this is your name', 'jack', '?')

print('100*25=', 100*25)

print('100*25=%s' % 2500)

print('100*25='+str(100*25))


name = input("please input you name:")
print('hello,', name)

num1 = input("做个乘法,输入乘数1：")
num2 = input("输入乘数2：")
num1 = int(num1)
num2 = int(num2)
print(num1, '*', num2, '=', num1*num2)

