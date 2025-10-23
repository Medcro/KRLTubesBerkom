import databases.databases as databases

def register_user(email, password):
    databases.create_login_table_if_not_exists()
    databases.register_user(email, password)

def input_login_data(email, password):
    databases.create_login_table_if_not_exists()
    databases.login_user(email, password)

def input_user_data(nama, nomor, nik, gender):
    databases.create_table_if_not_exists()
    databases.add_user(nama, nomor, nik, gender)

    users = databases.get_all_users()
    print("\nData Diri yang Tersimpan:")
    # for user in users:
    # print(
    # f'Tiket anda berhasil di order. Nama: {user[1]}, Tanggal keberangkatan: {user[2]}, Stasiun keberangkatan: {user[3]}, Stasiun tujuan: {user[4]}, Nama kereta: {user[5]}')


def input_tiket(ASAL, TUJUAN, TANGGAL):
    asal = ASAL
    tujuan = TUJUAN
    tanggal = TANGGAL
    databases.add_tiket(asal, tujuan, tanggal)
