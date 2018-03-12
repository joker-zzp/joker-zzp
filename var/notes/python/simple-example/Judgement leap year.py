# Judgement leap year
# 判断闰年

# Author：zhangzhp
# Date：2017-8-15 09:02:56

# 计算方法四年一闰，百年不润，四百在润
# 用户输入

print ("----------  判断闰年  ----------")
print ()

try:
  year =int(input ("请输入一个年份："))
  print ()
  try:
    if (year%4 == 0 and year%100 != 0)or(year%400 == 0):
      print ("{0} 是闰年".format(year))
    else:
      print("{0}不是闰年".format(year)) 
  except ValueError:
    pass
    print ("对不起，无法判断！")    
except ValueError:
  pass
  print ("输入内容不是年份")


print ()
print ("----------  结  束  ----------")
input ("按回车键继续！")
