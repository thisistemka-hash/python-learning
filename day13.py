import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        category_id INTEGER,
        amount INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
""")

cursor.execute("SELECT COUNT(*) FROM categories")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO categories (name) VALUES (?)",
                       [('Еда',),('Транспорт',),('Развлечения',)])
    cursor.executemany("INSERT INTO expenses (category_id, amount) VALUES (?, ?)",
                       [(1, 20),(2, 15),(1, 35), (3, 50), (1, 10)])
    conn.commit()

print("--- Расходы с названиями категорий ---")
cursor.execute("""
    SELECT expenses.amount, categories.name
    FROM expenses
    JOIN categories ON expenses.category_id = categories.id
""")
for row in cursor.fetchall():
    print(row)

print("--- Итоги по категориям, по убыванию ")
cursor.execute("""
    SELECT categories.name, COUNT(*), SUM(expenses.amount)
    FROM expenses
    JOIN categories ON expenses.category_id = categories.id
    GROUP BY categories.name
    ORDER BY SUM(expenses.amount) DESC
""")
for row in cursor.fetchall():
    print(row)

print("--- Топ-2 самых больших расхода ---")
cursor.execute("""
    SELECT categories.name, expenses.amount
    FROM expenses
    JOIN categories ON expenses.category_id = categories.id
    ORDER BY amount DESC
    LIMIT 2
""")
for row in cursor.fetchall():
    print(row)

conn.close()