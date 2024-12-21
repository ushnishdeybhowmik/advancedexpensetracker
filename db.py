import sqlite3

db_name = "expense_tracker.db"

connection = sqlite3.connect(db_name)

def get_users_name():
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM users")
    return [name[0] for name in cursor.fetchall()]

def create_user(name, mobno=1234567890):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, mobno) VALUES (?, ?)", (name, mobno))
    connection.commit()
    
def get_user_id(name):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM users WHERE name = ?", (name,))
    return cursor.fetchone()
    
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
        
def create_txn_table():
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS txn (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount INTEGER NOT NULL,
        description TEXT,
        payment_mode TEXT,
        txn_id TEXT,
        paid_at DATETIME,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    connection.commit()
    
def add_txn(user_id, amount, description, payment_mode, txn_id, paid_at):
    cursor = connection.cursor()
    cursor.execute("""
                   INSERT INTO txn (user_id, amount, description, payment_mode, txn_id, paid_at)
                   VALUES (?, ?, ?, ?, ?, ?)
                   """, (user_id,amount, description, payment_mode, txn_id, paid_at))
    connection.commit()
    
def get_all_txn():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM txn")
    return cursor.fetchall()

def get_txn_columns():
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(txn)")
    return [column[1] for column in cursor.fetchall()]
    
def get_all_txn_with_names():
    cursor = connection.cursor()
    cursor.execute("SELECT txn.id, users.name, txn.amount, txn.description, txn.payment_mode, txn.txn_id, txn.paid_at, txn.created_at FROM txn JOIN users ON txn.user_id = users.id")
    return cursor.fetchall()

create_user_table()
create_txn_table()