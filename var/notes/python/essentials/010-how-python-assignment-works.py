# python赋值机制

# 先来看这一段代码在Python中的执行过程。

x = 500
print(id(x))
y = x
print(id(x), id(y), x is y)
y = 'foo'
print(id(x), id(y), x is y)
'''
x = 500
Python分配了一个 PyInt 大小的内存 pos1 用来储存对象 500 ，\
然后，Python在命名空间中让变量 x 指向了这一块内存，\
注意，整数是不可变类型，所以这块内存的内容是不可变的。

y = x
Python并没有使用新的内存来储存变量 y 的值，而是在命名空间中，\
让变量 y 与变量 x 指向了同一块内存空间。

y = 'foo'
Python此时分配一个 PyStr 大小的内存 pos2 来储存对象 foo ，\
然后改变变量 y 所指的对象。
'''

# 为了提高内存利用效率，Python采用了重用对象内存的办法：
a = 'aa'
print(id(a))
b = 'aa'
print(id(b))

# 容器类型
'''
x = [500, 501, 502]
Python为3个PyInt分配内存 pos1 ， pos2 ， pos3 （不可变）， \
然后为列表分配一段内存 pos4 ，它包含3个位置，分别指向这3个内存， \
最后再让变量 x 指向这个列表。

y = x
并没有创建新的对象，只需要将 y 指向 pos4 即可。

y[1] = 600
原来 y[1] 这个位置指向的是 pos2 ，由于不能修改 pos2 的值，所以首先为 600 分配新内存 pos5 。
再把 y[1] 指向的位置修改为 pos5 。此时，由于 pos2 位置的对象已经没有用了，Python会自动调用垃圾处理机制将它回收。

y = [700, 800]
首先创建这个列表，然后将变量 y 指向它
'''

x = [500, 501, 502]
print('x =', id(x), ['x[{}]={}, id={} '.format(x.index(i), i, id(i)) for i in x ])
y = x
print('y =', id(y), ['y[{}]={}, id={} '.format(y.index(i), i, id(i)) for i in y ])
y[1] = 600
print('y =', id(y), ['y[{}]={}, id={} '.format(y.index(i), i, id(i)) for i in y ])
y = [700, 800]
print('y =', id(y), ['y[{}]={}, id={} '.format(y.index(i), i, id(i)) for i in y ])


