# 数组的形状

import numpy as np

a = np.arange(6)

# 将形状修改为2乘3
print(a)

a.shape = 2, 3
print(a)

# 与之前对应的方法是reshape,但是它不会改变原来数组的值，而是反回一个新的数组
a.reshape(3, 2)

a

# 使用 newaxis 增加数组维数
a = np.arange(3)
np.shape(a)
a
y = a[np.newaxis, :]
print('\n', y)
np.shape(y)
y = a[:np.newaxis]
np.shape(y)
y = a[np.newaxis, np.newaxis, :]
np.shape(y)

# squeeze 方法去除多余的轴
a = np.arange(6)

a.shape = (2, 1, 3)
b = a.squeeze()
b.shape
# squeeze 返回一个将所有长度为1的维度去除的新数组


# 数组转置
a
# 使用 transpose 返回数组的转置，本质上是将所有维度反过来
a.transpose()  # 对于二维数组相当与换行和列
# 或者使用缩写属性
b = a.T
# 注意：
# ·对于复数数组，转置并不反回共轭，只是单纯的交换轴的位置
# ·转置可以作用于多维数组

a = np.arange(60)
a
a.shape = 3, 5, 4
print(a)
b = a.T
b.shape
# 转置只是交换了轴的位置
# 另一方面，转置返回的是对原数组的另一种view，所以改变转置会改变原数组的值

a = np.arange(6)
a.shape = 2, 3
print(a)

# 修改转置
b = a.T
b[0, 1] = 39  # 原数组也更改
a

# 数组的连接
# 有时我们要将不同的数组按照一定的顺序连接起来
# concatenate((a0,a1,a2,a3...,aN), axis=0)
# 注意这些数组要用()包括到一个元组去
# 除了给定的轴外，这些数组其他轴的长度必须一样

x = np.array([
    [0, 1, 2],
    [10, 11, 12]
])

y = np.array([
    [50, 51, 52],
    [60, 61, 62]
])

print(x.shape)
print(y.shape)

z = np.concatenate((x, y))
print(z.shape)
print(z)

z = np.concatenate((x, y), axis=1)
print(z.shape)
print(z)

# 注意到这里x 和y 的形状是一样的，还可以将他们链接成三维的数组,但是concatenate不能提供这样的功能，不过可以这样
z = np.array((x, y))
print(z.shape)
print(z)

# 实际上，Numpy提供了分别对应这三种情况的函数：
# ·vstack
# ·hstack
# ·dstack
print(np.vstack((x, y)).shape)
print(np.hstack((x, y)).shape)
print(np.dstack((x, y)).shape)

# flatten 数组
# flatten 方法的作用是将多维数组转化为1维数组

a = np.array([[0, 1],
              [2, 3]])
b = a.flatten()
print(b)
# 返回的是数组的复制，因此，改变b并不会影响a的值
b[0] = 10
print(b)
print(a)

# flat 属性
# 还可以使用数组自带的flat 属性
a.flat  # 相当于返回了所有元组组成的一个迭代器
b = a.flat
print(b[0])
# 但此时修改b的值会影响到a
b[0] = 10
print(a)
print(a.flat[:])

# ravel 方法
# 除此之外，还可以使用ravel方法，ravel使用高效的方法表示

a = np.array([[0, 1],
              [2, 3]])
b = a.ravel()
print(b)
# 修改b会改变a
b[0] = 10
print(a)
# 但另一种情况下
a = np.array([[0, 1],
              [2, 3]])
aa = a.transpose()
b = aa.ravel()
print(b)
b[0] = 10
print(aa)
print(a)
# 可以看到，在这种情况下，修改b并不会改变aa 的值，原因是我们用来ravel 的对象aa 本身是 a 的view

# atleast_xd 函数
# 保证数组至少有x维
x = 1
np.atleast_1d(x)
a = np.array([1, 2, 3])
print(a)
b = np.atleast_2d(a)
print(b.shape)
print(b)
c = np.atleast_3d(a)
print(c.shape)
# x可以取值1,2,3
