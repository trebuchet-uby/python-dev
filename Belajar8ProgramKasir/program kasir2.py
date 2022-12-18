print("MENU".center(60,"="))
tanda = ("".center(30,"="))
from prettytable import PrettyTable
table = PrettyTable(["Paket Makanan","Makanan"])
table.add_row(["Paket 1","Nasi goreng seafood + Es teh"])
table.add_row(["Paket 2","Cumi goreng tepung + Es teh + nasi"])
table.add_row(["Paket 3","Steak ayam + Nasi + Es Teh"])
print(table)

from prettytable import PrettyTable
table = PrettyTable(["No","Minuman"])
table.add_row(["1","Es teh"])
table.add_row(["2","Es jeruk "])
table.add_row(["3","Teh anget"])
table.add_row(["4","Jeruk anget"])
print(table)
print("Harga Perpaket".center(30,"="))
harga = ["15k","20k","25k"]
Paket = 0
for i in harga:
     Paket +=1
     print(f"Paket {Paket}dengan harga {i}")

print("Harga Minuman".center(30,"="))
harga = ["3k","4k","5k","6k"]
minuman = 0
for a in harga:
     minuman +=1
     print(f"Nomor {minuman}dengan harga {a}")
nama = input("Masukkan Nama : ")
print(f"\nMasukkan pesanan anda\n\n1.Ketik paket jika ingin memesan\n2.Ketik minuman jika ingin membeli minuman\n")
Opsi = input("Paket/minuman? : ")
if Opsi=="Paket":
     Pesanan = int(input("Masukkan paket pilihan anda : "))
     Jumlah =int(input("Masukkan jumlah pesanan : "))
     if Pesanan ==1:
          print(f"\n{tanda}\nNama:{nama}\n{tanda}\nPaket 1:Nasi goreng seafood + es teh\nHarga:Rp.15.000,00\nTotal PembayaranRp.{Jumlah*15000},00\n{tanda}\n")
     elif Pesanan ==2:
      print(f"\n{tanda}\nNama:{nama}\n{tanda}\n Paket 2:Cumi goreng tepung + es teh + nasi\nHarga:Rp.20.000,00\nTotal Pembayaran:Rp.{Jumlah*20000},00\n{tanda}\n")
     elif Pesanan ==3:
      print(f"\n{tanda}\nNama:{nama}\n{tanda}\n Paket 3:steak ayam + nasi + es teh\nHarga:Rp.25.000,00\nTotal Pembayaran:Rp.{Jumlah*25000},00\n{tanda}\n")
     else:print("Menu yang anda sebutkan tidak ada dalam daftar menu")
if Opsi=="minuman":
     Pesanan =int(input("Masukkan jumlah pesanan anda : "))
     if Pesanan ==1:
          print(f"\n{tanda}\nNama{nama}\n{tanda}\nMinuman 1:Es Teh\nHarga:Rp.3.000,00\nTotal Pemabayaran:Rp.{Jumlah*3000},00\n{tanda}\n")
     elif Pesanan ==2:
          print(f"\n{tanda}\nNama{nama}\n{tanda}\nMinuman 1:Es Jeruk\nHarga:Rp.4.000,00\nTotal Pemabayaran:Rp.{Jumlah*4000},00\n{tanda}\n")
     elif Pesanan ==3:
          print(f"\n{tanda}\nNama{nama}\n{tanda}\nMinuman 1:Teh Hangan\nHarga:Rp.5.000,00\nTotal Pemabayaran:Rp.{Jumlah*5000},00\n{tanda}\n")
     elif Pesanan ==4:
          print(f"\n{tanda}\nNama{nama}\n{tanda}\nMinuman 1:Jeruk Hangat\nHarga:Rp.6.000,00\nTotal Pemabayaran:Rp.{Jumlah*6000},00\n{tanda}\n")
     else:print("Menu yang anda sebutkan tidak ada dalam daftar menu")
print(f"\n1.Ketik Paket Jika Ingin Memesan Makanan Lagi\n2.Ketik Minuman Jika Ingin Membeli Minuman Lagi\n3.Ketik selesai jika sudah selesai memesan\n")
Opsi = input("Paket/minuman/selesai:")
if Opsi =="Paket":
     Pesanan = int(input("Masukkan paket pilihan anda : "))
     Jumlah =int(input("Masukkan jumlah pesanan : "))
     if Pesanan ==1:
          print(f"\n{tanda}\nNama:{nama}\n{tanda}\nPaket 1:Nasi goreng seafood + es teh\nHarga:Rp.15.000,00\nTotal PembayaranRp.{Jumlah*15000},00\n{tanda}\n")
     elif Pesanan ==2:
      print(f"\n{tanda}\nNama:{nama}\n{tanda}\n Paket 2:Cumi goreng tepung + es teh + nasi\nHarga:Rp.20.000,00\nTotal Pembayaran:Rp.{Jumlah*20000},00\n{tanda}\n")
     elif Pesanan ==3:
      print(f"\n{tanda}\nNama:{nama}\n{tanda}\n Paket 3:steak ayam + nasi + es teh\nHarga:Rp.25.000,00\nTotal Pembayaran:Rp.{Jumlah*25000},00\n{tanda}\n")
     else:print("Menu yang anda sebutkan tidak ada dalam daftar menu")
if Opsi=="minuman":
     Pesanan =int(input("Masukkan jumlah pesanan anda : "))
     if Pesanan ==1:
          print(f"\n{tanda}\nNama{nama}\n{tanda}\nMinuman 1:Es Teh\nHarga:Rp.3.000,00\nTotal Pemabayaran:Rp.{Jumlah*3000},00\n{tanda}\n")
     elif Pesanan ==2:
          print(f"\n{tanda}\nNama{nama}\n{tanda}\nMinuman 1:Es Jeruk\nHarga:Rp.4.000,00\nTotal Pemabayaran:Rp.{Jumlah*4000},00\n{tanda}\n")
     elif Pesanan ==3:
          print(f"\n{tanda}\nNama{nama}\n{tanda}\nMinuman 1:Teh Hangan\nHarga:Rp.5.000,00\nTotal Pemabayaran:Rp.{Jumlah*5000},00\n{tanda}\n")
     elif Pesanan ==4:
          print(f"\n{tanda}\nNama{nama}\n{tanda}\nMinuman 1:Jeruk Hangat\nHarga:Rp.6.000,00\nTotal Pemabayaran:Rp.{Jumlah*6000},00\n{tanda}\n")
     else:print("Menu yang anda sebutkan tidak ada dalam daftar menu")
if Opsi=="selesai":quit











