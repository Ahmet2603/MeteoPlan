import sqlite3
from datetime import datetime

DATABASE_NAME = "meteo_plan.db"


def get_connection():
    """SQLite veritabanı bağlantısı oluşturur."""
    return sqlite3.connect(DATABASE_NAME)


def init_database():
    """Gerekli tabloları oluşturur."""
    connection = get_connection()
    cursor = connection.cursor()

    # Hava durumu arama geçmişi
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            country TEXT,
            temperature REAL,
            description TEXT,
            searched_at TEXT NOT NULL
        )
    """)

    # Kullanıcı notları
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            selected_hour TEXT,
            note TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    # Favori şehirler
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL UNIQUE,
            added_at TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()


def save_weather_history(city, country, temperature, description):
    """Hava durumu aramasını geçmişe kaydeder."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO weather_history
        (city, country, temperature, description, searched_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        city,
        country,
        temperature,
        description,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_weather_history():
    """Hava durumu geçmişini getirir."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT city, country, temperature, description, searched_at
        FROM weather_history
        ORDER BY id DESC
    """)

    history = cursor.fetchall()
    connection.close()

    return history


def save_note(city, selected_hour, note):
    """Yeni not kaydeder."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO notes
        (city, selected_hour, note, created_at)
        VALUES (?, ?, ?, ?)
    """, (
        city,
        selected_hour,
        note,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_notes(city=None):
    """Notları getirir. Şehir verilirse sadece o şehrin notlarını getirir."""
    connection = get_connection()
    cursor = connection.cursor()

    if city:
        cursor.execute("""
            SELECT id, city, selected_hour, note, created_at
            FROM notes
            WHERE city = ?
            ORDER BY id DESC
        """, (city,))
    else:
        cursor.execute("""
            SELECT id, city, selected_hour, note, created_at
            FROM notes
            ORDER BY id DESC
        """)

    notes = cursor.fetchall()
    connection.close()

    return notes


def delete_note(note_id):
    """Belirtilen notu siler."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )

    connection.commit()
    connection.close()


# Program başlatıldığında veritabanını hazırla
init_database()

def add_favorite(city):
    """Şehri favorilere ekler."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO favorites (city, added_at)
        VALUES (?, datetime('now'))
    """, (city,))

    connection.commit()
    connection.close()


def get_favorites():
    """Favori şehirleri getirir."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, city, added_at
        FROM favorites
        ORDER BY added_at DESC
    """)

    favorites = cursor.fetchall()

    connection.close()

    return favorites


def delete_favorite(favorite_id):
    """Favori şehri siler."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM favorites WHERE id = ?",
        (favorite_id,)
    )

    connection.commit()
    connection.close()