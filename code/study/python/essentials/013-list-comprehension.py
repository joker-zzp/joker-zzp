# 列表推到式

# 循环可以来生成列表
values = [10, 21, 4, 7, 12]
squares = []
for x in values:
    squares.append(x**2)
print(squares)

# 列表推到式可以使用更简便的方法来创建这个列表
squares = [x**2 for x in values]
print(squares)

'''

还可以在列表推导式中加入条件进行筛选。
例如在上面的例子中，假如只想保留列表中不大于10的数的平方
'''
values = [10, 21, 4, 7, 12]
squares = [x**2 for x in values if x <= 10]
print(squares)

# 也可以使用推导式生成集合和字典：
square_set = {x**2 for x in values if x <= 10}
print(square_set)
square_dict = {x: x**2 for x in values if x <= 10}
print(square_dict)
'''
但是，Python会生成这个列表，然后在将它放到垃圾回收机制中（因为没有变量指向它），这毫无疑问是种浪费。
为了解决这种问题，与xrange()类似，Python使用产生式表达式来解决这个问题
'''
# 计算上面例子中生成的列表中所有元素的和
total = sum(x**2 for x in values if x <= 10)
print(total)

'''
与上面相比，只是去掉了括号，但这里并不会一次性的生成这个列表。
比较一下两者的用时
'''
x = range(100000000)
'''
%timeit total = sum([i**2 for i in x])
36.6 s ± 1.3 s per loop (mean ± std. dev. of 7 runs, 1 loop each)
%timeit total = sum(i**2 for i in x)
35 s ± 118 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
'''
