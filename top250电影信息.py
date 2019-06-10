import requests 
from lxml import etree
import csv

#思路
#先获取信息
def get_data(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    s = etree.HTML(res.text)
    Title = s.xpath('//div[@class="info"]/div/a/span[1][@class="title"]/text()')
    Score = s.xpath('//div[@class="bd"]/div[1]/span[@class="rating_num"]/text()')
    Inq = s.xpath('//div[@class="bd"]/p[@class="quote"]/span/text()')
    Star = s.xpath('//div[@class="bd"]/div/span[4]/text()')
    #将信息以字典形式存储！   [{},{},{}]的形式
    movieInfoList = []
    for each in range(25):
        movieDict = {}  
        movieDict['title'] = Title[each]
        movieDict['score'] = Score[each]
        movieDict['inq'] = Inq[each]
        movieDict['star'] = Star[each]
        print(movieDict)
        movieInfoList.append(movieDict)
    return movieInfoList    

def writeData(movielist):
    with open('Douban.csv','a+',encoding='utf-8',newline='') as ft:
        writer = csv.DictWriter(ft,fieldnames=['title','score','inq','star'])#制表
        writer.writeheader()#写入表头
        for each in movielist:
            writer.writerow(each)


if __name__ == "__main__":
    result = []
    baseurl = 'https://movie.douban.com/top250'
    urlList = [baseurl + '?start=' + str(25*index) for index in range(10)]
    for url in urlList:
        list = get_data(url)
        result += list 
    print(result[-10:])
    writeData(result)

#文件存储错误
















