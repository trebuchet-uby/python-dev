# UTS PBO - Andhi Prasetyo - C20010004

class Kasir: # Nama Class
    nopesanan = 0
    hargaTotal = 0
    hargaTambahan = 0
    hargabayar = 0

    def __init__(self, # Constructor
        inputnama, 
        inputjml, 
        inputharga
    ):

        self.nama = inputnama
        self.jumlah = inputjml
        self.harga = inputharga

        Kasir.nopesanan += 1
        Kasir.hargaTotal = self.jumlah * self.harga
        Kasir.hargaTambahan = DataTransaksi.jumlah * DataTransaksi.harga
        Kasir.hargabayar = Kasir.hargaTotal + Kasir.hargaTambahan

    def tampil(self):
        print("\n")
        print("===== TAMPIL TRANSAKSI =====")
        print("Nomor Pesanan\t: ", Kasir.nopesanan)
        print("Nama Pesanan\t: ", self.nama)
        print("Jumlah Pesanan\t: ", self.jumlah)
        print("Harga Satuan\t: ", self.harga)
        print("Total Harga\tNo: ", Kasir.hargaTotal)

    def total(self):
        print("\n")
        print("== TOTAL PEMBAYARAN ==")
        print("Total Harga Bayar\t: ", Kasir.hargabayar)
        print("\n")
        print("== TRANSAKSI SELESAI ==")

class DataTransaksi(Kasir):

        print("\n")
        print("== INPUT DATA TAMBAHAN ==")
        tambahan1   = input("Tambahan Item\t: ")
        jumlah      = int(input("Jumlah Item\t: "))
        harga       = int(input("Harga Item\t: "))

        def tampiltambahan(self):
            print("\n")
            print("Tambah Pesanan\t: ", DataTransaksi.tambahan1)
            print("Jumlah Tambahan\t: ",DataTransaksi.jumlah)
            print("Harga Satuan\t: ",DataTransaksi.harga)
            print("Harga Total\t: ", Kasir.hargaTambahan)


print("\n")
print("== INPUT DATA PESANAN ==")
transaksi1 = DataTransaksi(
    input("Nama Item\t: "), 
    int(input("Jumlah Item\t: ")), 
    int(input("Harga Satuan\t: "))
)

transaksi1.tampil()
transaksi1.tampiltambahan()
transaksi1.total()