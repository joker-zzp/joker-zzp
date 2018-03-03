# 计算扑克牌
import numpy as np
import random

pk = np.array([np.arange(13)+1 for i in range(4)])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(random.sample(a, 1))
for i in range(4):
    temp = random.sample(a, 1)
