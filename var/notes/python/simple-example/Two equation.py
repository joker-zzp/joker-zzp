# Two equation

# 二次方程 ax**2 + bx + c = 0
# a、b、c用户提供
# 导入复杂运算模块
import cmath

global a,b,c

print ("输入a，b，c的数值，计算出二次方程ax**2 + bx + c = 0的值")

# 输入字符a，b，c的值
def inputNumber():
  global a,b,c
  try:
    a = float(input("输入 a："))
    b = float(input("输入 b："))
    c = float(input("输入 c："))
  except ValueError:
    a = ''
    b = ''
    c = ''  
  return a,b,c

# 计算
def Calculation(a,b,c):
  
  if (a!='' and b!='' and c!=''):
    d = (b**2)-(4*a*c)
    
    #两种求解方程
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print ("结果为 {0} 和 {1}".format(sol1,sol2))

#inputNumber()
#Calculation(a,b,c)

# 前提a的值不能为0否则无解
while True:
  inputNumber()
  if (a==0):
    print ("a的值为0时无解!")
    yorn = input("是否重新输入计算（yes or no）")
    if (yorn.lower() in 'yes' ):
      # 重新输入
      print ("请重新输入：")
      continue
    elif (yorn.lower=='n' or yorn.lower=='no'):
      print ("计算结束！")
      break
    else:
      print ("输入有误！视为No，计算结束")
      break
  elif (a=='' or b=='' or c==''):
    print ("输入不能为空！")
    yorn = input("是否重新输入计算（yes or no）")
    if (yorn.lower() in 'yes' ):
      # 重新输入
      print ("请重新输入：")
      continue
    elif (yorn.lower=='n' or yorn.lower=='no'):
      print ("计算结束！")
      break
    else:
      print ("输入有误！视为No，计算结束")
      break
  else:
    Calculation(a,b,c)
  # 计算结束 #

  # 询问是否退出计算程序
    print()
  ifEnd = (input ("是否继续执行（y or n）")).lower()
 
  if (True if ifEnd=='y' or ifEnd=='n'else False):
    if (ifEnd=='y'):
      print()
      print ("请继续输入：")
    else:
      print ("您已成功退出计算程序。欢迎下次继续使用。")
      break
  else:
    print ("输入有误！视为No，并退出运算程序。")
    break

print()
print ("谢谢使用！再见！")

print()
input("按任意键继续！")
