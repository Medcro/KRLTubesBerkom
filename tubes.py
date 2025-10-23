<<<<<<< HEAD
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

print("Selamat datang di Access KAI")
akun = input("Apakah Anda sudah memiliki akun? 1. Iya 2. Tidak : ")

def login():
    print("Silahkan masuk ke akun Anda")
    email = input("Masukkan email Anda: ")
    pass = input("Masukkan password email Anda: ")

if akun == 1:
    login()
if akun == 2: 
    print("Buat akun Access KAI")
    print("Isi data diri Anda")
    nama     = input("Nama lengkap: ")
    nomor    = input("Nomor handphone: ")
    nik      = input("NIK KTP: ")
    gender   = input("Gender 1. Laki-laki 2. Perempuan: ")
    email    = input("Masukkan email Anda: ")
    print(f'Pembuatan akun selesai, Nama : {nama}, Nomor handphone: {nomor}, NIK : {nik}, Gender: {gender}, Email: {email}')
    valid = input("Apa data ini sudah valid? 1. Ya 2.Tidak: ")
    if valid == 1:
        print("Pembuatan akun selesai")
        login()

def login():
    print("Silahkan masuk ke akun Anda")
    email = input("Masukkan email Anda: ")
    pass = input("Masukkan password email Anda: ")
>>>>>>> origin/add_stasiun


decision = input("Apakah Anda ingin pesan tiket? 1. Ya 2. Tidak : ")
if decision == 1:
    asal = str(input("Stasiun asal: "))
    tujuan = str(input("Stasiun tujuan: "))
    tanggal = str(input("Tanggal keberangkatan (DD-MM-YYYY): "))
    input_data.input_tiket(asal, tujuan, tanggal)
    # ini perlu input jumlah penumpangnya ga ya
    '''
    asal    = input("Stasiun asal 1. Padalarang  2. Cimahi 3. Stasiun Bandung 4. Kiaracondong 5. Rancaekek : ")
    tujuan = input("Stasiun tujuan 1. Padalarang  2. Cimahi 3. Stasiun Bandung 4. Kiaracondong 5. Rancaekek : ")
    jam = input("Pilih jam keberangkatan 1. 05.00 - 07.30 2. 07.30-10.00 3. 10.00 - 12.30 4. 12.30 - 15.00 5. 15.00 - 17.30:")
    #ini perlu input jumlah penumpangnya ga ya

    if asal == 1:
        if tujuan == 1: 
            if jam == 1:
            elif jam == 2:
            elif jam == 3:
            elif jam == 4:
            elif jam == 5:
        if tujuan == 2:
            if jam == 1:
            elif jam == 2:
            elif jam == 3:
            elif jam == 4:
            elif jam == 5:
        if tujuan == 3: 
            #tampilkan harga, nama kereta, dan jam keberangkatan
        if tujuan == 4:
            #tampilkan harga, nama kereta, dan jam keberangkatan
        if tujuan == 5:
            #tampilkan harga, nama kereta, dan jam keberangkatan
        '''
# print(f'Tiket anda berhasil di order. Nama: {nama}, Tanggal keberangkatan: {tanggal}, Stasiun keberangkatan: {asal}, Stasiun tujuan: {tujuan}, Nama kereta')
# belum lengkap
        if jam == 1:
            elif jam == 2:
            elif jam == 3:
            elif jam == 4:
            elif jam == 5:
        if tujuan == 4: 
            if jam == 1:
            elif jam == 2:
            elif jam == 3:
            elif jam == 4:
            elif jam == 5:
        if tujuan == 5: 
            if jam == 1:
            elif jam == 2:
            elif jam == 3:
            elif jam == 4:
            elif jam == 5:

print(f'Tiket anda berhasil dipesan. Nama: {nama}, Tanggal keberangkatan: {tanggal}, Stasiun keberangkatan: {asal}, Stasiun tujuan: {tujuan}, Jam keberangkatan: {jam}')
#belum lengkap

if decision == 2:
    print("Sampai jumpa")
