# 字典
'''

字典 dictionary ，在一些编程语言中也称为 hash ， map ，是一种由键值对组成的数据结构。

顾名思义，我们把键想象成字典中的单词，值想象成词对应的定义，那么——

一个词可以对应一个或者多个定义，但是这些定义只能通过这个词来进行查询。
'''

# 基本操作
# python 使用{} 或者dict() 来创造一个空的字典

a = {}
type(a)

a = dict()
type(a)

# 有了dict 之后可以用索引键值的方法添加元素，也可以通过索引来查看元素的值
a['one'] = 'this is number 1'
a['two'] = 'this is number 2'

a

# 查看键值
a['one']

# 更新键值
a['one'] = 'this is number 1, too'
a['one']

# 初始化字典
b = {'one': 'this is number 1', 'two': 'this is number 2'}
print(a)
print(b)

'''
键必须是不可变的类型
出于hash的目的，Python中要求这些键值对的键必须是不可变的，而值可以是任意的Python对象。

一个表示近义词的字典
'''

synonyms = {}
synonyms['mutable'] = ['changeable', 'variable', 'varying', 'fluctuating',
                       'shifting', 'inconsistent', 'unpredictable',
                       'inconstent', 'fickle', 'uneven', 'unstable', ' protean']
synonyms['immutable'] = ['fixed', 'set', 'rigid', 'inflexible',
                         'permanent', 'established', 'carved in stone']
synonyms

# 定义四个字典
e1 = {'mag': 0.05, 'width': 20}
e2 = {'mag': 0.04, 'width': 25}
e3 = {'mag': 0.05, 'width': 80}
e4 = {'mag': 0.03, 'width': 30}
# 以字典作为值传入新的字典
events = {500: e1, 760: e2, 3001: e3, 4180: e4}
events

# 使用dict初始化字典

inventory = dict(
    [('foozelator', 123),
     ('frombicator', 18),
     ('spatzleblock', 34),
     ('snitzelhogen', 23)])
inventory

# 利用索引直接更新对应键值
inventory['frombicator'] += 1
inventory

# 有时，也可以使用元组作为键值，例如，可以用元组做键来表示从第一个城市飞往第二个城市航班数的多少

connections = {}
connections[('New York', 'Seattle')] = 100
connections[('Austin', 'New York')] = 200
connections[('New York', 'Austin')] = 400

# 元组是有序的，因此 ('New York', 'Austin') 和 ('Austin', 'New York') 是两个不同的键
print(connections[('Austin', 'New York')])
print(connections[('New York', 'Austin')])


# 字典方法
'''
get 方法
之前已经见过，用索引可以找到一个键对应的值，但是当字典中没有这个键的时候，Python会报错，这时候可以使用字典的 get 方法来处理这种情况，其用法如下：

d.get(key, default = None)

返回字典中键 key 对应的值，如果没有这个键，返回 default 指定的值（默认是 None ）。
'''
a = {}
a["one"] = "this is number 1"
a["two"] = "this is number 2"

# a['three'] # 报错
print(a.get('three'))
# 指定默认参数
print(a.get('three', 'undefined'))

'''
pop 方法删除元素
pop 方法可以用来弹出字典中某个键对应的值，同时也可以指定默认参数：

`d.pop(key, default = None)`

删除并返回字典中键 key 对应的值，如果没有这个键，返回 default 指定的值（默认是 None ）。
'''

a
a.pop('two')
# 弹出不存在的键值
a.pop('two', 'not exist')

# del 函数可以用来删除字典中特定的键值对
del a["one"]
a

'''
update方法更新字典
之前已经知道，可以通过索引来插入、修改单个键值对，但是如果想对多个键值对进行操作，这种方法就显得比较麻烦，好在有 update 方法：

`d.update(newd)`

将字典newd中的内容更新到d中去。
'''
person = {}
person['first'] = "Jmes"
person['last'] = "Maxwell"
person['born'] = 1831
print(person)

person_modifications = {'first': 'James', 'middle': 'Clerk'}
person.update(person_modifications)
print(person)

'''
in 查询字典中是否有该键
'''

barn = {'cows': 1, 'dog': 5, 'cats': 3}
'chickens' in barn
'cows' in barn


'''
keys 方法，values 方法和items 方法
d.keys()

返回一个由所有键组成的列表；
d.values()

返回一个由所有值组成的列表；
d.items()

返回一个由所有键值对元组组成的列表；
'''

barn.keys()
barn.values()
barn.items()
