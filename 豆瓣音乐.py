import requests
import re 
import json
#排行、名称、时间、评分、图片

def get_data(url):
	res = requests.get(url).text
	#regex express
	rank_p = '<i class="board-index board-index.*?">(.*?)</i>'
	title_p = 'p class="name">.*?title="(.*?)" data-act'
	date_p = 'p class="releasetime">(.*?)</p>'
	score_p = '<p class="score">.*?>(.*?)</i><i class="fraction">(\d)</i></p>'
	img_p = 'img data-src="(.*?)" alt'
	#list 
	ranks = re.findall(rank_p,res,re.S)
	titles = re.findall(title_p,res,re.S)
	dates = re.findall(date_p,res,re.S)
	score = re.findall(score_p,res,re.S)
	scores = [score[i][0] + score[i][1] for i in range(len(score))]
	imgs = re.findall(img_p,res,re.S)

	list = []
	for i in range(10):
		dict = {}
		dict['rank'] = ranks[i]
		dict['title'] = titles[i]
		dict['date'] = dates[i]
		dict['score'] = scores[i]
		dict['img'] = imgs[i]
		list.append(dict)
	return list
	
#sace_function		
def save_data(content):
	with open('dianyigntop100.txt','a',encoding='utf-8') as f:
		print(type(json.dumps(content)))
		f.write(json.dumps(content,ensure_ascii=False) + '\n')


if __name__ == '__main__':
	urls = ['https://maoyan.com/board/4?offset={}'.format(10*i) for i in range(10)]
	result = []
	for url in urls:
		list = get_data(url)
		result += list
	for i in result:
		with open('test.txt','a') as f:
			f.write(str(i) + '\n')
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		