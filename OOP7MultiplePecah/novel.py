class Novel:
    def harga_novel(self):
        print("1. Harga Novel Aku          : Rp. 50.000")
        print("2. Harga Novel LP           : Rp. 65.000")
        print("3. Harga Novel SAO          : Rp. 70.000\n")

    def pembelian_novel(self):
        pilihan = input("Masukkan pilihan buku anda : ")
        jumlah = int(input("Masukkan jumlah pembelian : "))

        if pilihan == "1":
            harga = jumlah * 50000
            print(f"Anda membeli {jumlah} Novel Aku \n" +
                f"dengan total harga {harga}")
        elif pilihan == "2":
            harga = jumlah * 65000
            print(f"Anda membeli {jumlah} Novel LP \n" +
                f"dengan total harga {harga}")
        elif pilihan == "3":
            harga = jumlah * 70000
            print(f"Anda membeli {jumlah} Novel SAO \n" +
               f"dengan total harga {harga}")
        else:
            quit("Input Salah !!!")