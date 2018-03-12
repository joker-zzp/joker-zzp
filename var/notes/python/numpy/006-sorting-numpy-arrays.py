# 数组排序

import numpy as ny

name = ny.array(['Java', 'JavaScript', 'Python', 'C'])
weights = ny.array([3.2, 45.6, 55, 33, 22, 11, 9.3, 2])

# sort 函数
# sort 返回的是从小到大排列
ny.sort(weights)
ny.sort(name)

# argsort 函数
# argsort 返回从小到大排列数组中索引的位置
ny.argsort(weights)
ny.argsort(name)
# 并不会改变原数组的值
name

# sort 和 argsort 方法
# 支持方法操作
name.argsort()  # 不会改变数值
print(name)
name.sort()  # 会改变数值
print(name)


# 二维数组排序
# 对于多维数组排序 sort方法默认沿着最后一维开始排序
a = ny.array([[.2, .1, .5],
              [.8, .4, .6],
              [.7, .3, .9]])
a
ny.sort(a)  # 默认相当于对每一行进行排序

ny.sort(a, axis=0)  # 变轴，对每一列进行排序

# searchsorted 函数
# searchsorted(sorted_array, values) 其中第一个必须是已排序的数组
a = ny.array([9, 8, 6, 5, 7, 4, 3, 2, 1])
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ny.searchsorted(sorted_array, a)
# secarchsorted 返回值相当于保持第一组数组排序不变，将第二个数组的值插入第一个数组中

data = ny.random.rand(100)
data.sort()

bounds = .4, .6
bounds

low_idx, high_idx = ny.searchsorted(data, bounds)
print(ny.searchsorted(data, bounds))
data[low_idx:high_idx]
