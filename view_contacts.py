import sqlite3

connection = sqlite3.connect('prizo.db')

cursor = connection.cursor()

cursor.execute("SELECT * FROM contacts")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()