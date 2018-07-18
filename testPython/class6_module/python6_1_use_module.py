#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'yll'

# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
# 运行python3 python6_1_use_module.py 获得的sys.argv就是['hello.py']；
# 运行python3 python6_1_use_module.py Michael获得的sys.argv就是['hello.py', 'Michael]。

import sys      #导入sys模块

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments')


# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
    test()


# 作用域
# 1、正常函数和变量都是public的  如 abc, x123, pi等
# 2、__xxx__这样的变量是特殊变量，可以被直接引用，但是用特殊用途，我们自己的变量一般不要用这种变量名
# 3、_xxx,__xxx 这样的函数和变量是非公开 private 的，不能被直接引用，如_abc, __abc等

