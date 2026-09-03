import sqlite3

conn = sqlite3.connect("uchet.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE  TABLE IF NOT EXISTS uchet (
        id INTEGER PRIMARY KEY,
        category TEXT,
        amount INTEGER
    )
""")

print("1 - Добавить расход, 2 - Показать все, 3 - Итоги по категориям, 4 - Общая сумма, 5 - Выход")
while True:
    x = int(input("Выбери:"))
    if x == 1:
        name = input("Категория:") 
        price = int(input("Цена:"))
        cursor.execute("INSERT INTO uchet (category, amount) VALUES (?, ?)", (name, price))
        print("Добавлено!")
    elif x == 2:
        print("--- Все категории: ---")
        cursor.execute("SELECT * FROM uchet")
        for row in cursor.fetchall():
            print(row)
    elif x == 3:
        cursor.execute("SELECT category, SUM(amount) FROM uchet GROUP BY category")
        for row in cursor.fetchall():
            print(row)
    elif x == 4:
        cursor.execute("SELECT SUM(amount) FROM uchet")
        for row in cursor.fetchall():
            print(row)
    else:
        print("Всего доброго!")
        break
    
conn.commit()
conn.close()