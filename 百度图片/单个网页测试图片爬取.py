import requests
from lxml import etree
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%85%A8%E8%81%8C%E6%B3%95%E5%B8%88'

html = requests.get(url,headers=headers)
html_new = html.content.decode('utf-8').replace(r'<!--','"').replace(r'-->','"')
soup = BeautifulSoup(html_new,'lxml')
tag_list = soup.find_all("a",class_="j_th_tit ")
#输出由50个帖子的列表(bs4.element.ResultSet)
for i,index in enumerate(tag_list,start=1):
    href = index.get('href')
    detail_url = 'https://tieba.baidu.com' + href
    page_html = requests.get(detail_url,headers=headers)
    page_html_new = page_html.content.decode('utf-8').replace(r'<!--','"').replace(r'-->','"')
    soup_img = BeautifulSoup(page_html_new,'lxml')
    img_data_list = soup_img.find_all("img",class_="BDE_Image")
    for img in img_data_list:
        img_src = img.get('src')
        img_data = requests.get(img_src,headers=headers).content
#以数字后十位命名
        base_path = 'D://szl/new_folder/' 
        fname = img_src[-12:]
        with open(base_path+fname,'wb') as f:
            f.write(img_data)
        print(fname)
        break    


"""
url = 'https://tieba.baidu.com/p/5747954969'
data = requests.get(url,headers=headers)
html = data.content.decode('utf-8').replace(r'<!--','"').replace(r'-->','"')
soup = BeautifulSoup(html,'lxml')
img_list = soup.find_all("img",class_="BDE_Image")
for i,index in enumerate(img_list):
    img_src = index.get('src')
    print(i,img_src) 
"""