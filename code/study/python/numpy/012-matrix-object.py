# 矩阵

import numpy as np


# 使用mat方法将 2 维数组转化为矩阵
a = np.array([[1, 2, 4],
              [2, 5, 3],
              [7, 8, 9]])
print(a)
# 也可以使用Matlab 的语法传入一个字符串来生成矩阵
A = np.mat('1,2,2;4,5,6;7,8,9')
print(a)


# 利用分块创造 新的矩阵
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[10, 20],
              [30, 40]])
np.bmat('a,b;b,a')


# 矩阵与向量的乘法
x = np.array([[1, 11], [2, 22], [3, 33]])
print(x)
A * x

# A.I 表示A矩阵的逆矩阵

print(A * A.I)

# 矩阵指数表示矩阵连乘

print(x**4)
