# PR
# BISA TRANSAKSI BERKALI-KALI
# ANDHI PRASETYO (C20010004)

class Toko:
    def __init__(self, inputJudul, inputJenis):
        self.judul = inputJudul
        self.jenis = inputJenis
    
    def judul_program(self):
        print("\n")
        print(" Toko Buku ".center(30,"=")+("\n"))

        print("1. Komik")
        print("2. Novel")
        print("3. Majalah\n")

        print(30*"=")

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



class Pembelian(Toko, Komik, Novel, Buku):
    def beli(self):
        if self.jenis == "1":
            self.harga_komik()
            self.pembelian_komik()
        elif self.jenis == "2":
            self.harga_novel()
            self.pembelian_komik()
        elif self.jenis == "3":
            self.harga_buku()
            self.pembelian_buku()
        else:
            quit("Input Salah !!!")

pembelian1 = Pembelian(Toko.judul_program(self=Toko),
    input("Masukkan jenis buku yang akan dibeli : ")
)

print("\n")
pembelian1.beli()
print("Transaksi Selesai")
print("\n")

while True:
    jawab = input("Belanja Lagi??? ( Y / N ):  ")
    if (jawab == "Y" or jawab == "y"):
        pembelian1 = Pembelian(Toko.judul_program(self=Toko),
        input("Masukkan jenis buku yang akan dibeli : ")
        )

        print("\n")
        pembelian1.beli()
        print("Transaksi Selesai")
        print("\n")


    else:
        quit(f"Terima Kasih Sudah Berbelanja\n" +
            f"PROGRAM SELESAI"
        )

