import sqlite3

users_list = [
    (1, 'Denis', '12345678'),
    (2, 'Stanley', 'stan123'),
    (3, 'Bill', 'billboard'),
    (4, 'Anna', 'pass006'),
    (5, 'Corey', 'click')
]

content = [
    (1, 'JoshArt', 20, 'product design', '3 years'),
    (2, 'Kate1998', 20, 'UI design', '2 years')
]


conn = sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS UsersDatabase(ID integer, Username text, Password text)')
cur.executemany('INSERT OR IGNORE INTO UsersDatabase VALUES(?, ?, ?)', users_list)


cur.execute('CREATE TABLE IF NOT EXISTS Information(ID integer, Nickname text, Hourly_Wage integer, Type text, Experience text)')
cur.executemany('INSERT OR IGNORE INTO Information VALUES(?, ?, ?, ?, ?)', content)

conn.commit()
conn.close()
