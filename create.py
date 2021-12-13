import sqlite3
connect = sqlite3.connect('data.db')
cursor = connect.cursor()

title = input('제목을 알려주세요: ')
body = input('본문을 알려주세요: ')

sql = 'INSERT INTO topics (title, body) VALUES("'+title+'","'+body+'")'
cursor.execute(sql)

connect.commit()
cursor.close()
connect.close()