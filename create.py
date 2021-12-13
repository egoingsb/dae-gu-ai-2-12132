import sqlite3
connect = sqlite3.connect('data.db')
cursor = connect.cursor()

title = input('제목을 알려주세요: ')
body = input('본문을 알려주세요: ')

sql = 'INSERT INTO topics (title, body) VALUES(?,?)'
cursor.execute(sql, (title, body))

connect.commit()
cursor.close()
connect.close()