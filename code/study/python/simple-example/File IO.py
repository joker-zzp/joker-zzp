# File IO
# 基本的文件操作

# Author: zhangzhp
# Date: 2017-8-17 13:22:11

# ---------- 执行 ---------- #

# 写文件
with open('../foo.txt','wt') as out_file:
    out_file.write("我们来玩个游戏！\n哈哈哈！")

# Read a File
with open('../foo.txt','rt') as in_file:
    text = in_file.read()
print(text)

input("按<Enter>键结束程序！")
