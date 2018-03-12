# String manipulation
# 字符串操作

# Author: zhangzhp
# Date: 2017-8-17 13:42:01

# ---------- 运行 ---------- #

print()
str = (input("请输入要检查的字符串：\n"))

# 字符串判断
print("\n ---------- 字符串判断 ---------- \n")
print("\tPurpose\t\t\t Usage\t\t Result")
print("判断所有字符都是数字或字母:\t str.isalnum()\t",str.isalnum())
print("判断所有字符都是字母:\t\t str.isalpha()\t",str.isalpha())
print("判断所有字符都是数字:\t\t str.isdigit()\t",str.isdigit())
print("判断所有字符都是大写:\t\t str.islower()\t",str.islower())
print("判断所有字符都是小写:\t\t str.isupper()\t",str.isupper())
print("判断所有单词都是首字母大写:\t str.istitle()\t",str.istitle())
print("判断所有字符都是空白字符\\t\\n\\r:\t str.isspace()\t",str.isspace())
print("\n ---------- 字符串判断 ---------- \n")

# 字符串大小写转换
print("\n ---------- 字符串大小写转换 ---------- \n")
print("\t\tPurpose\t\t \t Usage\t\t\t Result")
print("把所有字符中的小写字母转换成大写字母:\t str.upper()\t\t",str.upper())
print("把所有字符中的大写字母转换成小写字母:\t str.lower()\t\t",str.lower())
print("把第一个字母转化为大写字母:\t\t str.capitalize()\t",str.capitalize())
print("把每个单词的第一个字母转化为大写字母:\t str.title()\t\t",str.title())

print("\n ---------- 字符串大小写转换 ---------- \n")

print()
input("按<Enter>键退出程序！")
