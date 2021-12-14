import sqlite3
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()

    id = input('아이디를 입력해주세요: ')
    sql = 'DELETE FROM topics WHERE id = ?'
    cursor.execute(sql, [id])
