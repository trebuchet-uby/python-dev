class Toko:
    def __init__(self, 
        inputNama, inputHarga, inputJumlah):
        self.nama = inputNama
        self.harga = inputHarga
        self.banyak = inputJumlah
    def tampil(self):
        print(f"anda membeli {self.banyak} buah {self.nama} " +
        f"dengan harga @ {self.harga}")
    def jumlah(self):
        self.total = (buku1.harga*buku1.banyak) + (roti1.harga*roti1.banyak)
        print("Total".center(42,"="))
        print(f"\nTotal Harga Rp.{self.total}")
        print(42*"=")

class Buku(Toko):
    def __init__(self, nama):
        super().__init__(nama,
            int(input("Masukkan harga buku : ")),
            int(input("Masukkan jumlah buku : "))
            )
        super().tampil()

class Roti(Toko):
    def __init__(self, nama):
        super().__init__(nama,
            int(input("Masukkan harga roti : ")),
            int(input("Masukkan jumlah roti : "))
        )
        super().tampil()

buku1 = Buku("Buku Tulis")
roti1 = Roti("Donat")
Toko.jumlah(self=Toko)

