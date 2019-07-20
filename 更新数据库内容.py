import pymysql

db = pymysql.connect('localhost','root','123456','testdb')
cursor = db.cursor()

data = {
'firat_name':'zhang',
'last_name':'zihan',
'age':'4'
}
keys = ', '.join(data.keys())
values = ', '.join(['%s']*len(data))

sql = "insert into employee ({keys}) values ({values}) on duplicate key update".format(keys=keys,values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update       #为什么不能实现更新功能？



try:
	if cursor.execute(sql,tuple(data.values())*2): #元组不可少！
		print('successful!')
		db.commit()
except:
	print('failed')
	db.rollback()
db.close()

