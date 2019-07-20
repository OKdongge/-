import requests
import time 
import json
import jieba
from matplotlib import pyplot as plt
from WordCloud import WordCloud
from bs4 import BeautifulSoup

data = []

def get_data(url):
    #使用ios的模式模拟
    headers = {
        "User-Agent":'Mozilla/5.0 (iPad; CPU OS 11_0… Mobile/15A5341f Safari/604.1'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
url = 'http://m.maoyan.com/movie/248172/comments?'
#print(get_data(url))

def parse_data(html):
    data = json.loads(html)['data']['comments']
    comment = []
    for items in data:
        content = item['content'].replace('\n','')
        comment.append(content)
        return comment

def save_data():
    for i in ragne(1,60):
        stat_time = time.time()
        stat_time= '%.3f'%stat_time
        now_time = stat_time.split('.')
        request_time = now_time[0] + now_time[1]
        offset = (i-1)*15


#导入背景图
bd_img = plt.imread('妇联四.jpg')
WordCloud(width=1024,height=700,backgroud_color='white')
wc.generate_form_text(word)

with open('猫眼电影.txt','r',encoding='utf-8') as f:


plt.axis('off')
plt.show()
wc.to_file('妇联4.jpg')


if if __name__ == "__main__":
    pass



