"""import stmplib
from email.mime.text import MIMEText
from email.mime.multipart imort MIMEMultipart
from emai.header import Header

class send_email(self,title,path,name):
    message = MIMEMultipart()#创建一个可以发送附件的的对象
    message['Form'] = self.sender
    message['To'] = ';'join(self,receivers)
    message['Subject'] = Header(title,'utf-8')
    message.attach(MIMEText(text,'plain','utf-8'))

    att = MIMEText('第2834章 黑色警戒.txt','base64','utf-8')#注意一下
    att['Content-Type'] = 
"""

# 发邮件的库
import smtplib
#邮件文本
from email.mime.text import MIMEText

# smtp服务器
SMTPServer ="smtp.qq.com"

# 发邮件的地址
Sender = "1098498321@qq.com"

#发送者邮箱的密码
passwd = "yourpassword"

# 设置发送的内容
message = "hockel is a good men "

# 转换成邮件文本
msg = MIMEText(message)

# 标题
msg["Subject"] = "来自帅哥的问候"

#发送者
msg["From"] = Sender

#    创建SMTP服务器       服务器    端口号
mailServer = smtplib.SMTP(SMTPServer, 25)

#登录邮箱
mailServer.login(Sender, passwd)

# 发送邮件
for x in range(1,2):
    mailServer.sendmail(Sender, ["szl1452@163.com"],msg.as_string())
    x += 1
# 退出邮箱
mailServer.quit()
