# 数组类型
from numpy import *

# 复数数组
# 产生一个复数数组
a = array([1 + 1j, 2, 3, 4])
a.dtype

# 对于复数我们可以查看它的实部和虚部
a.real
a.imag

# 还可以设置他们的值
a.imag = [1, 2, 3, 4]
a
a.conj()
