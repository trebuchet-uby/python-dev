# Tugas : Toko
# Turunannya Merk Dagang
# Salah satu dikasih diskon, persen harga
# Andhi Prasetyo (C20010004)

class Toko_Saya:
    def __init__ (self, judul, inputPelanggan, 
    inputBarang, belanja1, belanja2, belanja3):
        self.judul_program = judul
        self.nama = inputPelanggan
        self.barang = inputBarang
        self.frekuensi_belanja = belanja1
        self.produk_1 = belanja2
        self.produk_2 = belanja3
    
    def tampil(self):
        pass

class Merk_Dagang(Toko_Saya):
    def __init__(self, judul_program, nama):
        super().__init__(judul_program, nama, 1, 
            float(input("Frekuensi Belanja Bulanan\t: ")),
            float(input("Input Nilai Belanja Makanan ($)\t: ")),
            float(input("Input Nilai Belanja Barang ($)\t: "))
            )
    
    #Override
    def tampil(self):
        point = (self.frekuensi_belanja + self.produk_1 + self.produk_2) / 3

        if point >= 80:
            print("\n" + "Point Akhir Bulan 1".center(30,"=") + "\n"
            f"Nama Pelanggan    : {self.nama}\n"
            f"Belanja Bulan Ke  : {self.barang}\n"
            f"Nilai Shopping    : {self.frekuensi_belanja}\n"
            f"Shop Makanan      : {self.produk_1}\n"
            f"Shop Barang       : {self.produk_2}\n\n"
            f"Point Belanja     : {round(point,2)} (DIAMOND)"
            f"Diskon Belanja"
            )
        elif point >= 70:
            print("\n" + "Point Akhir Bulan 1".center(30,"=") + "\n"
            f"Nama Pelanggan    : {self.nama}\n"
            f"Belanja Bulan Ke  : {self.barang}\n"
            f"Nilai Shopping    : {self.frekuensi_belanja}\n"
            f"Shop Makanan      : {self.produk_1}\n"
            f"Shop Barang       : {self.produk_2}\n\n"
            f"Point Belanja     : {round(point,2)} (PLATINUM)"
            )
        elif point >= 60:
            print("\n" + "Point Akhir Bulan 1".center(30,"=") + "\n"
            f"Nama Pelanggan    : {self.nama}\n"
            f"Belanja Bulan Ke  : {self.barang}\n"
            f"Nilai Shopping    : {self.frekuensi_belanja}\n"
            f"Shop Makanan      : {self.produk_1}\n"
            f"Shop Barang       : {self.produk_2}\n\n"
            f"Point Belanja     : {round(point,2)} (GOLD)"
            )
        elif point >= 50:
            print("\n" + "Point Akhir Bulan 1".center(30,"=") + "\n"
            f"Nama Pelanggan    : {self.nama}\n"
            f"Belanja Bulan Ke  : {self.barang}\n"
            f"Nilai Shopping    : {self.frekuensi_belanja}\n"
            f"Shop Makanan      : {self.produk_1}\n"
            f"Shop Barang       : {self.produk_2}\n\n"
            f"Point Belanja     : {round(point,2)} (SILVER)"
            )
        elif point < 50:
            print("\n" + "Point Akhir Bulan 1".center(30,"=") + "\n"
            f"Nama Pelanggan    : {self.nama}\n"
            f"Belanja Bulan Ke  : {self.barang}\n"
            f"Nilai Shopping    : {self.frekuensi_belanja}\n"
            f"Shop Makanan      : {self.produk_1}\n"
            f"Shop Barang       : {self.produk_2}\n\n"
            f"Point Belanja     : {round(point,2)} (BRONZE30)"
            )

pelanggan1 = Merk_Dagang(print(" PROGRAM DISKON ".center(30,("="))), 
    input("Masukkan Nama Pelanggan\t\t: "), 
    )

pelanggan1.tampil()