# Sum of numbers
# 数字求和 #
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")

# 求和 #
sum = float(num1) + float(num2)

# 显示计算结果 #
print ("数字:{0} 和 数字:{1} 相加结果为：{2}".format(num1,num2,sum))

print()

# 将上述代码合并为一行 #
print ("两数之和为：%.1f" %(float(input("输入第一个数字：") ) +float(input("输入第二个数字：") ) ) )

print()
input("按任意键继续！")
