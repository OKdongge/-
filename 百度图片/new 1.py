import requests
from lxml import etree

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
    def parse_data(self,data,rule):
        html_data = etree.HTML(data)
        data_list = html_data.xpath(rule)
        return data_list
    # 
    def run(self):
        params_data = self.params()
        html = self.send_request(self.url,params_data)
        html_new = html.decode('utf-8').replace(r'<!--','"').replace(r'-->','"')
        detail_rule = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        href_list = self.parse_data(html_new,detail_rule)
        for item in href_list:
            url_list = 'https://tieba.baidu.com' + item
            print(url_list)

if __name__ == "__main__":
    a = input('请输入你要查询的关键字：')
    tieba = Tieba(a)
    tieba.run()