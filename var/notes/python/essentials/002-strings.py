# 字符操作

s = "hello world ! "

# 相乘
s*3

# 字符串长度
len(s)

# 字符串分割
line = s
line.split()
line = s*3
line.split('!')

# 连接
s = ' '
s.join(line)

# 替换
s = 'hello world'
s.replace('world', 'python')
s

# 大小写转换
# 把所有字符中的小写字母转换成大写字母
s.upper()
# 把所有字符中的大写字母转换成小写字母
s.lower()
# 把第一个字母转化为大写字母
s.capitalize()
# 把每个单词的第一个字母转化为大写字母
s.title()

# 字符串判断
print(s)
# 判断所有字符都是数字或字母
s.isalnum()
# 判断所有字符都是字母
s.isalpha()
# 判断所有字符都是数字
s.isdigit()
# 判断所有字符都是小写
s.islower()
# 判断所有字符都是大写
s.isupper()
# 判断所有单词都是首字母大写
s.istitle()
# 判断所有单词都是首字母大写
s.isspace()

# 去除多余空格
# 返回一个将s两端的多余空格除去的新字符串
s.strip()
# 返回一个将s开头的多余空格除去的新字符串
s.lstrip()
# 返回一个将s结尾的多余空格除去的新字符串
s.rstrip()

# 可以使用dir函数查看所有可以使用的方法
dir(s)

# 多行字符串
a = """
 hello world
 hahahaha"""

print(a)

# 使用() 或 \ 来换行
a = ('hello world.'
     'it is a nice day.'
     'my name zzp.')
a
b = 'hello world.'\
    'it is a nice day.'\
    'my name zzp.'
b

# 强制转换字符串
str(1.1 + 2.2)
repr(1.1 + 2.2)

# 整数与不同进制的字符串转换
# 十六进制
hex(255)
# 八进制
oct(255)
# 二进制
bin(255)
# 字符串转整数
int('255')
# 指定进制转换，最后返回整数
int('FF', 16)
int('377', 8)
int('11111111', 2)
# 转换成浮点数
float('3.5')

# 格式化字符串
'{} {} {}'.format('a', 'b', 'c')
'{1} {2} {0}'.format('a', 'b', 'c')
# 制定参数名称
'{x} {y} {z}'.format(x=1, y=2, z=3)
# 混用
'{1} {x} {y} {0}'.format('0', '1', y='y', x='x')
# 用{<field name>:<format>}指定格式
from math import pi
'{0:2} {1:10d} {2:10.2f}'.format('foo', 5, 2 * pi)
