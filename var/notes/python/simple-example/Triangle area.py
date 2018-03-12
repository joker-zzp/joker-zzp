# Triangle area
# 根据用户输入计算三角面积

####################  函数块  ####################

# 判断输入是否为空
def my_input(str):
  try:  
    value = input(str)
    isVlist = True
    if value == '':
      isVlist = False
  except ValueError:
    isVlist = False
  return [value,isVlist]

# 是否需要重新输入
def yorn(str = "是否重新输入（y or n）"):

  try:
    YorN = input(str)
    YorN = YorN.lower()

    if YorN=='y' or YorN=='yes':
      return True
    elif YorN=='n' or YorN=='no':
      print ("计算结束！")
      return False
    else:
      print ("输入有误！视为No，计算结束")
      return False
  except ValueError:
    print ("输入有误！视为No，计算结束")
    return False

# 用户输入
def get_value(s):

  a = my_input("请输入第"+s+"个边的值：")
  if a[1]:
    try:
      a = float(a[0])
      return a
    except ValueError:
      print ("请验证输入内容是否正确")
      Verification = yorn()
      if Verification :
        get_value(s)
      if (not Verification):
        return False
  else:
    print ("输入内容不能为空")
    Verification = yorn()
    if Verification :
      get_value(s)
    if (not Verification):
      return False

# 计算
def Triangle_area():
  a = get_value('一')
  if not a : return
  b = get_value('二')
  if not b : return
  c = get_value('三')
  if not c : return

  # 计算半周长
  s = (a + b + c) / 2

  # 计算面积
  area = (s*(s-a)*(s-b)*(s-c))**0.5

  if area!=0:
    print()
    print ("三角形的面积是：%0.2f" %area)  
    print()
  else:
    print()    
    print ("输入的值违反三角形定理，无法组成三角形")
    print()

  # 是否继续进行计算
  if yorn("是否继续进行计算（y or n）"):
    Triangle_area()
  else:
    return

####################  函数块  ####################


# 全局变量
global a,b,c

print("----------计算三角型面积----------")
print()# 空行

# 运行 #
Triangle_area()

print()#空行
print ("----------运算结束----------")

print()
input("按任意键继续！")
