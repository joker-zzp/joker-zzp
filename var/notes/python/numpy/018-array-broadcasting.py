# 数组广播机制
import numpy as np
import matplotlib.pyplot as plt

# 正常加法
a = np.array([np.arange(3) * 0 + i * 10 for i in range(4)])
b = np.array([np.arange(3) for i in range(4)])
print(a + b)
b = np.arange(3)
print(a + b)
'''
结果一样，虽然两个数组的维数不一样，但是 Numpy 检测到 b 的维度与 a 的维度匹配，所以将 b 扩展为之前的形式，得到相同的形状。

对于更高维度，这样的扩展依然有效。
'''
# 如果把a变成一个列向量
a = np.arange(4) * 10
a.resize(4, 1)  # 直接改变a数组形状

print(a)
print(b)
print(a + b)
'''
可以看到，虽然两者的维度并不相同，但是Numpy还是根据两者的维度，自动将它们进行扩展然后进行计算。
对于 Numpy 来说，维度匹配当且仅当：

维度相同
有一个的维度是1
匹配会从最后一维开始进行，直到某一个的维度全部匹配为止，因此对于以下情况，Numpy 都会进行相应的匹配：

A	                        B	                Result
3d array: 256 x 256 x 3	        1d array: 3	        3d array: 256 x 256 x 3
4d array: 8 x 1 x 6 x 1	        3d array: 7 x 1 x 5	3d array: 8 x 7 x 6 x 5
3d array: 5 x 4 x 3	        1d array: 1	        3d array: 5 x 4 x 3
3d array: 15 x 4 x 13	        1d array: 15 x 1 x 13	3d array: 15 x 4 x 13
2d array: 4 x 1          	1d array: 3      	2d array: 4 x 3
匹配成功后，Numpy 会进行运算得到相应的结果。

当然，如果相应的维度不匹配，那么Numpy会报错：
'''
a = np.array([0, 10, 20, 30])
a[:, np.newaxis] + b
print(a)  # 不会改变a数组形状

# 例子

x = np.linspace(-.5, .5, 21)
y = x[:, np.newaxis]
x.shape
y.shape
radius = np.sqrt(x ** 2 + y ** 2)


plt.imshow(radius)
plt.show()
