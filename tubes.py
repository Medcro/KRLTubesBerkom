import component.input_data as input_data

# PROSES LOGIN
print("Selamat datang di Access KAI")
decision = input("Apakah Anda sudah memiliki akun? 1. Ya 2. Tidak : ")
if decision == "1":
    print("Silahkan login menggunakan akun email Anda")
    email = input("Masukkan email Anda: ")
    pass_email = input("Masukkan password Anda: ")
    input_data.input_login_data(email, pass_email)
elif decision == "2":
    print("Silahkan registrasi terlebih dahulu")
    email = input("Masukkan email Anda: ")
    pass_email = input("Masukkan password Anda: ")
    input_data.register_user(email, pass_email)

    # INPUT DATA DIRI
    print("Isi data diri Anda")
    nama = str(input("Nama lengkap: "))
    nomor = int(input("Nomor handphone: "))
    nik = int(input("NIK KTP: "))
    gender = str(input("Gender (L/P): "))
    input_data.input_user_data(nama, nomor, nik, gender)
else:
    print("Pilihan tidak valid. Silakan mulai ulang program.")
    exit()


decision = input("Apakah Anda ingin pesan tiket? 1. Ya 2. Tidak : ")
if decision == 1:
    asal = str(input("Stasiun asal: "))
    tujuan = str(input("Stasiun tujuan: "))
    tanggal = str(input("Tanggal keberangkatan (DD-MM-YYYY): "))
    input_data.input_tiket(asal, tujuan, tanggal)
    # ini perlu input jumlah penumpangnya ga ya
    '''
    if asal == 1:
        if tujuan == 1:
            #tampilkan harga, nama kereta, dan jam keberangkatan
        if tujuan == 2:
            #tampilkan harga, nama kereta, dan jam keberangkatan
        if tujuan == 3: 
            #tampilkan harga, nama kereta, dan jam keberangkatan
        if tujuan == 4:
            #tampilkan harga, nama kereta, dan jam keberangkatan
        if tujuan == 5:
            #tampilkan harga, nama kereta, dan jam keberangkatan
        '''
# print(f'Tiket anda berhasil di order. Nama: {nama}, Tanggal keberangkatan: {tanggal}, Stasiun keberangkatan: {asal}, Stasiun tujuan: {tujuan}, Nama kereta')
# belum lengkap

if decision == 2:
    print("Sampai jumpa")
