import sqlite3

db_name = "expense_tracker.db"

connection = sqlite3.connect(db_name)

def get_users_name():
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM users")
    return cursor.fetchall()

def create_user(name, mobno=1234567890):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, mobno) VALUES (?, ?)", (name, mobno))
    connection.commit()
    



def create_user_table():     
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            mobno INTEGER NOT NULL,
            total_paid INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        connection.commit()