import requests 
from lxml import etree

baseurl = 'https://music.douban.com/top250?start=0'

res = requests.get(baseurl).content

s = etree.HTML(res)

"""    //*[@id="content"]/div/div[1]/div/table[25]/tr/td[2]/div/a
        //*[@id="content"]/div/div[1]/div/table[25]/tr/td[1]/a/img
        //*[@id="content"]/div/div[1]/div/table[25]/tr/td[2]/div/div/span[3]
        //*[@id="content"]/div/div[1]/div/table[25]/tr/td[2]/div/div/span[2]
"""
titles = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/text()') #这是一个列表

scores = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[2]/text()')

numbers = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[3]/text()')

links = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/@href')

imgpaths = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[1]/a/img/@src')


test = s.xpath('//*[@id="content"]/div/div[1]/div/table[16]/tr/td[2]/div/a/text()') #是一个列表！

for i in range(1,26):
    print(titles[i])
	
#	if not titles[i]:
 #       print('哎呀！，%s找不到了'% titles[i])
  #  else:
   #     print(titles[i].strip())
#print(len(titles))
	#result = titles[i].strip()+scores[i]+numbers[i]+links[i]+imgpaths[i]
    #print(result)
    
