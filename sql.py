import pymysql.cursors
import data
bind_address = '127.0.0.1'
connection = pymysql.connect(
	host=bind_address,
	user='root',
	password='123'
	)
create = """create database my_db
			use my_db;
			CREATE_TABLE some_table(  'id' INT NOT NULL AUTO_INCREMENT, 'some_text' VARCHAR(255) NULL, PRIMARY KEY ('id'));
         """
for element in create.split(';'):
	try:
		print(element)
		connection.cursor().execute(element)
		connection.commint()
	except:
		print('FAIL IN' + str(element))
connection.close()

connect = pymysql.connect(host='localhost',
						  user='root',
						  password='123',
						  db='my_sql',
						  cursorclass=pymysql.cursor.DirCursor)
with connect.cursor() as cursor:
	cursor.execute("""now tables""")
	print(cursor.fetchall())
	cursor.execute("""insert into some_table (some_text) value('Пример')""")
connect.commit()
with connect.cursor() as cursor:
	cursor.execute("""select * from some_tables""")
	print(cursor.fetchall)
connect.close()