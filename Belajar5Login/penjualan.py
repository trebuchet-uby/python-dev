from datetime import date, datetime as dt
hari_ini=date.today()
now=dt.now()
time=now.strftime("%d %B %Y  %H:%M:%S:%f")
hal_LOGIN="HALAMAN LOGIN".center(40,"=")
hal_HOST="HALAMAN TRANSAKSI".center(40,"=")
hal_HIST="HALAMAN HISTORI".center(40,"=")
print(hal_LOGIN)
username=input("masukkan USERNAME anda  :")
if username.count(" ")>0:quit("Jangan pakai spasi")
password=input("masukkan password anda  :")
login_sukses=f"SELAMAT DATANG {username}, anda masuk pada {time}"
if username=="abdul" and password=="12345":print(login_sukses)
elif username!="abdul" and password=="12345":quit("username salah????")
elif username=="abdul" and password!="12345":quit("password salah????")
else :print("username dan password salah???")
print(hal_HOST)
print("TOKO BUKU AR RAHMAN")
print(time)
print("")
print("akun :",username)
print("-------------------------------------")
print("1.KISAH WALI SONGO  Rp.70000")
print("2.PERJUANGAN KIAS   Rp.60000")
print("3.SIRAH NABAWIYAH   Rp.100000")
print("______________________________________")
buku=input("silahkan masukan nama buku :")
harga=int(input("silahkan masukkan harga:"))
jumlah=int(input("silahkan masukkan jumlah:"))
total=harga*jumlah
print("TOTAL   :Rp.",total)
uang=int(input("masukkan nominal  :"))
kembali=uang-total
print("kembali :Rp.",kembali)
print(hal_HIST)
print(username)
print(f"telah membeli buku {buku} sebanyak {jumlah} buah dengan harga Rp.{harga}.dengan total {total}. pada {time}")