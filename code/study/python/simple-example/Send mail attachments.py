# Send mail attachments
# 发送邮件附件

# Author: zhangzhp
# Date: 2017-8-21 09:47:30

# 导入包
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP服务

sender = 'joker_zzp@163.com'     # 发送人
receiver = '468462891@qq.com'    # 接收人
subject = '好久不见'              # 标题
smtpServer = 'smtp.163.com'      # 代理服务器

username = sender                # 用户名
password = 'joker1995'           # 密码

# 邮件正文内容
mail_msg ='''好好学习，天天向上！'''

# 构造附件1: ../foo.txt
att1 = MIMEText(open('foo.txt','rb').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="foo.txt"'

# 创建一个带附件的实例
message = MIMEMultipart()
message['Subject'] = Header(subject,'utf-8')
message['From'] = sender
message['To'] = receiver
# 正文
message.attach(MIMEText(mail_msg,'plain','utf-8'))
# 附件
message.attach(att1)

try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpServer)
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,message.as_string())
    print("\n发送邮件成功！")
except Exception:
    print("\n发送失败！")


