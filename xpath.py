import requests
import csv
from lxml import etree

baseurl = 'https://music.douban.com/top250?start='

def get_data(url):
	res = requests.get(url).content
	s = etree.HTML(res)
	#titles = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/text()') #字符串
	titles = s.xpath('//tr[@class="item"]/td[2]/div/a/text()')
	scores = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[2]/text()')

	numbers = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[3]/text()')

	links = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/@href')

	imgpaths = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[1]/a/img/@src')
	
	list = []
	for each in range(25):
		Dict = {}
		Dict['title'] = titles[each].strip()
		Dict['score'] = scores[each]
		Dict['number'] = numbers[each].strip().replace(' ','').replace('\n','')
		Dict['link'] = links[each]
		#print(Dict)
		list.append(Dict)
	return list

def save_file(list):
	with open('doubanmusic.csv','w',encoding='utf-8') as ft:
		writer = csv.DictWriter(ft,fieldnames=['title','score','number','link'])
		writer.writeheader()
		for each in list:
			writer.writerow(each)

if __name__ == "__main__":
	urllist = [baseurl + str(25*index) for index in range(10)]
	musiclist = []
	for url in urllist:
		result = get_data(url)
		musiclist += result
		save_file(musiclist)