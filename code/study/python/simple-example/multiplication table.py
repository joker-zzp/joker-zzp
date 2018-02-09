# multiplication table
# 九九乘法表

# Author：zhangzhp
# Date:2017-8-15 11:04:36

# 通过指定end参数的值，可以取消在末尾输出回车符，实现不换行。

print ("---------- 九九乘法表  ----------")
print()

for i in range(1,10):
  for j in range(1,i+1):
    print ("{}x{}={}\t".format(j,i,i*j),end='')
  print()


print()
print ("----------  结    束  ----------")

input ("按回车键继续！")
