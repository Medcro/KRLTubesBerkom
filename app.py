import databases.databases as databases

# Membuat tabel data di databases
databases.init_login_db()
databases.init_data_diri_db()
databases.init_train_db()

# PROSES LOGIN
while True:
    print("====================================================")
    print("            Selamat datang di Access KAI            ")
    print("====================================================\n")
    decision = input(
        "Apakah Anda sudah memiliki akun? \n1. Ya \n2. Tidak \nMasukkan pilihan Anda: ")
    nama = None

    if decision == "1":
        print("\nSilahkan login menggunakan akun email Anda")
        email = input("\nMasukkan email Anda: ")
        password = input("Masukkan password Anda: ")
        if databases.login_user(email, password):
            user_data = databases.get_user_by_email(email)
            nama = user_data[0]
            print(f"\nSelamat datang kembali, {nama}!")
        else:
            continue

    elif decision == "2":
        print("\nSilahkan registrasi terlebih dahulu")
        email = input("\nMasukkan email Anda: ")
        password = input("Masukkan password Anda: ")
        if databases.register_user(email, password):
            print("\nIsi data diri Anda")
            nama = str(input("\nNama lengkap: "))
            nomor = int(input("Nomor handphone: "))
            nik = int(input("NIK KTP: "))
            gender = str(input("Gender (L/P): "))
            databases.add_user(nama, nomor, nik, gender)
        else:
            print("\nRegistrasi gagal. Silakan coba lagi.")
            continue

    else:
        print("\nPilihan tidak valid. Silakan coba lagi.")
        continue

    break


# PESAN TIKET
while True:
    station_map = {'1': "Padalarang", '2': "Cimahi",
                   '3': "Stasiun Bandung", '4': "Kiaracondong", '5': "Rancaekek"}

    decision = input(
        "\nApakah Anda ingin pesan tiket? \n1. Ya \n2. Tidak\nMasukkan pilihan Anda: ")
    if decision == '1':
        asal = input(
            "\nStasiun asal: \n1. Padalarang  \n2. Cimahi \n3. Stasiun Bandung \n4. Kiaracondong \n5. Rancaekek \nPilih stasiun asal Anda: ")
        asal = station_map.get(asal)
        if not asal:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            continue

        tujuan = input(
            "\nStasiun tujuan: \n1. Padalarang  \n2. Cimahi \n3. Stasiun Bandung \n4. Kiaracondong \n5. Rancaekek \nPilih stasiun tujuan Anda: ")
        tujuan = station_map.get(tujuan)
        if not tujuan:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            continue

        if asal == tujuan:
            print("\nStasiun asal dan tujuan tidak boleh sama. Silakan coba lagi.")
            continue

        jam = input(
            "\nJam keberangkatan: \n1. 05.00 - 07.30 \n2. 07.30-10.00 \n3. 10.00 - 12.30 \n4. 12.30 - 15.00 \n5. 15.00 - 17.30 \nPilih jam keberangkatan Anda: ")

        time_map = {'1': "05.00 - 07.30", '2': "07.30 - 10.00",
                    '3': "10.00 - 12.30", '4': "12.30 - 15.00", '5': "15.00 - 17.30"}

        jam = time_map.get(jam)
        if not jam:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            continue

        databases.book_ticket(asal, tujuan, jam, nama)
        print("\n\n====================================================")
        print("     Terimakasih sudah menggunakan layanan kami     ")
        print("====================================================\n\n")
        break

    elif decision == '2':
        print("\n\n====================================================")
        print("                Sampai jumpa kembali                ")
        print("====================================================\n\n")
        break
    else:
        print("\nPilihan tidak valid. Silakan coba lagi.")
