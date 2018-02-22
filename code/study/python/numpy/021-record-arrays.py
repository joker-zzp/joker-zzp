# 记录数组

import numpy as np


partical_dtype = np.dtype([('mass', 'float'),
                           ('velocity', 'float')])
# 生成记录数组要使用 numpy.rec 里的 fromrecords 方法:

partical_rec = np.rec.fromrecords(
    [(1, 1), (1, 2), (1, 3)], dtype=partical_dtype)

print(partical_rec)
partical_rec.mass
partical_rec['velocity']

# 不过，记录数组的运行效率要比结构化数组要慢一些。

# 也可以通过将一个结构化数组看成记录数组：
particals = np.array([(1, 1), (1, 2), (2, 1), (1, 3)], dtype=partical_dtype)

# 使用view 方法看成recarray
particals_rec = particals.view(np.recarray)
particals_rec.mass
particals.dtype.names
