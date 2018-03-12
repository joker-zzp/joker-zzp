# Turn to Fahrenheit at centigrade
# 摄氏温度转换为华氏温度

# ----------  函数定义  ---------- #

# 用户输入
'''
当为空时认为输入有误
当输入遇到问题时
my_input()返回False 否则返回 True
'''
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
'''
--------有默认询问语句，调用方法是可以自己定--------
'''
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

def play():

  print()
  centigrade = my_input("请输入温度（默认为℃）： ")
  if centigrade[1] and centigrade[0].replace('℃','')!='':

    if centigrade[0].find('℉')>0:
      centigrade = centigrade[0].replace("℉",'')
      centigrade = float(centigrade)
      
      # 计算摄氏温度
      fahrenheit = (centigrade-32)/1.8
      print ("%0.1f ℉ 换成摄氏温度为：%0.1f ℃"%(centigrade,fahrenheit))
      if yorn():play()
    else:

      centigrade = centigrade[0].replace("℃",'')
      try:
        centigrade = float(centigrade)
        # 计算华氏温度
        fahrenheit = (centigrade * 1.8) + 32

        print ("%0.1f ℃ 换成华氏温度为：%0.1f ℉"%(centigrade,fahrenheit))
        if yorn():play()
      except ValueError:
        print ("输入内容无法转换成华氏温度！")
        if yorn():play()
  else:
    print ("输入内容不能为空")
    if yorn():play()

#----------  函数结束  ----------#

#----------  执    行  ----------#

print ("如果想从华氏度转换成摄氏度请在输入内容中加单位（℉）")
play()


#a = input("qingshur")
#print (a)
#print (a.index("℃"))
#print (a.replace('℃','')) #字符串替换replace(替换前的str，替换后的str，替换次数)

print()
input("按Enter键继续！")
