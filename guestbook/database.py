import sqlite3
from datetime import date

DATABASE = 'guestbook.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_all_messages():
    conn = get_db_connection()
    messages = conn.execute(
        'SELECT * FROM messages ORDER BY created_at DESC'
    ).fetchall()
    conn.close()
    return messages

# Функция для добавления тестовых данных (вызови один раз, потом закомментируй)
def add_test_messages():
    conn = get_db_connection()
    test_messages = [
        ('Анна', 'Отличный сайт! Спасибо!', '2026-06-01'),
        ('Иван', 'Очень полезная информация', '2026-05-30'),
        ('Мария', 'Здорово, что есть такая гостевая книга', '2026-05-28'),
        ('Петр', 'Жду новых обновлений!', '2026-05-25')
    ]
    for name, message, created_at in test_messages:
        conn.execute(
            'INSERT INTO messages (name, message, created_at) VALUES (?, ?, ?)',
            (name, message, created_at)
        )
    conn.commit()
    conn.close()
    print("✓ Тестовые сообщения добавлены!")
