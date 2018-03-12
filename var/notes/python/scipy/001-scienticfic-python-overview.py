# SCIentific Python 简介
'''
Ipython 提供了一个很好的解释器界面。

Matplotlib 提供了一个类似 Matlab 的画图工具。

Numpy 提供了 ndarray 对象，可以进行快速的向量化计算。

Scipy 是 Python 中进行科学计算的一个第三方库，以 Numpy 为基础。

Pandas 是处理时间序列数据的第三方库，提供一个类似 R 语言的环境。

StatsModels 是一个统计库，着重于统计模型。

Scikits 以 Scipy 为基础，提供如 scikits-learn 机器学习和scikits-image 图像处理等高级用法。

Scipy
Scipy 由不同科学计算领域的子模块组成：


────────────────────────────────
子模块        描述
────────────────────────────────
cluster      聚类算法
constants    物理数学常数
fftpack	     快速傅里叶变换
integrate    积分和常微分方程求解
interpolate  插值
io	     输入输出
linalg	     线性代数
odr	     正交距离回归
optimize     优化和求根
signal	     信号处理
sparse	     稀疏矩阵
spatial	     空间数据结构和算法
special	     特殊方程
stats	     统计分布和函数
weave	     C/C++ 积分
────────────────────────────────

'''
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import linalg, optimize


# 可以使用 numpy 中的 info 函数来查看函数的文档
print("可以使用 numpy 中的 info 函数来查看函数的文档:")
np.info(optimize.fmin)

print()
# 可以用 lookfor 来查询特定关键词相关的函数
print("可以用 lookfor 来查询特定关键词相关的函数:")
np.lookfor("resize array")

# 还可以指定查找的模块
print()
print("还可以指定查找的模块")

np.lookfor('remove path', module="os")
