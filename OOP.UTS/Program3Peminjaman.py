# UTS PBO - Andhi Prasetyo - C20010004

class Perpustakaan: # nama Class
    NoPeminjamanan = 0
    Meminjam = 0
    Durasi_Pinjam = 0

    def __init__(self, InputNama, InputId, InputBuku, InputDurasi):
        self.nama = InputNama
        self.__id = InputId # Properti Bersifat Private
        self.buku = InputBuku
        self.durasi= InputDurasi

        Perpustakaan.NoPeminjamanan += 1
        Perpustakaan.Meminjam = Peminjaman.LamaPinjam-self.durasi
        Perpustakaan.Durasi_Pinjam = Perpustakaan.Meminjam*2000

    def tampil(self): # Function Tampil
        print("\n")
        print("=== DATA PEMINJAMAN ANDA ===")
        print("Nama Anggota\t: ", self.nama)
        print("Id Anggota\t: ", self.__id)
        print("Judul Buku\t: ", self.buku)
        print("Durasi Pinjam\t: ",self.durasi)
        print("Saldo Awal ID\t: ", Peminjaman.LamaPinjam*2000)
        print("Tarif Sewa\t: ", self.durasi*2000)
        print("Saldo Akun\t: ", Perpustakaan.Durasi_Pinjam)
        print("\n")
        print("=== TRANSAKSI SELESAI ===")
        print("\n")

class Peminjaman(Perpustakaan):

    print("\n")
    print("==== DURASI SEWA (2K/HARI) ====")
    LamaPinjam = int(input("Lama Pinjam\t: "))
    print("Saldo Awal ID\t:", LamaPinjam * 2000)


print("\n")
print("== INPUT DATA PENGEMBALIAN BUKU ==")
datapinjam1 = Peminjaman(
    input("Masukan Nama ID\t: "),
    input("Masukan ID Anda\t: "),
    input("Judul Buku\t: "),
    int(input("Lama Peminjaman\t: "))
)

datapinjam1.tampil()