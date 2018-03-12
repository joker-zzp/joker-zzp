#! /usr/bin/python3
# 二次元运算

import numpy as np


# 四则运算
'''
a + b    add(a, b)
a - b    subtract(a, b)
a * b    multiply(a, b)
a / b    divide(a, b)
a ** b   power(a, b)
a % b    remainder(a, b)

'''
a = np.array([1, 2])
print(a * 3)

# 数组逐元素相乘
b = ([3, 4])
print(a * b)
# 使用函数
print(np.multiply(a, b))
# 事实上,函数还可以接收第三个参数,表示讲结果存入第三个参数中
temp = np.array([])
temp.resize(2,)
np.multiply(a, b, temp)
print(temp)

# 比较和逻辑运算
'''
运算   函数
==    equal
!=    not_equal
>     greater
>=    greater_equal
<     less
<=    less_equal
      logical_and
      logical_or
      logical_xor
      logical_not
&     bitwise_and
      bitwise_or
^     bitwise_xor
~     invert
>>    right_shift
<<    left_shift
'''

# 等于操作也是逐元素比较的
a = np.array([[1, 2, 3], [2, 3, 4]])
b = np.array([[1, 3, 2], [2, 3, 1]])
print(a == b)

# 这意味着如果我们在条件中要判断两个数组是否一样时，不能直接使用　if a == b
# 而是要用
if np.all(a == b):
    print('yes')

# 对于浮点数，由于存在精度问题，使用函数allclose 会更好
if np.allclose(a, b):
    print('yes')

# logical_and 也是逐元素的and操作
a = np.array([1, 2, 0])
b = np.array([2, 2, 3])
print(np.logical_and(a, b))
# 比特操作
print(a | b)
# 取反
print(~a)
# 左移
print(a << 3)
# 要注意的是 & 的运算优先于比较运算,所以必要时需要加上括号
a = np.array([1, 2, 5, 4])
b = np.array([16, 32, 64, 128])
print((a > 3) & (b < 100))
