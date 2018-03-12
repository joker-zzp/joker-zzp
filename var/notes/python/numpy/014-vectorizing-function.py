#! /usr/bin/python3
# 向量化函数

# 自定义的sinc函数
import numpy as np
import matplotlib.pyplot as plt


def sinc(x):
    if x == 0.0:
        return 1.0
    else:
        w = np.pi * x
        return np.sin(w) / w


print(sinc(0))
print(sinc(3))

# 但是这个函数不能应用于数组
# x = np.arange(1, 6)
vsinc = np.vectorize(sinc)
# print(vsinc(x))

x = np.linspace(-5, 5, 150)
plt.plot(x, vsinc(x))
print(x, vsinc(x))
plt.show()

# 因为这样的用法设计大量函数,因此,向量化函数的效率并不高
