# 数组读写

import numpy as np
import time
import os

# 创建测试文件
data = np.array([[2.1, 2.3, 3.2, 1.3, 3.1],
                 [6.1, 3.1, 4.2, 2.3, 1.8]])
np.savetxt("apply-to-019-01.txt", data, fmt='%.1f')
np.savetxt("apply-to-019-02.txt", data, fmt='%.2f', delimiter=',')
data = np.array([['% Day, Month, Year, Skip, Power'],
                 ['01, 01, 2000, x876, 13 % wow!'],
                 ['% we don\'t want have Jan 03rd'],
                 ['04, 01, 2000, xfed, 55']])
np.savetxt('apply-to-019-03.txt', data, fmt='%s')
data = np.array([['2010-01-01 2.3 3.2'],
                 ['2011-01-01 6.1 3.1']])
np.savetxt('apply-to-019-04.txt', data, fmt='%s')

data = []


with open('./apply-to-019-01.txt') as f:
    for line in f:
        fileds = line.split()
        row_data = [float(x) for x in fileds]
        data.append(row_data)

data = np.array(data)
print('apply-to-019-01.txt :')
print(data)
print()

# 不过,更简便的是使用loadtxt方法
data = np.loadtxt('./apply-to-019-01.txt')
print('apply-to-019-01.txt :')
print(data)
print()

'''
对于逗号分隔的文件（通常为.csv格式）,我们可以稍微修改之前繁琐的过程，将 split 的参数变成 ','即可。

不过，loadtxt 函数也可以读这样的文件，只需要制定分割符的参数即可
'''
data = np.loadtxt('./apply-to-019-02.txt', delimiter=',')
print('apply-to-019-02.txt :')
print(data)
print()

'''
此外，有一个功能更为全面的 genfromtxt 函数，能处理更多的情况，但相应的速度和效率会慢一些。

genfromtxt(fname, dtype=<type 'float'>, comments='#', delimiter=None,
           skiprows=0, skip_header=0, skip_footer=0, converters=None,
           missing='', missing_values=None, filling_values=None, usecols=None,
           names=None, excludelist=None, deletechars=None, replace_space='_',
           autostrip=False, case_sensitive=True, defaultfmt='f%i', unpack=None,
           usemask=False, loose=True, invalid_raise=True)
'''

# loadtxt 的更多特性
data = np.loadtxt('./apply-to-019-03.txt',
                  skiprows=1,
                  dtype=np.int,
                  delimiter=',',
                  usecols=(0, 1, 2, 4),
                  comments='%',
                  )
print('apply-to-019-03.txt :')
print(data)
print()

# loadtxt 自定义替换方法
# 假设我们的文本包含日期，我们可以使用 datetime 在 loadtxt 中处理：


def date_converter(s):
    return time.strftime("%Y-%m-%d", time.localtime())


data = np.loadtxt('./apply-to-019-04.txt',
                  dtype=np.object,
                  converters={0: date_converter,
                              1: float,
                              2: float})
print('apply-to-019-04.txt :')
print(data)
print()

os.remove('apply-to-019-01.txt')
os.remove('apply-to-019-02.txt')
os.remove('apply-to-019-03.txt')
os.remove('apply-to-019-04.txt')
