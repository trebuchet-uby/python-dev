class Toko:
    def __init__ (self, inputNama, inpurHarga):
        self.nama = inputNama
        self.harga = inpurHarga
    
class Buku(Toko):
    def __init__(self, nama):
        super().__init__(nama, 5000)

class Roti(Toko):
    def __init__(self, nama):
        super().__init__(nama, 2500)

buku = Buku ("Buku Tulis")
roti = Roti ("Donat")

print(f"Anda membeli {buku.nama} dengan harga {buku.harga}")
print(f"Anda membeli {roti.nama} dengan harga {roti.harga}")