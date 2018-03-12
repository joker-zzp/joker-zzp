# ufunc 对象
import numpy as np


a = np.array([0, 1, 2])
b = np.array([2, 3, 4])
np.add(a, b)
dir(np.add)
# 除此之外,大部分能够作用于数组的学习函数如三角函数等,都是ufunc对象
# 特别的,对于二元操作符所对应的ufunc对象,支持以下方法

# reduce方法
'''
op.reduce(a)
将op沿着某个轴应用,使得数组a的维数降低一维
add 作用到一维数组上相当于求和

y = add.recuce(a)
  = a[0] + a[1] + ... + a[N - 1]
    N-1
  = ∑ a[n]
    n=0
'''
a = np.array([1, 2, 3, 4])
np.add.reduce(a)
# 多维数组默认只按照第一维度进行计算
a = np.array([[1, 2, 3], [4, 5, 6]])
np.add.reduce(a)
# 指定维度
np.add.reduce(a, axis=1)
# 作用于字符串
b = np.array(['ab', 'cd', 'ef'], np.object)
np.add.reduce(b)
# 逻辑运算
c = np.array([1, 1, 0, 1])
np.logical_and.reduce(c)
np.logical_or.reduce(c)

# accumulate 方法
'''
op.accumulate(a)
accumulate 可以看成保存reduce 每一步的结果所形成的数组

    y = add.accumulate(a)
       ┌ 0      1           N-1   ┐
      =│ ∑a[n], ∑a=[n], ...,∑a[n] │
       └ n=0    n=0         n=0   ┘
与之前类似
'''

print('a =', a)
np.add.accumulate(a)
# 多维数组默认只按照第一维度进行计算
np.add.accumulate(a, axis=1)
print('b =', b)
np.add.accumulate(b)
print('c =', c)
np.logical_and.accumulate(c)
np.logical_or.accumulate(c)

# outer 方法
'''
op.outer(a, b)
对于a中每个元素,将op运用到它和b的每个元素上所得到的结果
'''
a = np.array([0, 1])
b = np.array([1, 2, 3])
np.add.outer(a, b)
np.add.outer(b, a)
