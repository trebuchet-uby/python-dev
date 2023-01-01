class Komik:
    def harga_komik(self):
        print("1. Harga Komik Naruto       : Rp. 30.000")
        print("2. Harga Komik Doraemon     : Rp. 25.000")
        print("3. Harga Komik Conan        : Rp. 20.000\n")
    
    def pembelian_komik(self):
        pilihan = input("Masukkan pilihan buku anda : ")
        jumlah = int(input("Masukkan jumlah pembelian : "))

        if pilihan == "1":
            harga = jumlah * 30000
            print(f"Anda membeli {jumlah} Komik Naruto \n" +
                f"dengan total harga {harga}")
        elif pilihan == "2":
            harga = jumlah * 25000
            print(f"Anda membeli {jumlah} Komik Doraemon \n" +
                f"dengan total harga {harga}")
        elif pilihan == "3":
            harga = jumlah * 20000
            print(f"Anda membeli {jumlah} Komik Conan \n" +
               f"dengan total harga {harga}")
        else:
            quit("Input Salah !!!")