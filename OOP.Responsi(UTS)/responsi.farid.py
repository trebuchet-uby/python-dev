class Perpustakaan:
    no_peminjaman = 0
    terlambat = 0
    denda_terlambat = 0

    def __init__(self, InputNama, InputId, InputBuku, InputDurasi):
        self.nama = InputNama
        self.__id = InputId
        self.buku = InputBuku
        self.durasi= InputDurasi

        Perpustakaan.no_peminjaman += 1
        Perpustakaan.terlambat = Denda.kembali-self.durasi
        Perpustakaan.denda_terlambat = Perpustakaan.terlambat*3000

    def tampil(self):
        print("Nama : ", self.nama)
        print("Id : ", self.__id)
        print("Buku : ", self.buku)
        print("Durasi Pinjam : ",self.durasi)
        print("Denda : ", Perpustakaan.denda_terlambat)

class Denda(Perpustakaan):
    kembali = float(input("Lama Kembali : "))

peminjaman1 = Denda(input("Masukan Nama Anda : "),
                           input("Masukan ID : "),
                           input("Masukan Buku : "),
                           float(input("Masukan Durasi Pinjam : ")))
peminjaman1.tampil()