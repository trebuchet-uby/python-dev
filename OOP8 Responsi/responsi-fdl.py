class Peminjaman :
    def __init__(self, nama, judul, tglpinjam, tglkembali):
        self.nama=nama
        self.judul=judul
        self.tanggal_pinjam = tglpinjam
        self.tanggal_kembali = tglkembali

    def tampil(self):
        print(f"\nNama Peminjam : {self.nama}")
        print(f"Judul Buku : {self.judul}")
        print(f"Tanggal Pinjam : {self.tanggal_pinjam}")
        print(f"Tanggal Kembali : {self.tanggal_kembali}")

       
class Buku (Peminjaman):
    def __init__(self, nama):
        super().__init__(nama, input("Masukkan Judul Buku : "), input("Masukkan Tanggal Pinjam : "), input("Masukkan Tanggal Kembali : "))
        super().tampil()

buku1 = Buku(input("Masukkan Nama Anda : "))
