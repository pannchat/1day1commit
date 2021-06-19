import sqlite3
conn = sqlite3.connect('./resource/database.db')

#커서 바인딩
c = conn.cursor()

#데이터 조회(전체)
c.execute("SELECT * FROM users")

# for row in c.fetchall():
#     print('retrieve1 > ', row)

# for row in c.execute("SELECT * FROM users ORDER BY id desc"):
#     print('retrieve2 > ', row)

# WHERE

# param1= (3,)
# c.execute("SELECT * FROM users WHERE id=?", param1)
# print('param1', c.fetchone())
# print('param1', c.fetchall())
# param2= 4
# c.execute("SELECT * FROM users WHERE id='%s'" % param2)
# print('param2', c.fetchone())
# print('param2', c.fetchall())


# c.execute("SELECT * FROM users WHERE id=:Id" , {"Id":5})
# print('param2', c.fetchone())
# print('param2', c.fetchall())


# c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2" ,{'id1':2, 'id2':5})
# print(c.fetchall())

# with conn:
#     with open('./resource/dump.sql', 'w') as f:
#         for line in conn.iterdump():
#             f.write('%s\n' % line)
#         print('dump print complete')