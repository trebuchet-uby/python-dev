from datetime import date, datetime as dt

hari_ini = date.today()

now = dt.now()
time =now.strftime("%A,\n %d %B %Y %H:%M:%S.%f")
print("MENU".center(60,"="))
tanda = ("".center(60,"-"))
print ('''
----------------------------------------------------
     |  Paket   |            Isi            |
----------------------------------------------------
     |  Paket 1 | Nasi + paha atas + es teh |
     |  Paket 2 | Nasi + paha bawah + es teh|
     |  Paket 3 |    Nasi + dada + es teh   |
     |  Paket 4 |      Burger + Es Milo     |
     |  Paket 5 |   Steak Ayam + Es Milo    |
----------------------------------------------------
''')
print ('''
----------------------------------------------------
     |  Nomor   |           Minuman         |
----------------------------------------------------
     |     1    |            Es Teh         |
     |     2    |           Es Jeruk        |
     |     3    |            Es Milo        |
     |     4    |           Good Day        |
     |     5    |           Lemon Tea       |
----------------------------------------------------
''')
print("Harga Perpaket".center(30,"="))
harga = ["11k","10k","13k","17k","20k"]
Paket = 0
for i in harga :
    Paket += 1
    print(f"Paket {Paket} dengan harga {i}")

print("Harga Minuman".center(30,"="))
harga1 = ["3k","3k","5k","4k","5k"]
minuman = 0
for a in harga1 :
    minuman += 1
    print(f"Nomor {minuman} dengan harga {a}")
nama = input("Masukan Nama: ")
print(f"\nMau pesan apa?\n\n1. Ketik Paket Jika Ingin Memesan Paket\n2. Ketik minuman Jika Ingin Membeli minuman\n")
Opsi = input("Paket/minuman? : ")
if Opsi == "Paket" :
     Pesanan = int(input("Masukan Nomor Paket Pilihan Anda: "))
     Jumlah = int(input("Masukan Jumlah Pesanan Anda: "))
     if Pesanan == 1 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nPaket 1 : Nasi + Paha Atas + Es Teh\nHarga : Rp.11.000,00\nTotal Pembayaran : Rp. {Jumlah*11000},00\n{tanda}\n{time}\n")
     elif Pesanan == 2 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nPaket 2 : Nasi + Paha Bawah + Es Teh\nHarga : Rp.10.000,00\nTotal Pembayaran : Rp. {Jumlah*10000},00\n{tanda}\n{time}\n")
     elif Pesanan == 3 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nPaket 3 : Nasi + Dada + Es Teh\nHarga : Rp.13.000,00\nTotal Pembayaran : Rp. {Jumlah*13000},00\n{tanda}\n{time}\n")
     elif Pesanan == 4 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nPaket 4 : Burger + Es Milo\nHarga : Rp.17.000,00\nTotal Pembayaran : Rp. {Jumlah*17000},00\n{tanda}\n{time}\n")
     elif Pesanan == 5 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nPaket 5 : Steak Ayam + Es Milo\nHarga : Rp.20.000,00\nTotal Pembayaran : Rp. {Jumlah*20000},00\n{tanda}\n{time}\n")
     else: print("Maaf pesanan mu tidak ada di daftar menu")
if Opsi == "minuman" :
     Pesanan = int(input("Masukan Nomor Paket Pilihan Anda: "))
     Jumlah = int(input("Masukan Jumlah Pesanan Anda: "))
     if Pesanan == 1 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nMinuman 1 : Es Teh\nHarga : Rp.3.000,00\nTotal Pembayaran : Rp. {Jumlah*3000},00\n{tanda}\n{time}\n")
     elif Pesanan == 2 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nMinuman 2 : Es Jeruk\nHarga : Rp.3.000,00\nTotal Pembayaran : Rp. {Jumlah*3000},00\n{tanda}\n{time}\n")
     elif Pesanan == 3 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nMinuman 3 : Es Milo\nHarga : Rp.5.000,00\nTotal Pembayaran : Rp. {Jumlah*5000},00\n{tanda}\n{time}\n")
     elif Pesanan == 4 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nMinuman 4 : Good Day\nHarga : Rp.4.000,00\nTotal Pembayaran : Rp. {Jumlah*4000},00\n{tanda}\n{time}\n")
     elif Pesanan == 5 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nMinuman 5 : Lemon Tea\nHarga : Rp.5.000,00\nTotal Pembayaran : Rp. {Jumlah*5000},00\n{tanda}\n{time}\n")
     else: print("Maaf pesanan mu tidak ada di daftar menu")
print(f"\n1. Ketik Paket Jika Ingin Memesan Paket lagi\n2. Ketik minuman Jika Ingin Membeli minuman lagi\n3. Ketik selesai jika sudah selesai memesan\n")
Opsi = input("Paket/minuman/selesai: ")
if Opsi == "Paket" :
     Pesanan = int(input("Masukan Nomor Paket Pilihan Anda: "))
     Jumlah = int(input("Masukan Jumlah Pesanan Anda: "))
     if Pesanan == 1 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nPaket 1 : Nasi + Paha Atas + Es Teh\nHarga : Rp.11.000,00\nTotal Pembayaran : Rp. {Jumlah*11000},00\n{tanda}\n{time}\n")
     elif Pesanan == 2 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nPaket 2 : Nasi + Paha Bawah + Es Teh\nHarga : Rp.10.000,00\nTotal Pembayaran : Rp. {Jumlah*10000},00\n{tanda}\n{time}\n")
     elif Pesanan == 3 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nPaket 3 : Nasi + Dada + Es Teh\nHarga : Rp.13.000,00\nTotal Pembayaran : Rp. {Jumlah*13000},00\n{tanda}\n{time}\n")
     elif Pesanan == 4 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nPaket 4 : Burger + Es Milo\nHarga : Rp.17.000,00\nTotal Pembayaran : Rp. {Jumlah*17000},00\n{tanda}\n{time}\n")
     elif Pesanan == 5 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nPaket 5 : Steak Ayam + Es Milo\nHarga : Rp.20.000,00\nTotal Pembayaran : Rp. {Jumlah*20000},00\n{tanda}\n{time}\n")
     else: print("Maaf pesanan mu tidak ada di daftar menu")
if Opsi == "minuman" :
     Pesanan = int(input("Masukan Nomor Paket Pilihan Anda: "))
     Jumlah = int(input("Masukan Jumlah Pesanan Anda: "))
     if Pesanan == 1 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nMinuman 1 : Es Teh\nHarga : Rp.3.000,00\nTotal Pembayaran : Rp. {Jumlah*3000},00\n{tanda}\n{time}\n")
     elif Pesanan == 2 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nMinuman 2 : Es Jeruk\nHarga : Rp.3.000,00\nTotal Pembayaran : Rp. {Jumlah*3000},00\n{tanda}\n{time}\n")
     elif Pesanan == 3 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nMinuman 3 : Es Milo\nHarga : Rp.5.000,00\nTotal Pembayaran : Rp. {Jumlah*5000},00\n{tanda}\n{time}\n")
     elif Pesanan == 4 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nMinuman 4 : Good Day\nHarga : Rp.4.000,00\nTotal Pembayaran : Rp. {Jumlah*4000},00\n{tanda}\n{time}\n")
     elif Pesanan == 5 :
          print(f"\n{tanda}\nNama : {nama}\n{tanda}\nMinuman 5 : Lemon Tea\nHarga : Rp.5.000,00\nTotal Pembayaran : Rp. {Jumlah*5000},00\n{tanda}\n{time}\n")
     else: print("Maaf pesanan mu tidak ada di daftar menu")
if Opsi == "selesai" : quit