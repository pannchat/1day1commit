import sqlite3
conn = sqlite3.connect('./resource/database.db')

c = conn.cursor()

# c.execute("UPDATE users SET username=? WHERE id=?", ("niceman",3))

# c.execute("UPDATE users SET username=:name WHERE id=:id", {"name": 'goodman', 'id':5})

# c.execute("UPDATE users SET username='%s' WHERE id='%s'" % ("badboy", 1))

#삭제

print(conn.execute("DELETE FROM users").rowcount)

conn.commit()
conn.close()
