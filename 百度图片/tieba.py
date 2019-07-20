import requests
from lxml import etree
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

#去除html中的注释部分！
url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%85%A8%E8%81%8C%E6%B3%95%E5%B8%88'

#html = res.content.decode('utf-8')
#html_new = html.replace(r'<!--','"').replace(r'-->','"')

#数据清洗,返回所有标签
def parse_data(html,rule1,class_==rule2):
    html_new = html.decode('utf-8').replace(r'<!--','"').replace(r'-->','"')
    soup = BeautifulSoup(html_new,'lxml')
    tag_list = soup.find_all(rule1,class_=rule2)
    return tag_list

#发送请求
def send_request(url):
    response = requests.get(url,headers=headers)
    return response.content

a_res = send_request(url)
a_rule1 = 'a'
a_rule2 = "j_th_tit " #这个不能传入find_all方法中去
a_list = parse_data(a_res,a_rule1,a_rule2)
print(a_list)

#for i,index in enumerate(a_list,start=1):
 #   a_href = index.get('href')
  #  a_herf_url = 'https://tieba.baidu.com/' + a_href
   # print(i,a_herf_url)

"""img_rule = '"imag",class_="BDE_Image" '

soup = BeautifulSoup(html_new,'lxml')
a_list = soup.find_all("a",class_="j_th_tit ")
#问题出在soup里面没有img的代码，所以要请求帖子代码
img_list = soup.find_all("img")

for i,index in enumerate(img_list[:10]):
    img_url = index.get('src')
    print(i,img_url)

for i,index in enumerate(a_list[:10],start=1):
    tiezi_url = index.get('href')#从标签中获取属性值的方法get
    detail_url = 'https://tieba.baidu.com/' + tiezi_url
    print(i,detail_url)	
"""





