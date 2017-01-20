import MySQLdb as m
host='localhost'
username='root'
password='root123'
database='practice'
db_con=m.connect(host,username,password,database)
db_cur=db_con.cursor(m.cursors.DictCursor)
sql="select * from employe"
db_cur.execute(sql)
data=db_cur.fetchall()
for row in data:
	print row

try:
	db_cur.execute(sql)
	db_con.commit()
except:
	db_con.rollback()
