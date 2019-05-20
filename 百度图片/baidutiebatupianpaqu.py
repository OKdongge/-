import requests
import os 
from lxml import etree
from bs4 import BeautifulSoup

class Tieba:
    def __init__(self,query_string):
        self.query_string = query_string
        self.url = 'https://tieba.baidu.com/f'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

    #查询的关键字！
    def params(self):
        para = {
            'ie':'utf-8','kw':self.query_string,'fr':'search'
        }
        return para

    #1.发送请求的函数
    def send_request(self,url,params={}):
        response = requests.get(url,params=params,headers=self.headers)
        return response.content

    #2.数据清洗xpath
    """def parse_data(self,data,rule):
        html_data = etree.HTML(data)
        data_list = html_data.xpath(rule)
        return data_list"""
    #2.使用beautifulsoup重构
    def parse_data(self,data):
        soup = BeautifulSoup(data)
        










    #3.存储数据 
    def save_data(self,data,name):
        #创建文件夹
        base_path = 'D://szl/tieba_image/' + str(self.query_string) + '/'
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        path = base_path + name
        with open(path,'wb') as f:
            f.write(data)
            print(name)   

    def run(self):
        params_data = self.params()
        html = self.send_request(self.url,params_data)
        html_new = html.decode('utf-8').replace(r'<!--','"').replace(r'-->','"')
        detail_rule = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        #总的帖子地址
        href_list = self.parse_data(html_new,detail_rule)
        image_rule = '//img[@class="BDE_Image"]/@src'
        #全部图片列表
        for item in href_list[:15]:
            #每一个帖子的地址
            detail_url = 'https://tieba.baidu.com' + item
            #每一个帖子的信息
            detail_data = self.send_request(detail_url)
            image_url = self.parse_data(detail_data,image_rule)
            for index in image_url:
                if index:
                    image_data = self.send_request(index)
                    image_name = index[-15:]
                    self.save_data(image_data,image_name)
        print('爬取完成，共获取{}个帖子，总共{}张图片'.format(15,'未知'))
    
if __name__ == "__main__":
    a = input('请输入你要查询的关键字：')
    tieba = Tieba(a)
    tieba.run()

