# 不可变合集

'''
对应于元组（tuple）与列表（list）的关系，对于集合（set），Python提供了一种叫做不可变集合（frozen set）的数据结构。
使用 frozenset 来进行创建
'''
s = frozenset([1, 2, 3, 4, 'a', 5])
s

'''
与集合不同的是，不可变集合一旦创建就不可以改变。
不可变集合的一个主要应用是用来作为字典的键，例如用一个字典来记录两个城市之间的距离：
'''
flight_distance = {}
city_pair = frozenset(['Los Angeles', 'New York'])
flight_distance[city_pair] = 2498
flight_distance[frozenset(['Austin', 'Los Angeles'])] = 1233
flight_distance[frozenset(['Austin', 'New York'])] = 1515

print(flight_distance)
# 由于集合不分顺序，所以不同顺序不会影响查阅结果：
print(flight_distance[frozenset(['Austin', 'New York'])])
print(flight_distance[frozenset(['New York', 'Austin'])])
