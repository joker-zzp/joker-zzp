# ASCII code and character conversion
# ASCII码与字符转换

# author:zhangzhp
# Date:2017-8-16 17:11:40

# ----------  ASCII码与字符转换  ---------- #
print(" ----------  ASCII码与字符转换  ---------- ")
print()

# 用户输入字符
c = input('请输入一个字符：\n')
try:
  print(c + "的ASCII码为：",ord(c))
except TypeError:
  print("已经超过一个字符无法转换")

print()
# 用户输入ASCII码，并将输入数字转换为整形
try:
  a = int(input("请输入一个ASCII码：\n"))
  print(a,"对应的字符为：",chr(a))
except ValueError:
  print("输入有误，输入内容必需为整数！")

print(" ----------  End  ---------- ")
print()


input("按<Enter>继续！")

