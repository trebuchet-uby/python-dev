pilih="y" or "n"
while pilih == "y" :
    print("""
        BING CHILLING ICE CREAM
    _______________________________
   | KODE |     RASA    |   HARGA  |
   |-------------------------------|
   |   1  | STRAWBERRY  | Rp.3500  |
   |   2  | VANILLA     | Rp.3000  |
   |   3  | SPARKLE GUM | Rp.5000  |
   |   4  | MIXED FRUIT | Rp.7500  |
   _________________________________
    """)
    pesan=input("Masukkan Kode Produk: ")
    jumlah=int(input("Masukan Jumlah pesanan: "))
    if pesan == "1" :
        nama = "STRAWBERRY ICE CREAM"
        harga = 3500
        total = jumlah * harga
    elif pesan == "2" :
        nama = "VANILLA ICE CREAM"
        harga = 3000
        total = jumlah * harga
    elif pesan == "3" :
        nama = "SPARKLE GUM ICE CREAM"
        harga = 5000
        total = jumlah * harga
    elif pesan == "4" :
        nama = "MIXED FRUIT ICE CREAM"
        harga = 3000
        total = jumlah * harga
    else : quit("PRODUK TIDAK DITEMUKAN")
    print("=====RINCIAN PESANAN=====")
    print(f"Produk: {nama}")
    print(f"Jumlah: {jumlah}")
    print(f"Total Bayar: {total}")
    bayar = int(input("Tunai: "))
    print(f"Kembalian: {bayar - total}")
    pilih = input("ingin melakukan transaksi lain?, ketik y untuk ya, ketik n untuk mengakhiri transaksi: ")
    while pilih == "n" : 
        quit("Terimakasih Telah Berkunjung")