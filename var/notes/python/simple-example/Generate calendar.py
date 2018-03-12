# calendar
# 日历

# Author: zhangzhp
# Date: 2017-8-17 11:42:51

# ---------- 导入模块 ---------- #
# 日历模块
import calendar


# ---------- 执行 ---------- #
# 输入指定的年月：

try:
    yy = int(input("请输入年份：\n"))
    mm = int(input("请输入月份：\n"))
except ValueError:
    print("输入内容不正确！")

print()
# 显示日历
try:
    print(calendar.month(yy,mm))
except ValueError:
    print("输入内容有误，无法显示日历！\n")
input("\n按<Enter>键退出程序！")
