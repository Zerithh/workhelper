import sqlite3
import os

# Шлях до бази даних
DB_PATH = os.path.join("db", "guidebot.db")


def init_db():
    # Створити папку db, якщо її нема
    os.makedirs("db", exist_ok=True)

    # Підключення до бази даних
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Таблиця турів
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tours (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    # Таблиця екскурсій
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS excursions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tour_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            FOREIGN KEY (tour_id) REFERENCES tours(id) ON DELETE CASCADE
        )
    ''')

    # Таблиця туристів
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tourists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tour_id INTEGER NOT NULL,
            full_name TEXT NOT NULL,
            FOREIGN KEY (tour_id) REFERENCES tours(id) ON DELETE CASCADE
        )
    ''')

    # Таблиця оплат
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tourist_id INTEGER NOT NULL,
            excursion_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            paid BOOLEAN NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (tourist_id) REFERENCES tourists(id) ON DELETE CASCADE,
            FOREIGN KEY (excursion_id) REFERENCES excursions(id) ON DELETE CASCADE
        )
    ''')

    # Зберегти зміни та закрити з’єднання
    conn.commit()
    conn.close()


# Функція для отримання підключення до бази (буде використовуватись в інших модулях)
def get_connection():
    return sqlite3.connect(DB_PATH)
