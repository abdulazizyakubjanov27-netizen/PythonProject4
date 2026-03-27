import sqlite3

conn = sqlite3.connect("crawler_data.db")
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS pages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    title TEXT
)
''')
conn.commit()
conn.close()