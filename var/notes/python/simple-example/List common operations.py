# List common operations
# list 常用操作

# Author: zhangzhp
# Date: 2017-8-17 14:49:31

### ---------- 执行 ---------- ###
print()

# list 定义
print('\n ---------- 定义数组 ---------- \n')
ls = ['a','b1','haha','123','@']
print('''定义数组:\nls = ['a','b','haha','123','@']''')
for i in ls:
    print(i,end='  ')  # >>>a  b  haha  123  #
print()
print("ls[2]:\t",ls[2])  # >>>haha
print('\n ---------- End ---------- \n')


# list 负数索引 --从后往前数
print('\n ---------- 负数索引 ---------- \n')
print("ls[-1]:\t",ls[-1])  # >>>@
print("ls[-3]:\t",ls[-3])  # >>>haha
print('\n ---------- End ---------- \n')


# list 增加元素
print('\n ---------- 增加元素 ---------- \n')
ls.append('666')
print("在列表末尾添加新的对象: list.append(obj)\t\t\t",ls)
ls.insert(2,'这是插入的')
print("将对象插入列表: list.insert(index,obj)\t\t\t\t",ls)
ls.extend(['two','elements','666'])
print("在列表末尾一次性追加另一个序列中的多个值: list.extend(seq)\t",ls)
print('\n ---------- End ---------- \n')


# list 搜索
print('\n ---------- 搜索 ---------- \n')
print("当前示例数组:",ls)
print()
print("从列表中找出某个值第一个匹配项的索引位置: list.index(obj)\t\t"+"查找'123':",ls.index('123')," 查找'a':",ls.index('a'))
# ls.index('c')
try:
    print("当 'c'in ls =",'c'in(ls),"时: ls.index('c')")
    ls.index('c')
except ValueError:
    print("报错:  ValueError: 'c' is not in list")
print('\n ---------- End ---------- \n')


# list 删除元素
print('\n ---------- 删除元素 ---------- \n')
print("当前示例数组:",ls)
print("移除列表中某个值的第一个匹配项:('666')\t\t list.remove(obj)\t 返回值是:",ls.remove('666'),"\n当前列表:",ls,'\n')
# ls.remove('c')
try:
    print("当 'c'in ls =",'c'in(ls),"时: ls.remove('c')")
    ls.remove('c')
except ValueError:
    print("报错:  ValueError: list.remove(x): x not in list")
print()
print("移除列表中最后一个元素，然后返回删除元素的值:('666')\t\t list.pop()\t 返回值是:",ls.pop(),"\n当前列表: ",ls)
print()
print("用pop()移除列表中第一个元素：('a')\t\t\t\t ls.pop(0)\t 返回值是:",ls.pop(0),"\n当前列表: ",ls)
print('\n ---------- End ---------- \n')


# list 运算符
print("\n ---------- 运算符 ---------- \n")
print("当前示例数组:",ls)
print()
ls += ['qq','ww']
print("ls += ['qq','ww'] 后，向数组后插入两个元素")
print(ls)
a = [1,2,3]*3 
print("\na = [1,2,3]*3 后，会重复数组3次并作为a列表")
print("a列表为:",a)

print("\n ---------- End ---------- \n")


# list 使用join链接list字符串
print("\n ---------- 使用 join 链接 list 成为字符串 ----------\n")
udict = {'uid':'1','uname':'zhang','age':'男'}
print("当前示例字典: ulist = ",udict)
print()
udict = ['%s=%s'%(k,v) for k,v in udict.items()]
print("list字符串: ",udict,'\n')
print("使用 '; '.join 链接后: ",';'.join(udict))
print("\n ps:join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。连接一个存在一个或多个非字符串元素的 list 将引发一个异常。")
print("\n ---------- End ----------\n")


# list 分割字符串
print("\n ---------- 分割字符串 ---------- \n")
s = ';'.join(udict)
print("当前示例字符串：s = "+s)
print("将字符串s分割成数组：\t s.split(';')\t 结果:",s.split(';'))
print("分割1个其他不动 \t s.split(';',1)\t 结果:",s.split(';',1) )
print("\n ---------- End ---------- \n")


# list 的映射解析
print("\n ---------- list 的映射解析 ----------\n")
li = [1,2,3,5,8,13]
print("当前示例数组:",li)
print("将示例数组中所有数字乘以2: \t 结果:",[i*2 for i in li])
print("\n ---------- End ---------- \n")


# dictionary中的解析
print("\n ---------- distionary中的解析 ---------- \n")

# 查看当前 ulist 的属性 返回<class 'list'>
#print(type(ulist))
# 列表无法转换成字典
# 先转换成字符串格式
ustr = str(udict).replace('=','\':\'').replace('[','{').replace(']','}')
# 将字符串转换成字典
udict = eval(ustr)
#print(type(ulist)) test 返回 <calss 'dict'>

# 正式使用
print("当前示例字典:",udict)
print(udict.keys())
print(udict.values())
print(udict.items())
print("\n将字典解析成列表:")
ulist = ['%s=%s'%(k,v)for k,v in udict.items()]
print(ulist)
print("\n ---------- End ---------- \n")


# list 过滤
print('\n ---------- list 过滤 ----------\n')
print("当前示例列表:",ls)
print("找出当前列表中是纯英文的元素:",[elem for elem in ls if elem.isalpha()])
print("找到当前列表中不是纯英文的元素:",[elem for elem in ls if not elem.isalpha()])

print('\n ---------- End ---------- \n')


# ---------- 执行 ---------- #

#input("按<Enter>键退出程序！")
