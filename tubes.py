import component.input_data as input_data

# PROSES LOGIN
while True:
    print("Selamat datang di Access KAI")
    decision = input("Apakah Anda sudah memiliki akun? 1. Ya 2. Tidak : ")
    nama = None

    if decision == "1":
        print("Silahkan login menggunakan akun email Anda")
        email = input("Masukkan email Anda: ")
        pass_email = input("Masukkan password Anda: ")
        if input_data.input_login_data(email, pass_email):
            user_data = input_data.get_user_by_email(email)
            if user_data:
                nama = user_data[0]
                print(f"Selamat datang kembali, {nama}!")
            else:
                print("Data diri tidak ditemukan. Silakan lengkapi data diri Anda.")
                nama_input = input("Nama lengkap: ")
                nomor = int(input("Nomor handphone: "))
                nik = int(input("NIK KTP: "))
                gender = str(input("Gender (L/P): "))
                input_data.input_user_data(nama_input, nomor, nik, gender)
                nama = nama_input
        else:
            continue

    elif decision == "2":
        print("Silahkan registrasi terlebih dahulu")
        email = input("Masukkan email Anda: ")
        pass_email = input("Masukkan password Anda: ")
        if input_data.register_user(email, pass_email):
            print("Isi data diri Anda")
            nama = str(input("Nama lengkap: "))
            nomor = int(input("Nomor handphone: "))
            nik = int(input("NIK KTP: "))
            gender = str(input("Gender (L/P): "))
            input_data.input_user_data(nama, nomor, nik, gender)
        else:
            print("Registrasi gagal. Silakan coba lagi.")
            continue

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        continue

    break

# PESAN TIKET
input_data.pesan_tiket()
while True:
    decision = input("Apakah Anda ingin pesan tiket? 1. Ya 2. Tidak : ")
    if decision == '1':
        asal = input(
            "Stasiun asal 1. Padalarang  2. Cimahi 3. Stasiun Bandung 4. Kiaracondong 5. Rancaekek : ")
        tujuan = input(
            "Stasiun tujuan 1. Padalarang  2. Cimahi 3. Stasiun Bandung 4. Kiaracondong 5. Rancaekek : ")
        jam = input(
            "Pilih jam keberangkatan 1. 05.00 - 07.30 2. 07.30-10.00 3. 10.00 - 12.30 4. 12.30 - 15.00 5. 15.00 - 17.30:")

        if asal == tujuan:
            print("Stasiun asal dan tujuan tidak boleh sama. Silakan coba lagi.")
            continue

        station_map = {'1': "Padalarang", '2': "Cimahi",
                       '3': "Stasiun Bandung", '4': "Kiaracondong", '5': "Rancaekek"}
        asal = station_map.get(asal)
        tujuan = station_map.get(tujuan)
        if not asal or not tujuan:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        time_map = {'1': "05.00 - 07.30", '2': "07.30 - 10.00",
                    '3': "10.00 - 12.30", '4': "12.30 - 15.00", '5': "15.00 - 17.30"}
        jam = time_map.get(jam)
        if not jam:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        if input_data.input_kereta(asal, tujuan, jam, nama):
            break
    elif decision == '2':
        print("Sampai jumpa")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
