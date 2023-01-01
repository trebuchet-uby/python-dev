class Restaurant:
    nopesanan = 0
    hargaTotal = 0
    hargaTambahan = 0
    hargabayar = 0
    def __init__(self, inputnama, inputjml, inputharga):
        self.nama = inputnama
        self.jumlah = inputjml
        self.harga = inputharga

        Restaurant.nopesanan += 1
        Restaurant.hargaTotal = self.jumlah * self.harga
        Restaurant.hargaTambahan = Tambahan.jumlah * Tambahan.harga
        Restaurant.hargabayar = Restaurant.hargaTotal + Restaurant.hargaTambahan

    def tampil(self):
        print("=============================")
        print("pesanan no ", Restaurant.nopesanan)
        print("Nama pesanan ", self.nama)
        print("jumlah pesanan ", self.jumlah)
        print("harga   ", self.harga)
        print("Total Harga Pesanan : ", Restaurant.hargaTotal)

    def total(self):
        print("Harga bayar : ", Restaurant.hargabayar)

class Tambahan(Restaurant):

        tambahan1 = input("tambahan laku : ")
        jumlah = int(input("jumlah : "))
        harga = int(input("harga : "))

        def tampiltambahan(self):
            print("tambahan  : ", Tambahan.tambahan1)
            print("jumlah    : ",Tambahan.jumlah)
            print("Harga     : ",Tambahan.harga)
            print("harga total tambahan ", Restaurant.hargaTambahan)


pesanan1 = Tambahan(input("nama pesanan "), int(input("jumlah pesanan ")), int(input("Harga ")))

pesanan1.tampil()
pesanan1.tampiltambahan()
pesanan1.total()