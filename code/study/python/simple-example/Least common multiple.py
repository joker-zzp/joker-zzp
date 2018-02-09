# Least common multiple
# 最小公倍数

# Author: zhangzhp
# Date: 2017-8-17 09:22:01

# ---------- 调用包 ---------- #
import time


# ---------- 函数定义 ---------- #

# 求最小公倍数  very fast
def lcm(x,y):
    s = x*y
    while y:
        x,y = y,x%y
    return s//x


# ---------- 定义结束 ---------- #


# ---------- test ---------- #
'''
start = time.clock()
#L = lcm(40,32)
#print(L)
print(lcm(40,32))
end = time.clock()

print("read: %f s"%(end - start))
'''
# ---------- 执行 ---------- #

print(" ---------- 求最小公倍数 ---------- ")
print()
try:
    number1 = int(input("请输入第一个数：\n"))
    number2 = int(input("请输入第二个数：\n"))
    print()
    print(number1,'和',number2,'的最小公倍数是',lcm(number1,number2))
except:
    print("请输入一个整数！\n")
print()
print(" ---------- End ---------- ")


input("\n按<Enter>键继续！")
