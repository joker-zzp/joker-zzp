# tostring 方法
import numpy as np

a = np.array([[1, 2],
              [3, 4]],
             dtype=np.uint8)

a.tostring()
print(a.tostring())
# 这里使用了Fortran 的格式，按照列来读取数据
print(a.tostring(order='F'))

# fromstring 函数
# 可以使用formstring函数从字符串中读取数据，不过要指定类型
s = a.tostring()
a = np.fromstring(s, dtype=np.uint8)

print(a)
# 此时，返回的数组是一维的，需要重新设定维度
a.shape = 2, 2
print(a)

# 对于文本文件，推荐使用
# loadtxt
# genfromtxt
# savetxt

# 对于二进制文件，推荐使用
# save
# load
# savez
