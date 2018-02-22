# 从Matlab 到 Numpy

'''
Numpy 和 Matlab 比较
Numpy 和 Matlab 有很多相似的地方，但 Numpy 并非 Matlab 的克隆，它们之间存在很多差异，例如：

                           MATLAB®	Numpy
基本类型为双精度浮点数组，以二维矩阵为主	基本类型为 ndarray，有特殊的 matrix 类
                       1-based 索引	0-based 索引
              脚本主要用于线性代数计算	可以使用其他的 Python 特性
              采用值传递的方式进行计算	采用引用传递的方式进行计算
                        切片返回复制      切片返回引用
                文件名必须和函数名相同      函数可以在任何地方任何文件中定义
                               收费	免费
                      2D，3D图像支持	依赖第三方库如 matplotlib 等
                      完全的编译环境	依赖于 Python 提供的编译环境

array 还是 matrix？
Numpy 中不仅提供了 array 这个基本类型，还提供了支持矩阵操作的类 matrix，但是一般推荐使用 array：

很多 numpy 函数返回的是 array，不是 matrix
在 array 中，逐元素操作和矩阵操作有着明显的不同
向量可以不被视为矩阵
具体说来：

*， dot(), multiply()
array：* -逐元素乘法，dot() -矩阵乘法
matrix：* -矩阵乘法，multiply() -逐元素乘法
处理向量
array：形状为 1xN, Nx1, N 的向量的意义是不同的，类似于 A[:,1] 的操作返回的是一维数组，形状为 N，一维数组的转置仍是自己本身
matrix：形状为 1xN, Nx1，A[:,1] 返回的是二维 Nx1 矩阵
高维数组
array：支持大于2的维度
matrix：维度只能为2
属性
array：.T 表示转置
matrix：.H 表示复共轭转置，.I 表示逆，.A 表示转化为 array 类型
构造函数
array：array 函数接受一个（嵌套）序列作为参数——array([[1,2,3],[4,5,6]])
matrix：matrix 函数额外支持字符串参数——matrix("[1 2 3; 4 5 6]")
其优缺点各自如下：

array

[GOOD] 一维数组既可以看成列向量，也可以看成行向量。v 在 dot(A,v) 被看成列向量，在 dot(v,A) 中被看成行向量，这样省去了转置的麻烦
[BAD!] 矩阵乘法需要使用 dot() 函数，如： dot(dot(A,B),C) vs A*B*C
[GOOD] 逐元素乘法很简单： A*B
[GOOD] 作为基本类型，是很多基于 numpy 的第三方库函数的返回类型
[GOOD] 所有的操作 *,/,+,**,... 都是逐元素的
[GOOD] 可以处理任意维度的数据
[GOOD] 张量运算
matrix

[GOOD] 类似与 MATLAB 的操作
[BAD!] 最高维度为2
[BAD!] 最低维度也为2
[BAD!] 很多函数返回的是 array，即使传入的参数是 matrix
[GOOD] A*B 是矩阵乘法
[BAD!] 逐元素乘法需要调用 multiply 函数
[BAD!] / 是逐元素操作
当然在实际使用中，二者的使用取决于具体情况。

二者可以互相转化：

asarray ：返回数组
asmatrix（或者mat） ：返回矩阵
asanyarray ：返回数组或者数组的子类，注意到矩阵是数组的一个子类，所以输入是矩阵的时候返回的也是矩阵

'''

# 类Matlab 函数
# 很多类似的函数: ones, zeros, empty, eye, rand, repmat
import numpy
import numpy.matlib

a = numpy.ones(7)
'''
(7,)
<class 'numpy.ndarray'>
'''
a = numpy.matlib.ones(7)
'''
(1, 7)
<class 'numpy.matrixlib.defmatrix.matrix'>
'''
print(a.shape)
print(type(a))

# mat 函数将一个数组转化为矩阵
a = numpy.array([1, 2, 3])
b = numpy.mat(a)
print(type(b))
