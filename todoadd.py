import sqlite3
conn = sqlite3.connect('text_database.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS text_table (id INTEGER PRIMARY KEY, text TEXT)
''')
text = input('What would you like to add to the To-Do List? ')
c.execute("INSERT INTO text_table (text) VALUES (?)", (text,))
conn.commit()
conn.close()
