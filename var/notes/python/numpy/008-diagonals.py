# 对角线
import numpy as np

# 使用numpy中的函数时，需要加上np.

a = np.array([11, 21, 31, 12, 22, 32, 13, 23, 33])
a.shape = 3, 3
print(a)

# 查看它们对角线元素
a.diagonal()

# 可以使用偏移来查看它的次对角线，正数代表右移，负数代表左移
print(a.diagonal(offset=1))
print(a.diagonal(offset=-1))

# 可以使用花式索引来得到对角线
i = [0, 1, 2]
print()
print(a[i, i])
# 可以更新对角线的值
a[i, i] = 0
print(a)

i = np.array([0, 1])
a[i, i + 1] = 1
a[i + 1, i] = -1
print(a)
