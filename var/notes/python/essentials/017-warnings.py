# 警告

'''
出现了一些需要让用户知道的问题，但又不想停止程序，这时候我们可以使用警告：
'''
import warnings


def month_warning(m):
    if not 1 <= m <= 10:
        msg = "month ({:d}) is not between 1 and 12".format(m)
        warnings.warn(msg, RuntimeWarning)


warnings.filterwarnings(action='ignore', category=RuntimeWarning)
month_warning(12)

print('aa')
