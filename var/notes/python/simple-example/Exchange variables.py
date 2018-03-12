 # Exchange variables 变量交换

a = input("请输入第一个变量a：")
b = input("请输入第二个变量b：")
print("a的值为："+ a)
print("b的值为："+ b)

# 变量交换1
print()
print ("变量交换后")
temp = a
a = b
b = temp
print ("a的值为："+ a)
print ("b的值为："+ b)

# 变量交换2
print()
print ("再次交换回来")
a,b = b,a
print ("a的值为："+ a)
print ("b的值为："+ b)
