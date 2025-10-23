import databases.databases as databases


def register_user(email, password):
    databases.init_login_db()
    databases.register_user(email, password)


def input_login_data(email, password):
    databases.init_login_db()
    return databases.login_user(email, password)


def input_user_data(nama, nomor, nik, gender):
    databases.init_data_diri_db()
    databases.add_user(nama, nomor, nik, gender)


def input_kereta(asal, tujuan, jam_keberangkatan):
    return databases.book_ticket(asal, tujuan, jam_keberangkatan)


def pesan_tiket():
    databases.init_train_db()


def input_kereta(asal, tujuan, jam_keberangkatan, user_name):
    return databases.book_ticket(asal, tujuan, jam_keberangkatan, user_name)


def get_user_by_email(email):
    return databases.get_user_by_email(email)
