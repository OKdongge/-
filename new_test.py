import pymysql

db = pymysql.connect('localhost','root','123456','testdb')#分别是主机、用户、密码、数据库
cursor = db.cursor()#创建一个游标对象cursor

#cursor.execute('SELECT VERSION()')#获取单条数据
#data = cursor.fetchone()
#print("database version:",data)#database version: ('8.0.15',)
'''
#查询empolyee表中大于1的row
sql = "update employee set age = 20 where sex = 'M'"#为什么会不区分m M呢

try:
	cursor.execute(sql)
	db.commit()
	print('successful')
except:
	db.rollback()
	print('failed')

sql = "select * from employee where age > %s " % (1)
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
	print(row)
db.close()

'''
#删除操作

sql = "DELETE FROM EMPLOYEE WHERE AGE < %s " % (5)

try:
	cursor.execute(sql)
	db.commit()
	print('successful')
except:
	db.rollback()
	print('failed')
db.close()

