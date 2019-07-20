import requests
from bs4 import BeautifulSoup
import chardet
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
url = 'https://www.booktxt.net/0_595/'

res = requests.get(url,headers=headers)
html = res.content

soup = BeautifulSoup(html,'lxml')
dd_list = soup.find_all('dd')
for item in dd_list[-2:]:
    href = item.a.get('href')
    new_url = url + href
    character_data = requests.get(new_url).content
    new_soup = BeautifulSoup(character_data,'lxml')
    content = new_soup.find(id="content")
    fashi = content.get_text().replace('',r'\r\n')
    with open('fahsi.txt','w',encoding='utf-8') as f:
       f.write(fashi)

#邮件提醒功能
