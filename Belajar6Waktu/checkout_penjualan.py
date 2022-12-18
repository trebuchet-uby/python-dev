from datetime import date, datetime as dt
login="Laman Login".center(30,"=")
data="Daftar Barang".center(30,"=")
preview="Laman Checkout".center(30,"=")
hari_ini=date.today()
now=dt.now()
time=now.strftime("%A, %d %B %Y %H:%M:%S.%f")

print(login)
username=input("\nMasukkan Username Anda: ")
if username.count(" ") > 0 : quit("Username Tidak Boleh Memakai Spasi")
password=input("\nMasukkan Password: ")
login_sukses=f"selamat Datang {username}"

if username == "dana" and password == "192168" : print(login_sukses)
elif username != "dana" and password == "192168" : quit("Username Salah")
elif username == "dana" and password != "192168" : quit("Password Salah")
else : quit("Username & Password salah")

print(data)
print("\nUser: ",username)
print("========Barang========|=====Harga=====")
print("1.Celana Jeans        |Rp.300.000     ")
print("2.Celana Olahraga     |Rp.125.000     ")
print("3.Jaket Hitam Polos   |Rp.200.000     ")
print("4.Kemeja Motif Kotak  |Rp. 87.000     ")
print("======================================")

barang=input("Masukkan Nama Barang: ")
harga=int(input("Masukkan Harga Barang: "))
jumlah=int(input("Masukkan Jumlah Barang: "))
total= harga*jumlah
print("\nTotal Pembayaran:Rp. ",total)
print("Tanggal Transaksi")
print(time)