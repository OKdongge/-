name = ['hj','jz']
age = [56,65]

list = []

for i in range(2):
	dict = {}
	dict['name'] = name[i]
	dict['age'] = age[i]
	print(dict)
	list.append(dict)
	
print(list)