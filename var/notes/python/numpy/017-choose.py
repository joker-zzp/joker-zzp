# choose 函数实现条件筛选
# 对于数组,我们有时候需要进行类似switch 和case 进行条件筛选,此时使用choose 函数s十分方便

import numpy as np

control = np.array([[1, 0, 1],
                    [2, 1, 0],
                    [1, 2, 2]])
np.choose(control, [10, 11, 12])
'''
在上面的例子中,choose 将0, 1, 2对应的值映射为了10, 11, 12, 这里的0, 1, 2表示对应的下标.
事实上, choose不仅仅能接受下标参数,还可以接收所在的位置
'''
i0 = np.arange(9)
i0.resize((3, 3))
i2 = np.arange(20, 29)
i2.resize((3, 3))
print(i0, i2)
control = np.array([[1, 0, 1],
                    [2, 1, 0],
                    [1, 2, 2]])

np.choose(control, [i0, 10, i2])
# 这里,control传入第一个1对应的是10 ,传入的第一个0 对应于i0相应的位置的值即1 ,剩下的以此类推

# 下面的例子将数组中所有小于10的值变成10
a = np.array([np.arange(3) + i * 10 for i in np.arange(3)])
print(a)
a < 10
np.choose(a < 10, (a, 10))

# 下面的例子将数组中所有小于10的值变成10,大于15 的值变成15
lt = a < 10
gt = a > 15
choice = lt + 2 * gt
print(choice)
np.choose(choice, (a, 10, 15))
