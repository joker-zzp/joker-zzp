# 文件读写

f = open('test.txt')
text = f.read()
print(text)
f.close()

f = open('test.txt')
lines1 = f.readlines()
print(lines1)
f.close()

f = open('test.txt')
for lines in f:
    print(lines)
f.close()

# 删除文件
import os
os.remove('test.txt')

# 写文件
f = open('test.txt', 'w')
f.write('hello world!')
f.close()

print(open('test.txt', 'r').read())

# 追加模式
f = open('test.txt', 'a')
f.write('... and more')
f.close()

print(open('test.txt').read())

# 读写模式
f = open('test.txt', 'w+')
f.write('hello world!')
# 这里 f.seek(6) 移动到文件的第6个字符处，然后 f.read() 读出剩下的内容。
f.seek(6)
print(f.read())
f.close()

os.remove('test.txt')

# ps 写入文件时如果未 关闭文件在读取，读取内容可能显示不全，因为还没有完全写入磁盘
