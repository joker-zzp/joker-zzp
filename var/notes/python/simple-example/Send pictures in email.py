# Send pictures in email
# 发送的email中加图片

# Author: zhangzhp
# Date: 2017-8-21 13:08:51

# 导入包
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 第三方 SMTP服务

def my_email(qq):

  sender = 'joker_zzp@163.com'
  receiver = qq
  subject = '好久不见'
  smtpServer = 'smtp.163.com'

  username = sender
  password = 'joker1995'

  # -------------------- 页面 -------------------- #
  # 创建实例
  message = MIMEMultipart()
  message['Subject'] = Header(subject,'utf-8')
  message['From'] = sender
  message['To'] = receiver

  msgAlternative = MIMEMultipart('alternative')
  message.attach(msgAlternative)

  # 邮件正文内容
  mail_msg = '''
  <h3 align="center">致老友的一封信</h3>
  <p>&nbsp;&nbsp;亲爱的同学：</p>
  <p>&nbsp;&nbsp;好久不见!<br>
  &nbsp;&nbsp;之前，我们曾携手并进，走过人生中最灿烂，最充实的日子;<br>
  &nbsp;&nbsp;之后，我们各自高飞，去了不同的地方追求自己未完成的梦想;<br>
  &nbsp;&nbsp;相信：离别割不断思念，距离冲不淡友谊。为了曾经的一句诺言——“再见了，朋友。”我们决定重新聚首在一起，话思念，聊近况，谈理想。<br>
  &nbsp;&nbsp;相逢是缘分，重聚是情意。在这寒冷的冬季，我们迎来了很有意义的温暖相聚。<br>
  &nbsp;&nbsp;亲爱的TSD1608班同学们，无论你是远在天涯，还是近在咫尺，带着一份温情，一份感动，一份真诚，都积极行动起来吧。来吧!亲爱的同学!等待着你们!期待着你们!热忱欢迎全体同学老师参加本次聚会!!!<br>
  <br>
  聚会时间：2017年9月2日<br>
  聚会地点：我们一起学习奋斗的地方
  </p>

  <p align="center">
    <img height="600" width="800" src="cid:image">
  </p>
  '''
  msgAlternative.attach(MIMEText(mail_msg,'html','utf-8'))

  # 图片目录
  fp = open('../同学照.jpg','rb')
  msgImage = MIMEImage(fp.read())
  fp.close()
  # 定义图片ID，在HTML文本中引用
  msgImage.add_header('Content-ID','<image>')
  message.attach(msgImage)

  # 附件
  # 构造一个附件
  #attachment = MIMEApplication(open('../简明Python教程.pdf','rb').read())
  # windows下文件名编码问题*解决方案(使用gbk编码)
  #attachment.add_header('Content-Disposition','attachment',filename=('gbk','','简明Python教程.pdf'))
  #message.attach(attachment)

  # -------------------- 页面 -------------------- #

  try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpServer)
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,message.as_string())
    print("\n发送成功！")
  except Exception:
    print("\发送失败！")


qq_list = [1437905110,2806250960,554131157,1917696808,505732220,294724326,1730457440,695736259,752924575,2503906994,1012680943,891015136,784265699,1296573522,328848859,179345998,825914178,1713706279]

count = 0
for i in qq_list:
  qq = str(i)+'@qq.com'
  print(qq)
  count += 1
  my_email(qq)

#my_email("283671541@qq.com")
print(count)
print("over !")
