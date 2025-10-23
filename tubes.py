# PROSES LOGIN
print("Selamat datang di Access KAI")
print("Silahkan login menggunakan akun email Anda")
email = input("Masukkan email Anda: ")
pass_email = input("Masukkan password Anda: ")

print("Isi data diri Anda")
nama     = input("Nama lengkap: ")
nomor    = input("Nomor handphone: ")
nik      = input("NIK KTP: ")
gender   = input("Gender 1. Laki-laki 2. Perempuan: ")


decision = input("Apakah Anda ingin pesan tiket? 1. Ya 2. Tidak : ")
if decision == 1:
    asal    = input("Stasiun asal 1. 2. 3. 4. 5. : ")
    tujuan = input("Stasiun tujuan 1. 2. 3. 4. 5. : ")
    tanggal = input("Tanggal keberangkatan: ")
    #ini perlu input jumlah penumpangnya ga ya
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
print(f'Tiket anda berhasil di order. Nama: {nama}, Tanggal keberangkatan: {tanggal}, Stasiun keberangkatan: {asal}, Stasiun tujuan: {tujuan}, Nama kereta')
#belum lengkap

if decision == 2:
    print("Sampai jumpa")
