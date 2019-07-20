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
from email.mime.text import MIMEText

msg = MIMEText('hello.send by python...','plain','utf-8')
from_addr = input('From:')
password = input('Password:')

to_addr = input('To:')
smtp_server = input('SMTP server:')
import smtplib

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()