# Armstrongnumber
# 阿姆斯特朗数

# Author: zhangzhp
# Date:2017-8-16 09:48:48

# ----------  函数定义  ---------- #

'''
# 用户输入
'''
def my_input(strnum):
  if strnum!='':
    try:
      # 自定义的条件
      int(strnum)
      return True
    except ValueError:
      print("输入内容必需为正整数！")
  else:
    print("输入内容不能为空！")
    return False

'''
# 询问是否需要重新输入
'''
def yorn(yorn_str="是否重新输入（y or n）"):
  try:
    YorN = input(yorn_str).lower()
    if YorN =='y' or YorN == 'yes':
      return True
    elif YorN == 'n' or YorN == 'no':
      return False
    else:
      print("\n输入有误！视为No，查询结束\n")
      return False
  except ValueError:
    print("\n输入有误！视为No，查询结束！\n")
    return False


'''
# Armstrongnumber
# 阿姆斯特朗数
# 计算方法
'''
def Armstrongnumber(number):
  armstrongnumber_list = [1,2,3,4,5,6,7,8,9]

  # 按位数查询
  if number[-1]=='d':
    print("阿姆斯特朗数列1 ~ "+number[0:-1]+" 是：")
    number = int(number[0:-1])

    if number < 9:
      print(armstrongnumber_list[0:number])
    else:
      # 获取数组中最大的值
      num = max(armstrongnumber_list)
      # 根据数组长度 进行比较
      while len(armstrongnumber_list) < number:
        while True:
          num += 1
          # 获得指数
          n = len(str(num))
          # 初始化 相加后的值
          sum_num = 0
          # 进行比对
          temp = num
          while temp > 0:
            digit = temp%10
            sum_num += digit**n
            temp //= 10

          if sum_num == num :
            armstrongnumber_list.append(sum_num)
            break
      print(armstrongnumber_list)
  else:
    # 获取指数
    n = len(number)

    # 初始化相加的值
    sum_num = 0

    # 比对
    temp = int(number)
    while temp > 0:
      digit = temp%10
      sum_num += digit**n
      temp //=10
    print()
    print(number,"是阿姆斯特朗数")if int(number) == sum_num else print(number,"不是阿姆斯特朗数")

'''
# 要查询的数或位数
'''
def check_number(str_title='num'):
  sum = False
  if str_title == 'num':
    num = input('请输入要查询的数：\n')
  else:
    num =(input('请输入要查询的位数：\n'))
    sum = 'd'

  # 检查输入是否合法
  if not my_input(num):
    # 是否重新输入
    if not yorn():
      return
    else:
      return check_number(str_title)
  if sum :num += sum
  return num


# 测试
#check_number()
#check_number('digit')
#Armstrongnumber('11')

# ----------  函数结束  ---------- #

# ----------  执   行  ---------- #

print(" ----------  Armstrongnumber  ---------- ")

print()
check = input("按<Enter>判断是否为阿姆斯特朗数（输入L时<Enter>查询数列）：")
if check == 'l' or check == 'L' :
  Armstrongnumber(check_number('List'))
else:
  Armstrongnumber(check_number())

print()
print(" ----------  End  ---------- ")
print("\n按回车键继续！")
