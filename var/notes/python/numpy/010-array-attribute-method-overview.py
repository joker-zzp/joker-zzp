# 数组属性方法总结

'''
1. 基本属性
a.dtype      # 数组元素类型 float32，uint8,...
a.shape      # 数组形状(m, n, o, ...)
a.size       # 数组元素个数
a.itemsize   # 每个元素占字节数
a.nbytes     # 所有元素占字节数
a.ndim       # 数组维度

2.形状相关
a.flat                    # 所有元素的迭代器
a.flatten()               # 返回一个1维数组的复制
a.ravel()                 # 返回一个1维数组，高效
a.resize(new_size)        # 改变形状
a.swapaxes(axis1, axis2)  # 交换两个维度的位置
a.transpose(*axex)        # 交换所有维度的位置
a.T                       # 转置，a.transpose()
a.squeeze()               # 去除所有长度为1的维度

3.填充复制
a.copy()        # 返回数组的一个复制
a.fill(value)   # 将数组的设置为特定的值

4.转化
a.tolist()             # 将数组转化为列表
a.tostring()           # 转化为字符串
a.astype(dtype)        # 转化为指定类型
a.byteswap(False)      # 转换大小写字节序
a.view(type_or_dtype)  # 生成一个使用相同内存，但是使用不同的表示方法的数组

5.复数
a.imag         # 虚部
a.real         # 实部
a.conjugate()  # 复共轭
a.conj()       # 复共轭（缩写）

6.保存
a.dump(file)                          # 将二进制数据存在file中
a.dump()                              # 将二进制数据表示成字符串
a.tofile(fid, sep="", format="%s")    # 格式化ASCⅡ码写入文件

7.查找排序
a.nonzero()          # 返回所有非零元素的索引
a.sort(axis=-1)      # 沿某个轴排序
a.argsort(axis=-1)   # 沿某个轴，返回排序的索引
a.searchsorted(b)    # 返回将b中元素插入a后能保持有序的索引值

8.元素数学操作
a.clip(low, high)    # 将数值限制在一定范围内
a.round(decimals)    # 近似到指定精度
a.cumsum(axis=None)  # 累加和
a.cumprod(axis=None) # 累加积

9.简约操作
a.sum(axis=None)     # 求和
a.prod(axis=None)    # 求积
a.min(axis=None)     # 最小值
a.max(axis=None)     # 最大值
a.argmin(axis=None)  # 最小值索引
a.argmax(axis=None)  # 最大值索引
a.ptp(axis=None)     # 最大值减最小值
a.mean(axis=None)    # 平均值
a.std(axis=None)     # 标准差
a.var(axis=None)     # 方差
a.any(axis=None)     # 只要有一个不为0,返回真,逻辑或
a.all(axis=None)     # 所有都不为0,返回真,逻辑与

'''
import numpy as np
import os

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print('\n a = ')
print(a)

print('# 数组元素属性')
print(a.dtype)

print('# 形状')
print(a.shape)

print('# 元素数目')
print(a.size)

print('# 元素占字节大小')
print(a.itemsize)

print('# 所有元素所占字节')
print(a.nbytes)

print('# 数据维度')
print(a.ndim)

print('# 形状相关')
for row in a:
    print(row)

print('# 所有元素的迭代器')
for elt in a.flat:
    print(elt)

print('# 所有元素组成的一维数组，按照行排列')
print(a.flatten())
print(a.ravel)

print('# 重新改变形状')
a.resize(4, 2)
print(a)

print('# 交换这两个轴的顺序')
print(a.swapaxes(0, 1))

print('# 转置')
print(a.transpose())
print(a.T)

a2 = np.array([1, 2, 3])
print(a2.shape)
a2.resize((1, 3, 2))
print(a2.shape)

print('# 去除长度为1的维度')
print(a2.squeeze().shape)

print('# 填充复制')
print('# 复制')
b = a.copy()
print('b = a.copy() \n b = \n', b)
b[0][0] = -1
print('b[0][0] = -1')
print('b = \n', b)
print('a = \n', b)

print('# 填充')
b.fill(4)
print(b)

print('# 转化')
print('# 转化为列表')
print(a.tolist())

print('# 转化为字符串')
print(a.tostring())

print('# 改变数组元素类型')
print(a.astype(float))
b = a.copy()
print(b.byteswap(False))
print(a.view(np.dtype('int32')))

print('# 复数')
b = np.array([1 + 2j, 3 + 4j, 5 + 6j])
d = np.array([1 - 2j, 3 - 4j, 5 - 6j])
print('# 实部')
# print(np.abs(b) == np.abs(d))
print(b.real)

print('# 虚部')
print(b.imag)

print('# 共轭')
print(b.conj())
print(b.conjugate())

print('# 保存')
print('# 保存成文本')
a.dump('file.txt')
print(a.dumps())

print('# 写入文件')
a.tofile('foo.csv', sep=',', format='%s')

print('查找排序')

print('# 非零元素的索引')
print(a, a.nonzero())

print('# 排序')
b = np.array([2, 7, 5, 4, 6, 1])
b.sort()
print(b)

print('# 排序索引位置')
b = np.array([2, 7, 5, 4, 6, 1])
print(b, b.argsort(axis=-1))

print('将b插入a中的索引,使得a保持有序')
a = np.array([1, 3, 4, 6])
b = np.array([0, 2, 5])
a.searchsorted(b)

print('# 元素数学操作')
a = np.array([[4, 1, 3], [2, 1, 5]])
print('# 限制在一定范围内')
print(a.clip(0, 3))

print('# 近似')
a = np.array([1.22, 2.358, 4.562])
print(a.round(decimals=1))

print('# 累加和')
a = np.array([[2, 3, 4], [7, 5, 6]])
print(a.cumsum(axis=None))

print('# 累乘积')
print(a.cumprod(axis=None))

print('# 约简操作')
a = np.array([[4, 1, 3], [0, 6, 5]])
print('a =', a)
print('# 求和')
print(a.sum(axis=None))
print('# 求积')
print(a.prod(axis=None))
print('# 最大值')
print(a.max(axis=None))
print('# 最小值')
print(a.min(axis=None))
print('# 最大值索引')
print(a.argmax(axis=None))
print('# 最小值索引')
print(a.argmin(axis=None))
print('# 最大间隔')
print(a.ptp(axis=None))
print('# 均值')
print(a.mean(axis=None))
print('# 标准差')
print(a.std(axis=None))
print('# 方差')
print(a.var(axis=None))
print('# 是否有非零元素')
print(a.any(axis=None))
print('# 是否全部非零')
print(a.all())

print('# 删除生成的文件')

try:
    os.remove('foo.csv')
    os.remove('file.txt')
    print('删除成功!')
except Exception:
    print('删除失败!')
    pass
