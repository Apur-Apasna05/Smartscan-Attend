import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_number TEXT,
        name TEXT,
        email TEXT,
        class_name TEXT,
        timestamp TEXT,
        ip_address TEXT,
        status TEXT
    )
''')

conn.commit()
conn.close()

