import sqlite3
conn = sqlite3.connect('text_database.db')
c = conn.cursor()
c.execute("SELECT * FROM text_table")
rows = c.fetchall()
for row in rows:
    print(row[1])
conn.close()
