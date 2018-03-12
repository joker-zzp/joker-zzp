# Fibonacci Lucas sequence
# 斐波那契—卢卡斯数列

# Author: zhangzhp
# Date: 2017-8-15 11:42:24

# ----------  函数定义  ---------- #

'''
用户输入
必需输入正整数
'''
def my_input(str):
  if str != '':
    try:
      # 自定义的条件
      int(str)
      return True
    except ValueError:
      pass
      print('输入内容有误！\n')
    return False
  else:
    print("输入内容不能为空！\n")
    return False

'''
询问是否需要重新输入或继续输入询问语句自定义
'''
def yorn(str = "是否重新输入（y or n）"):
  try:
    YorN = input(str).lower()
    if YorN == 'y' or YorN == 'yes':
      return True
    elif YorN == 'n' or YorN == 'no':
      print("\n查询结束！\n")
      return False
    else:
      print("\n输入有误！视为No，查询结束\n")
      return False
  except ValueError:
    print("\n输入有误！视为No，查询结束\n")

'''
要查询的数列位数
'''
def listLengthFunction():
  listLengthStr = input("请输入一个整数：\n")
  if my_input(listLengthStr):
    listLength = int(listLengthStr)
    if listLength > 0:
      return listLength
    else:
      print("抱歉，输入内容必须为正整数！")
      # 询问是否重新输入
      if yorn():
        return listLengthFunction()
      else:
        return False
  else:
    if yorn():
      return listLengthFunction()
    else:
      return False

'''
Fibonacci sequence
斐波那契数列
Lucas sequence
卢卡斯数列
'''
def sequence(seq,listLength):
  if seq=='Lucas':
    sequenceList = [1,3]
    str_title = '卢卡斯'
  elif seq =='Fibonacci':
    sequenceList = [1,1]
    str_title = '斐波那契'
  else:
    return print('抱歉，找不到要查询的数列！')

  print(str_title+"数列：\n")
  listLength = int(listLength)
  if listLength <= 2:
    print(sequenceList[0:listLength])
    print()
  else:
    for i in range(3,listLength+1):
      sequenceList.append(sequenceList[i-2] + sequenceList[i-3])
    print(sequenceList)
    print()

'''
查询方法
Fibonacci or Lucas
'''
def check():
  print()
  str = input("请输入需要查询的数列（Lucas or Fibonacci）")
  if (str.lower() == 'l'):
    print('# ----------  卢卡斯数列  ---------- #')
    checkListLength = listLengthFunction()
    if checkListLength == False:return
    sequence('Lucas',checkListLength)
    print('# ----------  卢卡斯数列  ---------- #')
  elif str.lower() == 'f':
    print('# ----------  斐波那契数列  ---------- #')
    checkListLength = listLengthFunction()
    if checkListLength == False:return
    sequence('Fibonacci',checkListLength)
    print('# ----------  斐波那契数列  ---------- #')
  else:
    print('# ----------  斐波那契-卢卡斯数列  ---------- #')
    checkListLength = listLengthFunction()
    if checkListLength == False:return
    sequence('Fibonacci',checkListLength)
    sequence('Lucas',checkListLength)
    print('# ----------  斐波那契-卢卡斯数列  ---------- #')


# ----------  函数结束  ---------- #


# ----------  开始执行  ---------- #
check()
print()
input("按回车键继续！")
