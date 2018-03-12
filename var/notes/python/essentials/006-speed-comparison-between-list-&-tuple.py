# 列表与元组的速度比较

# 比较生成速度
# %timeit [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# %timeit (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

from numpy.random import rand

values = rand(10000, 4)
lst = [list(row) for row in values]
tup = tuple(tuple(row) for row in values)

'''
比较遍历的速度
 %timeit for row in lst:list(row)
1.48 ms ± 32.3 us per loop (mean ± std. dev. of 7 runs, 1000 loops each)

 %timeit for row in tup:tuple(row)
893 us ± 16.3 us per loop (mean ± std. dev. of 7 runs, 1000 loops each)

比较索引速度
%timeit for row in lst: a = row[0] + 1
2.15 ms ± 38 us per loop (mean ± std. dev. of 7 runs, 100 loops each)

%timeit for row in tup: a = row[0] + 1
2.34 ms ± 25.3 us per loop (mean ± std. dev. of 7 runs, 100 loops each)
'''
