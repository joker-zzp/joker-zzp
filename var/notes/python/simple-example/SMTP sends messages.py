# coding:UTF-8
# SMTP sends messages
# SMTP发送邮件

# Author: zhangzhp
# Date: 2017-8-18 15:02:36

# 导入包
import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
# 公司授权吗jDmL35BHH4QT4Qqm
# 第三方 SMTP 服务
sender = 'joker_zzp@163.com'
receiver = '468462891@qq.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'joker_zzp@163.com'
password = 'joker1995'

# 邮件内容
mail_msg = '''
<p>Python 邮件发送测试...</p>
<p>
  <a href="http://www.runoob.com">这是一个连接</a>
</p>
'''

def mail():
    ret = True
    try:
        msg = MIMEText(mail_msg,'html','utf-8')
        msg['Subject'] = Header(subject,'utf-8')
        msg['From'] = sender
        msg['To'] = receiver

        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username,password)
        smtp.sendmail(sender,receiver,msg.as_string())
    except Exception:
        ret = False
    return ret


ret = mail()
if ret:
    print('发送成功！')
else:
    print('发送失败！')


