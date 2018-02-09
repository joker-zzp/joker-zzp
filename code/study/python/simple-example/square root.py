# square root
# 求平方根
# 导入复杂运算模块 #
import cmath

print()
# 求平方根 #
print ("求输入数字的平方根")
num = float(input("请输入一个数字："))

# 求平方根方法 #
def sqrt(num):
  if num>0 or num==0:
    num_sqrt = num ** 0.5
    print ("%0.3f 的平方根为：%0.3f" %(num,num_sqrt))
  else:
    num_sqrt = cmath.sqrt(num)
    # num_sqrt.real = 0.0  num_sqrt.inag=输入数的负数
    print ("{0} 的平方根为：{1:0.3f}".format(num,(num_sqrt.real)-(num_sqrt.imag)))

sqrt(num)

input ("按任意键继续!")
