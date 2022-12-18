from datetime import date, datetime as dt

hari_ini = date.today()

now = dt.now()
time = now.strftime("%A, %d %B %Y  %H:%M:%S.%f")

judul_login = "Halaman Login".center(30,"=")
judul_data = "Data Lahir".center(30,"=")
judul_preview = "Preview Data".center(30,"=")

print(judul_login)
user_name = input("\nMasukkan Username Anda : ")
if user_name.count(" ") > 0 : quit("Tidak Boleh Pakai Spasi!!!")
password = input("Masukkan Password Anda : ")
login_sukses = f"Selamat Datang {user_name}, \nLast Login on {time}\n"

if user_name == "tono" and password=="1234" : print(login_sukses)

elif user_name != "tono" and password=="1234" : quit("username anda salah!!")

elif user_name == "tono" and password!="1234" : quit("password anda salah!!")

else : quit("username & password salah!!!!")

print(judul_data)

tgl_lahir = int(input("\nMasukkan Tanggal Lahir Anda : "))
bln_lahir = int(input("Masukkan Bulan Lahir Anda : "))
thn_lahir = int(input("Masukkan Tahun Lahir Anda : "))

waktu_lahir = date(thn_lahir,bln_lahir,tgl_lahir)
time_born = waktu_lahir.strftime("%A, %d %B %Y")
usia_hari = hari_ini - waktu_lahir
usia_tahun = usia_hari.days // 365
usia_bulan = (usia_hari.days % 365) // 30
usia_sisahari = (usia_hari.days % 365) - (usia_bulan*30)

print(judul_preview)

print("\nTanggal Lahir Anda : ", time_born)
print(f"Usia Anda Adalah : {usia_tahun} tahun {usia_bulan} bulan {usia_sisahari} hari")