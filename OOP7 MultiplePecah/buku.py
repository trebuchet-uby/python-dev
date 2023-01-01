class Buku:
    def harga_buku(self):
        print("1. Harga Buku PBO           : Rp. 70.000")
        print("2. Harga Buku Resep         : Rp. 40.000")
        print("3. Harga Buku Sejarah       : Rp. 50.000\n")

    def pembelian_buku(self):
        pilihan = input("Masukkan pilihan buku anda : ")
        jumlah = int(input("Masukkan jumlah pembelian : "))

        if pilihan == "1":
            harga = jumlah * 70000
            print(f"Anda membeli {jumlah} Buku PBO \n" +
                f"dengan total harga {harga}")
        elif pilihan == "2":
            harga = jumlah * 40000
            print(f"Anda membeli {jumlah} Buku Resep \n" +
                f"dengan total harga {harga}")
        elif pilihan == "3":
            harga = jumlah * 50000
            print(f"Anda membeli {jumlah} Buku Sejarah \n" +
               f"dengan total harga {harga}")
        else:
            quit("Input Salah !!!")
