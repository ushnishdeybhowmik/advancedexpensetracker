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



    
def add_txn(user_id, amount, description, cat_id,payment_mode, txn_id, paid_at):
    cursor = connection.cursor()
    cursor.execute("""
                   INSERT INTO txn (user_id, category_id, amount, description, payment_mode, txn_id, paid_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?)
                   """, (user_id, cat_id, amount, description, payment_mode, txn_id, paid_at))
    connection.commit()
    
def get_all_txn():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM txn")
    return cursor.fetchall()

def get_txn_columns():
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(txn_records)")
    return [column[1] for column in cursor.fetchall()]
    
def get_all_txn_with_names():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM txn_records")
    return cursor.fetchall()

def get_categories():
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM category")
    return [category[0] for category in cursor.fetchall()]

def create_category(name):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO category (name) VALUES (?)", (name,))
    connection.commit()
    
def get_category_id(name):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM category WHERE name = ?", (name,))
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
        category_id INTEGER NOT NULL,
        amount INTEGER NOT NULL,
        description TEXT,
        payment_mode TEXT,
        txn_id TEXT,
        paid_at DATETIME,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (category_id) REFERENCES category (id)
    )
    """)
    connection.commit()
    
def create_category_table():
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)
    connection.commit()
    
def create_txn_records_view():
    cursor = connection.cursor()
    cursor.execute("""
    CREATE VIEW IF NOT EXISTS txn_records AS
    SELECT txn.id, users.name, txn.amount, txn.description, category.name AS category, txn.payment_mode, txn.txn_id, txn.paid_at 
    FROM txn 
    INNER JOIN users 
    ON txn.user_id = users.id
    INNER JOIN category 
    ON txn.category_id = category.id
    """)
    connection.commit()
    

create_user_table()
create_txn_table()
create_category_table()
create_txn_records_view()