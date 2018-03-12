# 循环
'''
循环的作用在于将一段代码重复执行多次
'''

# while 循环
'''
while <condition>:
    <statesments>
Python会循环执行<statesments>，直到<condition>不满足为止。
'''

# 计算0 到 100000的和
i = 0
total = 0
while i < 1000000:
    total += i
    i += 1
print(total)

# 空容器会被当成 False ，因此可以用 while 循环来读取容器中的所有元素
plays = set(['Hamlet', 'Macbeth', 'King Lear'])
while plays:
    play = plays.pop()
    print('Perform', play)


# for 循环
'''
for <variable> in <sequence>:
    <indented block of code>

for 循环会遍历完<sequence>中所有元素为止
'''

plays = set(['Hamlet', 'Macbeth', 'King Lear'])
for play in plays:
    print('Perform', play)

# 求和
total = 0
for i in range(1000000):
    total += i
print(total)
'''
python2
然而这种写法有一个缺点：在循环前，它会生成一个长度为 100000 的临时列表。
生成列表的问题在于，会有一定的时间和内存消耗，当数字从 100000 变得更大时，时间和内存的消耗会更加明显。
为了解决这个问题，我们可以使用 xrange 来代替 range 函数，其效果与range函数相同，但是 xrange 并不会一次性的产生所有的数据
total = 0
for i in xrange(1000000):
    total += i
print(total)

python3
在python3中，range()这种实现被移除了，保留了xrange()的实现，且将xrange()重新命名成range()。
在 python3 中，range object在python里增加了attributes,’count’,’index’,’start’,’step’,
’stop’,且能支持slicing。python3的range()在xrange()的基础上变的更强大了。
'''

# continue 语句
'''
遇到 continue 的时候，程序会返回到循环的最开始重新执行。

例如在循环中忽略一些特定的值：
'''
values = [7, 6, 4, 7, 19, 2, 1]
for i in values:
    if i % 2 != 0:
        # 忽略奇数
        continue
    print(i/2)

# break 语句
'''
遇到 break 的时候，程序会跳出循环，不管循环条件是不是满足
'''

command_list = ['start',
                'process',
                'process',
                'process',
                'stop',
                'start',
                'process',
                'stop']
while command_list:
    command = command_list.pop(0)
    if command == 'stop':
        break
    print(command)

# else 语句
'''

与 if 一样， while 和 for 循环后面也可以跟着 else 语句，不过要和break一起连用。

当循环正常结束时，循环条件不满足， else 被执行；
当循环被 break 结束时，循环条件仍然满足， else 不执行。
'''

# 不执行:
values = [7, 6, 4, 7, 19, 2, 1]
for x in values:
    if x <= 10:
        print('Found:', x)
        break
else:
    print("values中没有小于10的数")

values = [11, 12, 13, 15, 17]
for x in values:
    if x <= 10:
        print('Found:', x)
        break
else:
    print("values中没有小于10的数")
