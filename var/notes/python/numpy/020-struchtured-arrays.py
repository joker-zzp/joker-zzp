# 结构化数组
import numpy as np
import os

a = np.array([1.0, 2.0, 3.0, 4.0], np.float32)
# 使用view方法,将a对应的内存按照复数来解释
a.view(np.complex64)

my_dtype = np.dtype([('mass', 'float32'), ('vol', 'float32')])
a.view(my_dtype)
my_data = np.array([(1, 1), (1, 2), (2, 1), (3, 1)], my_dtype)
my_data[0]
my_data[0]['vol']
my_data['mass']
my_data.sort(order=('vol', 'mass'))
print(my_data)

# 定义一个人的结构类型
person_dtype = np.dtype([('name', 'S10'), ('age', 'int'), ('weight', 'float')])
person_dtype.itemsize

people = np.empty((3, 4), person_dtype)
# 分别赋值
people['name'] = [['Brad', 'Jane', 'John', 'Fred'],
                  ['Henry', 'George', 'Brain', 'Amy'],
                  ['Ron', 'Susan', 'Jennife', 'Jill']]
people['age'] = [[33, 25, 47, 54],
                 [29, 61, 32, 27],
                 [19, 33, 18, 54]]
people['weight'] = [[135., 105., 255., 140.],
                    [154., 202., 137., 187.],
                    [188., 135., 88., 145.]]
print(people)
people[-1, -1]

with open('people.txt', mode='w', encoding='utf-8') as f:
    f.writelines('name age weight \n')
    f.writelines('amy 11 38.2 \n')
    f.writelines('john 10 40.3 \n')
    f.writelines('bill 12 21.2 \n')

people = np.loadtxt('people.txt',
                    skiprows=1,
                    dtype=person_dtype)

print(people)
print(people['name'])
os.remove('people.txt')

with open('wood.csv', mode='w', encoding='utf-8') as f:
    f.writelines('item,material,number\n')
    f.writelines('100,a,33\n')
    f.writelines('110,b,14\n')
    f.writelines('120,a,7\n')
    f.writelines('145,c,3\n')

tree_to_int = {'a': 1,
               'b': 2,
               'c': 3}


def convert(s):
    return tree_to_int.get(s, 0)


data = np.genfromtxt('wood.csv',
                     delimiter=',',
                     dtype=np.int,
                     names=True,
                     converters={1: convert}
                     )

print(data)
data['material']

os.remove('wood.csv')

# 嵌套类型
'''
有时候，结构数组中的域可能包含嵌套的结构，例如，在我们希望在二维平面上纪录一个质点的位置和质量：

position
        mass
x	y

'''

particle_dtype = np.dtype([('position', [('x', 'float'),
                                         ('y', 'float')]),
                           ('mass', 'float')
                           ])

with open('data.txt', mode='w', encoding='utf-8') as f:
    f.write('2.0 3.0 42.0\n2.1 4.3 32.5\n1.2 4.6 32.3\n4.5 -6.4 23.3')

data = np.loadtxt('data.txt', dtype=particle_dtype)
print(data)

os.remove('data.txt')
