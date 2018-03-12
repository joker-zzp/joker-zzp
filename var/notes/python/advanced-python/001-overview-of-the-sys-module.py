# sys 模块简介
import sys

print(sys.platform)
# print(sys.version)
# print(sys.path)

try:
    x = 1 / 0
except Exception:
    sys.exc_clear()
    print(sys.exc_info())
