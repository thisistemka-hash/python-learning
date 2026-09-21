import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT, price INTEGER)")
cursor.executemany("INSERT INTO items (name, price) VALUES (?, ?)",
                   [("стол", 100), ("стул", 40), ("стелаж", 180)])
conn.commit()

cursor.execute("SELECT * FROM items WHERE price < 50")
print("под изменения попадут:", cursor.fetchall())

cursor.execute("UPDATE items SET price = price + 10 WHERE price <50")
print("изменено строк:", cursor.rowcount)
conn.commit()

cursor.execute("SELECT * FROM items ORDER BY price")
print("после:", cursor.fetchall())

cursor.execute("SELECT name FROM items WHERE name LIKE 'ст%'")
print("на ст-:", cursor.fetchall())

cursor.execute("SELECT name, price FROM items WHERE price BETWEEN 30 AND 110")
print("30..110:", cursor.fetchall())

cursor.execute("SELECT name FROM items WHERE name IN ('стол', 'лампа', 'нет такого')")
print("из списка:", cursor.fetchall())

cursor.execute("DELETE FROM items WHERE name = 'диван'")
print("удалено:", cursor.rowcount)

conn.close()