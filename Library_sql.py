import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY,
        name TEXT,
        country TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,     
        author_id INTEGER,
        year INTEGER,
        pages INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(id)
    )
""")


cursor.execute("SELECT COUNT(*) FROM authors")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO authors (name, country) VALUES (?, ?)",
                   [('Лев Толстой', 'Россия'),
                    ('Джордж Оруэлл', 'Великобритания'),
                    ('Харуки Мураками', 'Япония')])

    cursor.executemany("INSERT INTO books (title, author_id, year, pages) VALUES (?, ?, ?, ?)",
                   [('Война и мир', 1, 1869, 1225),
                    ('Анна Каренина', 1, 1878, 864),
                    ('1984', 2, 1949, 328),
                    ('Скотный двор', 2, 1945, 112),
                    ('Норвежский лес', 3, 1987, 296),
                    ('Кафка на пляже', 3, 2002, 505)])
    conn.commit()

print("Все книги с именами авторов:")
cursor.execute("""
    SELECT books.title, authors.name
    FROM books
    JOIN authors ON books.author_id = authors.id
    ORDER BY books.author_id
""")
for row in cursor.fetchall():
    print(row)

print("Книги по году:")
cursor.execute("""
    SELECT books.title, books.year
    FROM books
    ORDER BY books.year
""")
for row in cursor.fetchall():
    print(row)

print("Сколько книг у каждого автора:")
cursor.execute("""
    SELECT authors.name, count(*)
    FROM books
    JOIN authors ON books.author_id = authors.id
    GROUP BY authors.name
    ORDER BY authors.name
""")
for row in cursor.fetchall():
    print(row)

print("Самая толстая книга:")
cursor.execute("""
    SELECT books.title, books.pages
    FROM books
    ORDER BY pages DESC
    LIMIT 1
""")
for row in cursor.fetchall():
    print(row)

print("Средний объём книг по каждому автору:")
cursor.execute("""
    SELECT authors.name, AVG(books.pages)
    FROM books
    JOIN authors ON books.author_id = authors.id
    GROUP BY authors.name
    ORDER BY authors.name
""")
for row in cursor.fetchall():
    print(row)