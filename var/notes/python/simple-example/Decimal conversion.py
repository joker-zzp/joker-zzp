# Decimal conversion
# 进制转换

# Author:zhangzhp
# Date:2017-8-16 16:53:06

# ----------  进制转换  ---------- #

print(" ----------  进制转换  ---------- ")
try:
  number = (int(input('请输入一个整数：\n')))
  print()

  print("2 进制数为：" + str(bin(number))[2:])
  print("8 进制数为：" + str(oct(number))[2:])
  print("10进制数为：" + str(number))
  print("16进制数为: " + str(hex(number))[2:])
except ValueError:
  print("\n输入内容有误！")
print()
print(" ----------  End  ---------- ")

input("\n按回车键继续！")
  
