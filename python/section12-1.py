import sqlite3
import datetime

now = datetime.datetime.now()
print('now : ', now)
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)
print('sqlite3.version :', sqlite3.version)
print('sqlite3.sqlite_version: ', sqlite3.sqlite_version)

conn = sqlite3.connect('./resource/database.db', isolation_level=None)
c = conn.cursor()
# print('Cursor Type: ', type(c))
#Cursor Type:  <class 'sqlite3.Cursor'>
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,\
 username text, email text, phone text, website text, regdate text)")
# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'kim', 'admin@admin.com', '010-0000-0000',\
     'kim.com', ?)", (nowDatetime,)
     )
# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2, 'park', 'park@admin.conm', '010-1111-1111', 'park.com', nowDatetime))

userList = (
    (3, 'lee', 'lee@naver.com', '010-1234-1234', 'lee.com', nowDatetime),
     (4, 'cho', 'cho@naver.com', '010-4321-1234', 'cho.com', nowDatetime),
      (5, 'yoo', 'yoo@naver.com', '010-0000-0000', 'yoo.com', nowDatetime),

)

c.executemany('INSERT INTO users(id, username, email, phone, website, regdate) \
    VALUES (?,?,?,?,?,?)', userList)

# conn.execute('DELETE FROM users')
# print("users db deleted: ", conn.execute('DELETE FROM users').rowcount)