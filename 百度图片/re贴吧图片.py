import requests 
import re 
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent':ua.random}
url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%85%A8%E8%81%8C%E6%B3%95%E5%B8%88'

html = requests.get(url,headers=headers)
html_new = html.content.decode('utf-8').replace(r'<!--','"').replace(r'-->','"')

pattern = re.compile(r'/p/\d+')
href_list = pattern.findall(html_new)
if href_list:
    print(href_list[:5])
else:
    print('error')