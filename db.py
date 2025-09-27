import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("""
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY, 
            title TEXT, 
            author TEXT, 
            genre TEXT,
            pages INTEGER,
            status TEXT
                )
    """)
    conn.commit()
    conn.close()

def insert(title, author, genre, pages, status):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?, ?)",
                 (title, author, genre, pages, status))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM book")
    rows = curr.fetchall()
    conn.close()
    return rows

def search(title="", author="", genre="", status=""):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("""
        CREATE TABLE IF NOT EXISTS book(
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            genre TEXT, 
            pages INTEGER,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("DELETE FROM book WHERE id=?", (id))
    conn.commit()
    conn.close()