#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict和set使用
# dict相当于java中的map, 选择不可变对象作为key很重要，最常用的key是字符串。
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# set和dict一样，不可以放入可变对象，因为无法判断两个可变对象是否相等
# 所以tuple可以作为dict和set的key，但是list不能，包含了list的tuple也不能

# 生成一个dict
d = {'yang': 25, 'xu': 26, 'chen': 27}
print(d)

d['yang'] = 30
print(d['yang'])

print('yang in d ?', 'yang' in d)
print('zhang in d ?', 'zhang' in d)

print(d.get('zhang'))
print(d.get('zhang', -1))

# 删除一个key
d.pop('chen')
print(d)

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 创建set 需要提供一个list作为输入集合：
s = set([1, 2, 2, 3])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
s.add(5)
s.add(5)
print(s)
# 通过remove(key)方法可以删除元素：
s.remove(4)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print('s1 & s2 =', s1 & s2)
print('s1 | s2 =', s1 | s2)

# list 不能作为dict、set的key
l = [1, 2, 3, 3]
print(l)
# d = {l: "aaa", "kkk": "kkk"}
s = set(l)
print(s)   # {1, 2, 3}

# l = [1, 2, 3, 3, [1, 2]]
# s = set(l)  # 报错

# exercise tuple 试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果
t1 = (1, 2, 3)
t2 = (1, [2, 3])

d = {t1: 1}
# d = {t2: 1}  # 报错
print(d)

s = set(t1)
# s = set(t2)  # 报错
print(s)


