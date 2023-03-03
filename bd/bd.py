import sqlite3

conn = sqlite3.connect('contas.db')

c = conn.cursor()

c.execute('''CREATE TABLE usuarios
             (username text, password text)''')

conn.commit()

conn.close()


