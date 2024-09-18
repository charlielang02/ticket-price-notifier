import sqlite3

def connect_db():
    conn = sqlite3.connect('ticket_tracker.db')
    return conn

def register_user(email, artist):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (email TEXT, artist TEXT)')
    cursor.execute('INSERT INTO users (email, artist) VALUES (?, ?)', (email, artist))
    conn.commit()
    conn.close()

def get_all_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT email, artist FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def store_price_history(artist, price, section):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS price_history (artist TEXT, price TEXT, section TEXT, date DATE)')
    cursor.execute('INSERT INTO price_history (artist, price, section, date) VALUES (?, ?, ?, date("now"))', (artist, price, section))
    conn.commit()
    conn.close()
