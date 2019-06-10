import requests 
import csv
import lxml.html

def getSource(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

def getEveryItem(source):
    selector = lxml.html.document_fromstring(source)
    movieItemList = selector.xpath('//div[@class="info"]')

    movieList = []
    for eachMovie in movieItemList:
        movieDict = {}
        title = eachMovie.xpath('div[@class="hd"]/a/span[@class="title"]/text()')
        otherTitle = eachMovie.xpath('div[@class="hd"]/a/span[@class="other"]/text()')
        link = eachMovie.xpath('div[@class="hd"]/a/@href')

        movieDict['title'] = ''.join(title + otherTitle)
        movieDict['link'] = link    
        print(movieDict)
        movieList.append(movieDict)

    return movieList

def writeData(movielist):
    with open('Douban_new.csv','w',encoding='utf-8',newline='') as ft:
        writer = csv.DictWriter(ft,fieldnames=['title','link'])#制表
        writer.writeheader()#写入表头
        for each in movielist:
            writer.writerow(each)

if __name__ == "__main__":
    doubanurl = 'https://movie.douban.com/top250?start={}&filter='
    result = []
    for i in range(10):
        pageLink  = doubanurl.format(i*25)
        print(pageLink)
        source  = getSource(pageLink)
        result += getEveryItem(source)

  #  print(result[:10])
    writeData(result) 