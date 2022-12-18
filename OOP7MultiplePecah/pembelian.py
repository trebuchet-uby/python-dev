from toko import Toko
from komik import Komik
from novel import Novel
from buku import Buku

class Pembelian(Toko, Komik, Novel, Buku):
    def beli(self):
        if self.jenis == "1":
            self.harga_komik()
            self.pembelian_komik()
        elif self.jenis == "2":
            self.harga_novel()
            self.pembelian_novel()
        elif self.jenis == "3":
            self.harga_Buku()
            self.pembelian_buku()
        else:
            quit("Input Salah !!!")