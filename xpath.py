import requests

from lxml import etree

baseurl = 'https://music.douban.com/top250?start='

# 爬取所有的歌曲名单、评分、人数
# 格式要规范
# 


def get_request(url):
	res = requests.get(url).content
	return res


def get_info(html):

	s = etree.HTML(html)

	titles = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/text()') #字符串

	scores = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[2]/text()')

	numbers = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[3]/text()')

	links = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/@href')

	imgpaths = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[1]/a/img/@src')

	for i in range(1,26):
		try:
			result = titles[i].strip()+scores[i]+numbers[i]+links[i]+imgpaths[i]
			return result
		except:
			pass

def save_file(data):
	with open('new_file.txt','w') as f:
		f.write(result) 


if __name__ == "__main__":
	url = [baseurl + str(25*index) for index in range(0,10)]
	for index in url:
		res = get_request(index)
		result = get_info(res)
		save_file(result)
