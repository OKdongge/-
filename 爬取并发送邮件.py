import requests
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

class Mailhelper():
    def __init__(self):
        self.mail_host = "smtp.qq.com"
        self.mail_user = "1098498321@qq.com"
        self.mail_pass = "oqfopmwewmebgiih"
        self.port = '25'

    def send_mail(self, to_list, sub, content):
        me = "更新了！！" + "<"+ self.mail_user + ">"
        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            server = smtplib.SMTP(self.mail_host,self.port)
            server.connect(self.mail_host) 
            server.login(self.mail_user,self.mail_pass)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            print('Done')
        except Exception as e:
            print(str(e))
            return False


if __name__ == '__main__':
    mailto_list=['szl1452@163.com']
    helper = Mailhelper()


    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    url = 'https://www.booktxt.net/0_595/'
    res = requests.get(url,headers=headers)
    html = res.content
    soup = BeautifulSoup(html,'lxml')
    dd_list = soup.find_all('dd')

    for item in dd_list[-3:]:
        href = item.a.get('href')
        #获得章节名
        chapter_name = item.string
        new_url = url + href
        character_data = requests.get(new_url).content
        new_soup = BeautifulSoup(character_data,'lxml')
        content = new_soup.find(id="content")
        fashi = chapter_name + '\n' + content.get_text().replace('\xa0\xa0\xa0\xa0','\n')
        helper.send_mail(mailto_list,fashi[:15], fashi)#发送到邮箱
    



#实时监控更新

    