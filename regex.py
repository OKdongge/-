import json

str = '''
[
{"name":"志立","gender":"male","birthday":"1992-10-18"},
{"name":"志龙","gender":"female","birthday":"1995-10-18"}
]

'''      	       #还是字符串
b = list(str)
data = json.loads(str)

with open('data.json','r') as f:
	#f.write(json.dumps(data,ensure_ascii=False,indent=2))
	re = f.read()
	print(re)  
	print('retype:',type(re))  #json格式字符串  
	la = json.loads(re)
	print(la)
	print('latype:',type(la))  #list