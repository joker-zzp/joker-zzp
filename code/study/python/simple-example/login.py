#! /usr/bin/python3

# 导入包
import pymysql
import traceback
import time

# 用户连接数据库


class connect_db:
    # 定义基本属性
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 定义登录方法
    def user_login(self):
        try:
            # print (self.user,self.password,self.database)
            self.conn = pymysql.connect(
                self.host, self.user, self.password, self.database)
            print("用户登录成功！")
        except Exception:
            print("错误信息:\n%s" % traceback.format_exc())
            self.conn.close
            print("数据库连接失败！")
            return

    # 定义退出方法
    def user_exit(self):
        try:
            self.conn.close()
            print("退出成功！")
            return
        except Exception:
            print("退出失败！")
            return

    # 延迟退出
    def Delay_exit(self):
        counter = 10
        while counter > 0:
            print(counter)
            time.sleep(1)
            counter -= 1
        else:
            self.user_exit()
        pass

# test
# 传入用户信息


admin = connect_db('localhost', 'admin', 'admin', 'helloworld')

print("正在登录，请稍候……")
admin.user_login()
print("开始退出倒计时！")
admin.Delay_exit()
