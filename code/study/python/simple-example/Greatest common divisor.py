# Greatest common divisor
# 最大公约数

# Author: zhangzhp
# Date: 2017-8-16 17:38:19

# ----------  调用包  ---------- #
import time


# ----------  函数定义  ---------- #


# 求最大公约数算法一
def hcf(x,y):
    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller =x
    for i in range(1,smaller+1):
        if((x%i == 0)and(y%i == 0)):
            hcf = i
    return hcf

# 求最大公约数算法二
def gcd(x,y):
    if y > x:
        x,y = y,x  # y为最小值
    if x%y == 0:
        return y
    for i in range(y//2+1,1,-1):  # 倒叙求公约数更合理
        if y%i == 0 and x%i == 0:
            return i
    return 0
  
# 求最大公约数算法三
def my_gcd(x,y):
    return x if y == 0 else my_gcd(y,x%y)

# ---------- 函数结束 ---------- #


# ----------  执  行  ---------- #
try:
    number1 = int(input("请输入第一个数：\n"))
    number2 = int(input("请输入第二个数：\n"))
except ValueError:
    print("输入内容只能为整数：")


start = time.clock()
my_gcd(number1,number2)
end = time.clock()
my_gcd_time = '%f'%(end - start)
print(my_gcd_time)

start = time.clock()
gcd(number1,number2)
end = time.clock()
gcd_time = '%f'%(end - start)
print(gcd_time)

start = time.clock()
hcf(number1,number2)
end = time.clock()
hcf_time = "%f"%(end - start)
print(hcf_time)




'''
# ---------- Test ---------- #
start = time.clock()
print(my_gcd(1235611,6524311))  # pass
end = time.clock()
print("rean: %f s"%(end - start))

start = time.clock()
print(hcf(1235611,6524311))  # pass
end = time.clock()
print("read: %f s"%(end - start))

start = time.clock()
print(gcd(1235611,6524311))  # pass
end = time.clock()
print("read: %f s"%(end - start))

'''



