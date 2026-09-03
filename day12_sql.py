import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE  TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        category TEXT,
        amount INTEGER
    )
""")

cursor.execute("INSERT INTO expenses (category, amount) VALUES ('еда', 20)")
cursor.execute("INSERT INTO expenses (category, amount) VALUES ('транспорт', 15)")
cursor.execute("INSERT INTO expenses (category, amount) VALUES ('еда', 35)")
conn.commit()


print("---Все расходы---")
cursor.execute("SELECT * FROM expenses")
for row in cursor.fetchall():
    print(row)


print("---Больше 15---")
cursor.execute("SELECT * FROM expenses WHERE amount > 15")
for row in cursor.fetchall():
    print(row)


print("---Итоги по категориям---")
cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
for row in cursor.fetchall():
    print(row)

conn.close()