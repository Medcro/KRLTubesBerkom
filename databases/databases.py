import sqlite3


def create_table_if_not_exists():
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        nomor INTEGER NOT NULL,
        NIK INTEGER NOT NULL,
        gender CHAR(1) NOT NULL
        
    )
    ''')
    conn.commit()
    conn.close()

def create_login_table_if_not_exists():
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS loginInfo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def register_user(email, password):
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO loginInfo (email, password) VALUES (?, ?)",
                   (email, password))
        print("Registrasi berhasil!")
    except: 
        print("Email sudah terdaftar. Silakan gunakan email lain.")
        exit()
    conn.commit()
    conn.close()

def login_user(email, password):
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM loginInfo WHERE email = ? AND password = ?",
                   (email, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Login berhasil!")
        return True
    else:
        print("Email atau password salah.")
        exit()
        return False

def add_user(nama, nomor, NIK, gender):
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (nama, nomor, NIK, gender) VALUES (?, ?, ?, ?)",
                   (nama, nomor, NIK, gender))
    conn.commit()
    conn.close()


def add_tiket(asal, tujuan, tanggal):
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tiket (asal, tujuan, tanggal, nama_kereta) VALUES (?, ?, ?, ?)",
                   (asal, tujuan, tanggal))
    conn.commit()
    conn.close()


def get_all_users():
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users
 
