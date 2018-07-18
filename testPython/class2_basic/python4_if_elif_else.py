#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = 10
if x:
    print('只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。')
print('')

# exercise
# input 输入值时str型， 需要转换类型
sWeight = input('please input your weight(KG):')
sHeight = input('please input your height(M):')
nWeight = float(sWeight)
nHeight = float(sHeight)

bmi = nWeight / (nHeight * nHeight)
print('you bmi is: ', bmi)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')



