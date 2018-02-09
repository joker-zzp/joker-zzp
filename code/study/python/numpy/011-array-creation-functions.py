# 生成数组的函数

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


'''
arange
arange 类似于Python中的 range 函数，只不过返回的不是列表，而是数组：

arange(start, stop=None, step=1, dtype=None)
产生一个在区间 [start, stop) 之间，以 step 为间隔的数组，如果只输入一个参数，则默认从 0 开始，并以这个值为结束
'''

np.arange(4)
np.arange(1, stop=10, step=2, dtype=np.float64)
np.arange(0, 2 * np.pi, np.pi / 4)

# 由于存在精度问题,使用浮点数可能出现问题
np.arange(1.5, 2.7, 0.3)

'''
linspace
linspace(start, stop, N)

产生 N 个等距分布在 [start, stop]间的元素组成的数组，包括 start, stop

'''
np.linspace(0, 1, 5)

'''
logspace
logspace(start, stop, N)

产生 N 个对数等距分布的数组，默认以10为底
'''
np.logspace(0, 1, 5)

# meshgrid
# 有时候需要在二维平面中生成一个网格,这时候可以使用meshgrid 来完成这样的工作

x_ticks = np.linspace(-1, 1, 5)
y_ticks = np.linspace(-1, 1, 5)
x, y = np.meshgrid(x_ticks, y_ticks)
print(x)
print(y)


def f(x, y):
    """sinc 函数"""
    r = np.sqrt(x ** 2 + y ** 2)
    result = np.sin(r) / r
    result[r == 0] = 1.0
    return result


x_ticks = np.linspace(-10, 10, 51)
y_ticks = np.linspace(-10, 10, 51)

x, y = np.meshgrid(x_ticks, y_ticks, sparse=True)

z = f(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z,
                rstride=1, cstride=1,
                cmap=cm.YlGnBu_r)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

# ogrid, mgrid
'''
Matlab中有 meshgrid 的用法：

meshgrid(-1:.5:1, -1:.5:1)

Numpy的 meshgrid 并不支持这样的用法，但我们可以使用 ogrid / mgrid 来实现类似这样的用法。

ogrid 与 mgrid 的区别在于：

ogrid 相当于 meshgrid(indexing='ij', sparse=True)
mgrid 相当于 meshgrid(indexing='ij', sparse=False)
'''

x, y = np.ogrid[-1:1:.5, -1:1:.5]
print(x)
print(y)

x, y = np.ogrid[-10:10:51j, -10:10:51j]
print(x, y)
z = f(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z,
                rstride=1, cstride=1,
                cmap=cm.YlGnBu_r)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
# 这里交换了x, y的输入顺序

# r_, c_
'''
我们可以使用 r_ / c_ 来产生行向量或者列向量。
'''
# 使用切片产生
np.r_[0:1:.1]
# 复数步长制定数组长度
np.r_[0:1:5j]
# 连接多个序列，产生数组
np.r_[(2, 33, 11), 2.2, [3., 5]]
# 列向量
np.c_[1:3:5j]

# ones, zeros

'''
ones(shape,dtype=float64)
zeros(shape,dtype=float64)
生产一个制定形状的全0或全1的数组,还可以制定数组类型
'''
np.zeros(3)
np.ones([2, 3], dtype=np.float32)

# 生产一个全是5的数组
np.ones([2, 3]) * 5

# empty
'''
empty(shape, dtype=float64, oder='C')
也可以使用empty方法产生一个制定大小的数据(数组所指向的内存未被初始化,所以值随机),再用fill 方法填充
'''
a = np.empty(2)
print(a)
a.fill(5)
print(a)

# 另外一种替代方法使用索引,不过速度会少慢一些
a[:] = 5


# empty_like, ones_like,zeros_like
'''
empty_like(a)
ones_like(a)
zeros_like(a)

产生一个跟 a 大小一样，类型一样的对应数组.
'''
a = np.arange(0, 10, 2.5)
print(a)

np.empty_like(a)
print(a)

np.zeros_like(a)
print(a)

print(np.ones_like(a))

# identity
'''
indentity(n, dtype=float64)
产生一个 n 乘 n 的单位矩阵
'''

np.identity(3)
