# 集合

'''
集合
之前看到的列表和字符串都是一种有序序列，而集合 set 是一种无序的序列。

因为集合是无序的，所以当集合中存在两个同样的元素的时候，Python只会保存其中的一个（唯一性）；同时为了确保其中不包含同样的元素，集合中放入的元素只能是不可变的对象（确定性）。
'''

'''
集合生成
可以用set()函数来显示的生成空集合：
'''
a = set()
type(a)

# 也可以使用一个列表来初始化一个集合
a = set([1, 2, 3, 1])
a

# 可以用{}的形式来创建集合
a = {1, 2, 3, 1}
a

# 但是创建空集合的时候只能用set来创建，因为在Python中{}创建的是一个空的字典
s = {}
type(s)


# 集合操作
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

'''
并
两个集合的并，返回包含两个集合所有元素的集合（去除重复）。
可以用方法 a.union(b) 或者操作 a | b 实现。
'''
a.union(b)
b.union(a)
a | b

'''
交
两个集合的交，返回包含两个集合共有元素的集合。
可以用方法 a.intersection(b) 或者操作 a & b 实现。
'''
a.intersection(b)
b.intersection(a)
a & b
print(a & b)

'''
差
a 和 b 的差集，返回只在 a 不在 b 的元素组成的集合。
可以用方法 a.difference(b) 或者操作 a - b 实现。
'''
a.difference(b)
b.difference(a)
a - b
print(b-a)

'''
对称差
a 和b 的对称差集，返回在 a 或在 b 中，但是不同时在 a 和 b 中的元素组成的集合。
可以用方法 a.symmetric_difference(b) 或者操作 a ^ b 实现（异或操作符）。
'''
a.symmetric_difference(b)
b.symmetric_difference(a)
a ^ b
print(b ^ a)

'''
包含关系
假设现在有这样两个集合：
'''
a = {1, 2, 3, 4}
c = {1, 2, 3}

# 要判断 c 是不是 a 的子集，可以用 c.issubset(a) 方法，或者更简单的用操作 b <= a ：
c.issubset(a)
print(c <= a)

# 与之对应，也可以用 a.issuperset(c) 或者 a >= c 来判断：
a.issuperset(c)
print(a >= c)

# 方法只能用来测试子集，但是操作符可以用来判断真子集：
print(a <= a)
print(a < a)
print(c < a)


# 集合方法

'''
add 方法向集合添加单个元素
跟列表的 append 方法类似，用来向集合添加单个元素。
s.add(a)
将元素 a 加入集合 s 中。
'''
t = {1, 2, 3}
t.add(5)
t

'''
update 方法向集合添加多个元素¶
跟列表的extend方法类似，用来向集合添加多个元素。
s.update(seq)
'''
t.update([4, 5, 6, 7])
t

'''
remove 方法移除单个元素
s.remove(ob)
从集合s中移除元素ob，如果不存在会报错。
'''
t.remove(1)
t

'''
pop方法弹出元素
由于集合没有顺序，不能像列表一样按照位置弹出元素，所以pop 方法删除并返回集合中任意一个元素，如果集合中没有元素会报错。
'''
t.pop()
print(t)

'''
discard 方法
作用与 remove 一样，但是当元素在集合中不存在的时候不会报错。
'''
t.discard(3)
t

'''
difference_update方法
a.difference_update(b)
从a中去除所有属于b的元素：
'''
print()
print('a = ', a)
print(b)
print(c)
print(t)
a.difference_update(b)
print(a)
print(b)
