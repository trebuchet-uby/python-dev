class Toko:
    def __init__ (self, inputNama, inpurHarga):
        self.nama = inputNama
        self.harga = inpurHarga
    
    def tampil(self):
        print(f"Anda membeli {self.nama} dengan harga {self.harga}")

class Buku(Toko):
    def __init__(self, nama):
        super().__init__(nama, 5000)
        super().tampil()

class Roti(Toko):
    def __init__(self, nama):
        super().__init__(nama, 2500)
        super().tampil()

buku = Buku ("Buku Tulis")
roti = Roti ("Donat")