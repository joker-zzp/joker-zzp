# 函数
'''
定义函数
函数function，通常接受输入参数，并有返回值。

它负责完成某项特定任务，而且相较于其他代码，具备相对的独立性
'''


def add(x, y):
    ''' Add two numbers'''
    a = x + y
    return a


'''
函数通常有一下几个特征：
使用 def 关键词来定义一个函数。
def 后面是函数的名称，括号中是函数的参数，不同的参数用 , 隔开， def foo(): 的形式是必须要有的，参数可以为空；
使用缩进来划分函数的内容；
docstring 用 """ 包含的字符串，用来解释函数的用途，可省略；
return 返回特定的值，如果省略，返回 None 。
'''

'''
使用函数
使用函数时，只需要将参数换成特定的值传给函数。

Python并没有限定参数的类型，因此可以使用不同的参数类型
'''
print(add(2, 3))
print(add('foo', 'bar'))

'''
设定参数默认值
可以在函数定义的时候给参数设定默认值，例如：'''


def quad(x, a=1, b=0, c=0):
    return a * x**2 + b * x + c


'''
# 可以省略有默认值的参数：
'''
print(quad(2))

'''
这里混合了位置和指定两种参数传入方式，第二个2是传给 a 的
'''
print(quad(2, 2, c=5))


'''
接收不定参数
使用如下方法，可以使函数接受不定数目的参数
'''


def add(x, *args):
    '''
    这里，*args 表示参数数目不定，
    可以看成一个元组，把第一个参数后面的参数当作元组中的元素。
    '''
    total = x
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3, 4))

print(add(1, 2))


'''
这样定义的函数不能使用关键词传入参数，要使用关键词，可以这样：
'''


def add(x, **kwargs):
    '''
    这里， **kwargs 表示参数数目不定，
    相当于一个字典，关键词和值对应于键值对。
    '''
    total = x
    for arg, value in kwargs.items():
        print('adding', arg)
        total += value
    return total


print(add(10, a=1, b=2, c=3))


'''
再看这个例子，可以接收任意数目的位置参数和键值对参数
'''


def foo(*args, **kwargs):
    print(args, kwargs)


foo(1, 2, 3, x='a', y=1)


'''
返回多个值
函数可以返回多个值：
'''
from math import atan2


def to_polar(x, y):
    r = (x**2 + y**2) ** 0.5
    theta = atan2(y, x)
    return r, theta


# 因为这个元组中有两个值，所以可以使用
r, theta = to_polar(3, 4)
print(r, theta)


# 事实上，Python将返回的两个值变成了元组：
print(to_polar(3, 4))

# 列表也有相似的功能：
a, b, c = [1, 2, 3]
print(a, b, c)

# 事实上，不仅仅返回值可以用元组表示，也可以将参数用元组以这种方式传入


def add(x, y):
    """Add two numbers"""
    a = x + y
    return a


z = (2, 3)
# 这里的*必不可少
print(add(*z))

# 事实上，还可以通过字典传入参数来执行函数：
w = {'x': 2, 'y': 3}
print(add(**w))


'''
map 方法生成序列
可以通过 map 的方式利用函数来生成序列：
'''


def sqr(x):
    return x**2


a = [2, 3, 4, 5]
# python2 中 map(sqr, a) 返回的是对象的内存地址
# python3 中应该如下方写法
print(list(map(sqr, a)))

b = [2, 3, 4, 5]
print(list(map(add, a, b)))
