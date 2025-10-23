import sqlite3


def init_data_diri_db():
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


def init_login_db():
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


def init_train_db():
    conn = sqlite3.connect('data_kereta.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kereta_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asal TEXT NOT NULL,
        tujuan TEXT NOT NULL,
        jam_keberangkatan TEXT NOT NULL,
        kapasitas INTEGER NOT NULL
    )
    ''')


def register_user(email, password):
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM loginInfo WHERE email = ?", (email,))
        if cursor.fetchone():
            print("Email sudah terdaftar. Silakan gunakan email lain.")
            return False 

        cursor.execute(
            "INSERT INTO loginInfo (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        print("Registrasi berhasil!")
        return True 
    except Exception as e:
        print(f"Error during registration: {e}")
        return False 
    finally:
        conn.close()


def login_user(email, password):
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM loginInfo WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Login berhasil!")
        return True
    else:
        print("Email atau password salah.")
        return False


def add_user(nama, nomor, NIK, gender):
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (nama, nomor, NIK, gender) VALUES (?, ?, ?, ?)", (nama, nomor, NIK, gender))
    conn.commit()
    conn.close()


def get_all_users():
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def book_ticket(asal, tujuan, jam_keberangkatan, user_name):
    conn = sqlite3.connect('data_kereta.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, kapasitas FROM kereta_info WHERE asal = ? AND tujuan = ? AND jam_keberangkatan = ?",
                       (asal, tujuan, jam_keberangkatan))
        row = cursor.fetchone()

        if row:
            train_id, current_kapasitas = row
            if current_kapasitas > 0:
                new_kapasitas = current_kapasitas - 1
                cursor.execute(
                    "UPDATE kereta_info SET kapasitas = ? WHERE id = ?", (new_kapasitas, train_id))
                conn.commit()
                print(
                    f'Tiket berhasil dipesan untuk {user_name}. Asal: {asal}, Tujuan: {tujuan}, Jam Keberangkatan: {jam_keberangkatan}, Kapasitas Tersisa: {new_kapasitas}')
                return True
            else:
                print("Kapasitas penuh. Tidak dapat memesan tiket.")
                return False
        else:
            initial_kapasitas = 100
            cursor.execute("INSERT INTO kereta_info (asal, tujuan, jam_keberangkatan, kapasitas) VALUES (?, ?, ?, ?)",
                           (asal, tujuan, jam_keberangkatan, initial_kapasitas))
            conn.commit()
            new_kapasitas = initial_kapasitas - 1
            cursor.execute("UPDATE kereta_info SET kapasitas = ? WHERE asal = ? AND tujuan = ? AND jam_keberangkatan = ?",
                           (new_kapasitas, asal, tujuan, jam_keberangkatan))
            conn.commit()
            print(
                f'Tiket berhasil dipesan untuk {user_name}. Asal: {asal}, Tujuan: {tujuan}, Jam Keberangkatan: {jam_keberangkatan}, Kapasitas Tersisa: {new_kapasitas}')
            return True
    except Exception as e:
        print(f"Error during booking: {e}")
        return False
    finally:
        conn.close()


def get_user_by_email(email):
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nama, nomor, NIK, gender FROM users WHERE id = (SELECT id FROM loginInfo WHERE email = ?)", (email,))
    user = cursor.fetchone()
    conn.close()
    return user


def add_tiket(asal, tujuan, tanggal):
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tiket (asal, tujuan, tanggal, nama_kereta) VALUES (?, ?, ?, ?)",
                   (asal, tujuan, tanggal))
    conn.commit()
    conn.close()
