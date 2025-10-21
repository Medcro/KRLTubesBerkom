import databases

databases.create_table_if_not_exists()

first_name = str(input("Masukkan nama depan Anda: "))
last_name = str(input("Masukkan nama belakang Anda: "))
age = int(input("Masukkan umur Anda: "))
databases.add_user(first_name, last_name, age)

users = databases.get_all_users()
print("\nData Diri yang Tersimpan:")
for user in users:
    print(f"Nama Depan: {user[1]}, Nama Belakang: {user[2]}, Umur: {user[3]}")
