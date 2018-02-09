# factorial
# 阶乘

# Author：zhangzhp
# Date:2017-8-15 10:18:14

# 5的阶乘 1x2x3x4x5 负数没有阶乘

print ("----------  阶  乘  ----------")
print ()

try:
  number = int(input("请输入一个数字："))
  factorial = 1
  
  # 查看输入值是否为负数
  if number < 0:
    print ("抱歉，负数没有阶乘")
  elif number == 0:
    print ("0的阶乘为：1")
  else:
    for i in range(1,number+1):
      factorial = factorial*i
      print ("%d x %d = %d"%(factorial/i,i,factorial))
    print ("%d的阶乘为%d"%(number,factorial))
except ValueError:
  pass
  print ("输入的内容不是正整数，无法计算阶乘")

print ()
print ("----------  结  束  ----------")

input ("按回车键继续！")
