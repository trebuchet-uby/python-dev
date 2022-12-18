from datetime import date, datetime as dt
hari_ini = date.today()

now = dt.now()
time = now.strftime("%A, %d %B %Y  %H:%M:%S.%f")


judul_login = "Silahkan Login".center(60,"~")

print(judul_login)
user_name = input("\nMasukan Username Anda : ")
if user_name.count(" ")>0 : quit("Tidak Boleh Pakai Spasi")
password = input("Masukkan Password Anda : ")
login_sukses = f"Welcome to Jinjjah Store {user_name}, \nLast Login on {time}\n"


if user_name =="Pritydita" and password =="13245":  print(login_sukses)

judul = "Daftar Skincare Yang Masih Ready".center(60,"*")
print(judul)

from prettytable import PrettyTable

table = PrettyTable(["Jenis Skincare","Harga"])

table.add_row(["Day Cream",30000])
table.add_row(["Night Cream",30000])
table.add_row(["Toner 30ml",27000])
table.add_row(["Serum 30ml",50000])
table.add_row(["Acne Gel",23000])

print(table)

judul = "Chek Out".center(60,"~")
print(judul)

pembeli = input("Nama Pembeli : ")
alamat = input("Alamat Pembeli : ")
nama_barang = input("Barang Yang Dibeli : ")
jumlah_barang =int(input("Jumlah Barang : "))
jumlah_harga =int(input("Harga Barang : "))
metode_pembayaran = input("Metode Pembayaran : ")
ongkos_kirim =int(input("Ongkir : "))


judul = "Konfirmasi Ulang Pembelian".center(60,"#")
print(judul)
print("--------------------------------------------------------")

print("Nama               : ", pembeli)
print("Alamat Yang Dituju : ", alamat)
print("----------------------------------------------------------")


print("Nama Barang                    : ", nama_barang)
print("Subtotal Item                  : ", jumlah_barang)
print("Harga Barang                   : ", jumlah_harga)
print("Metode Pembayaran              : ", metode_pembayaran)
print("Ongkos Kirim                   : ",ongkos_kirim)
print("Keseluruhan Harga Yang Dibayar : Rp.", jumlah_barang*jumlah_harga + ongkos_kirim)
print("--------------------------------------------------------------")
print("Siapkan Uang yang pas guna melakukan pembayaran")




