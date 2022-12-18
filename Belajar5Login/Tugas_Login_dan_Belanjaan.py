from datetime import date, datetime as dt

hari_ini = date.today()

now = dt.now()
time = now.strftime("%A, %d %B %Y %H:%M:%S.%f")

judul_program = "Program Kasir".center(60)
judul_login = "Halaman Login".center(60)
judul_data = "Daftar Barang".center(60)
judul_bayar = "Struk Pembayaran".center(60)
terimakasih = "Terima Kasih".center(60)
garis = "=".center(64,"=")

print(garis)
print("|",judul_program,"|")
print(garis,"\n")
print("|",judul_login,"|")
user_name = input("\n| Masukkan Username Anda : ")
if user_name.count(" ") > 0 : quit("Tidak Boleh Pakai Spasi")
password = input("| Masukkan Password Anda : ")
login_sukses = f"\nSelamat Datang {user_name},\nLast Login On \n{time}"


if user_name == "mahmud" and password=="1234" :
    print(login_sukses)

elif user_name != "mahmud" and password=="1234" : 
    print("username anda salah!!") 
    raise SystemExit()

elif user_name == "mahmud" and password!="1234" :
    print("password anda salah!!") 
    raise SystemExit()

else : 
    print("username & password salah!!!!") 
    raise SystemExit()
print(garis)
print(judul_program)
print(garis,"\n")
print("|",judul_data,"|")
print("\n| 1. Baju Branded \t: Rp 500.000,- \n")
print("| 2. Celana Branded \t: Rp 1.000.000,- \n")
print("| 3. Baju Lokal \t: Rp 100.000,- \n")
print("| 4. Celana Lokal \t: Rp 150.000,- \n")
print(garis)
nb = str(input("| Masukkan Nama Barang \t\t: "))
harga = int(input("| Masukkan Harga Barang\t\t: Rp "))
jb = int(input("| Masukkan Jumlah Barang \t: "))
total = f"| {nb} \t\t    {jb} \t\t\t{harga*jb}"

print(garis)
print("\n|", judul_bayar,"|\n")
print(f"Petugas \t: {user_name} \nTanggal \t: {time}\n")

print(f"| Nama Barang \t\t Jumlah \t\t Harga")
print(total)
print("\n")
print("| Total \t: Rp",harga*jb )
ju=int(input("| Jumlah Uang \t: Rp "))
print("| Kembalian \t: Rp",ju-(harga*jb))
print("\n\n",terimakasih)
print(garis)