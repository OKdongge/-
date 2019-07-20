import requests
import smtplib
import os
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

class Mailhelper():
    def __init__(self):
        self.mail_host = "smtp.qq.com"
        self.mail_user = "1098498321@qq.com"
        self.mail_pass = "oqfopmwewmebgiih"
        self.port = '25'
        self.temp = {'history':None}

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
    
    def get_data(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
        res = requests.get(url,headers=headers)
        html = res.content
        return html

    def parse_data(self,data):
        soup = BeautifulSoup(data,'lxml')
        #针对最后一条信息如果相同，则不返回，不同则爬取
        item = soup.find_all('dd')[-1]:
        href = item.a.get('href')
        #获得章节名
        chapter_name = item.string
        new_url = url + href
        character_data = requests.get(new_url).content
        new_soup = BeautifulSoup(character_data,'lxml')
        content = new_soup.find(id="content")
        fashi = chapter_name + '\n' + content.get_text().replace('\xa0\xa0\xa0\xa0','\n')
        return fashi
    
    def save_file(self,chapter_name):
        #name未知
        path = 'D://szl/upgrate_file' + chapter_name + '.txt'
        with open(path,'w') as f:
            f.write(fashi)
        return path

    def check(self,new):
        if os.path.exists(new):
            print('未更新！')
        else：
            self.save_file(path)
            self.send_mail()

    def run(self,url):
        html = self.get_data(url)
        fshi1 = self.parse_data(html)
        new_path =self.save_file() #文件路径
        self.check(new_path)

if __name__ == '__main__':
    url = 'https://www.booktxt.net/0_595/'
    mailto_list=['szl1452@163.com']
    helper = Mailhelper()
    helper.send_mail(mailto_list,chapter_name, fashi)
    helper.run()
"""
    def save_file(self):
        with open(path,'wb') as f:
            f.write(update_file)
    
    def check(self):
        history = self.temp['history']
        if history:
            now = self.parse_data()
            #比较两个结果相同吗
            if history ！= now：
                history = now
            else:
                return None
        else:
            history = self.parse_data()
            return history
"""



    