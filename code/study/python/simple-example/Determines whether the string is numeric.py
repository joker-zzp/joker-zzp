# Determines whether the string is numeric
# 判断字符串是否为数字

# 创建自定义函数
def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    pass
  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TypeError,ValueError):
    pass
  return False

# 测试字符串
print (is_number("hhhh"))  #False
print (is_number('1234'))  #True
print (is_number('2.22'))  #True
print (is_number('1j12'))  #False

print ()

# 测试 Unicode

print ("测试 Unicode")

# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False

print()
input("按回车键继续！")
