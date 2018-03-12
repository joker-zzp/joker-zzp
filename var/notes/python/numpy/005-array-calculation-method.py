# 数组方法
# sum() 求和
# prod() 求积
# min() 最小值
# max() 最大值
# argmin() 最小值的位置
# argmax() 最大值的位置
# mean() 均值
# average() 均值，支持加权平均
# std() 计算标准差
# var() 计算标准差
# clip() 将数值限制在某个范围内
# ptp() 计算最大值和最小值之差
# round() 近似，默认到整数


from numpy import *

a = array([[1, 2, 3],
           [4, 5, 6]])
sum(a)

# 指定求和的维度
# 沿着第一维度求和
sum(a, axis=0)

# 沿着第二维度求和
sum(a, axis=1)

# 沿着最后一维求和
sum(a, axis=-1)

# 或者使用sum()方法
a.sum()
a.sum(axis=0)
a.sum(axis=-1)

# 求积
# 求所有元素的乘积

a.prod()
# 或
prod(a, axis=0)

# 最大值 最小值
from numpy.random import rand
a = rand(3, 4)

a
# 全局最小
a.min()
# 沿着某个轴的最小
a.min(axis=0)
# 全局最大
a.max()
# 沿着某个轴的最大
a.max(axis=-1)

# 最大值 最小值的位置 使用argmin argmax 方法
a.argmin()
a.argmin(axis=0)
a.argmax()

# 均值
# 可以使用mean 方法
a = array([[1, 2, 3], [4, 5, 6]])
a.mean()
a.mean(axis=1)
mean(a)

# 也可以使用average函数
average(a, axis=0)

# average 函数还支持加权平均
average(a, axis=0, weights=[1, 2])

# 标准差
# 用std方法计算标准差
a.std(axis=1)
# 用var
a.var(axis=1)
# 或使用函数
var(a, axis=0)
std(a, axis=1)

# clip 方法
# 将数值限制在某个范围内

a.clip(3, 5)
# 小于3的变成3，大于5的变成5

# ptp方法
# 计算最大值和最小值之差

a.ptp(axis=1)
a.ptp()

# round 方法
# 近似，默认到整数
a = array([1.2, 3.5, 4.5, 6.5, 8.6])
a.round()
a.round(decimals=1)
