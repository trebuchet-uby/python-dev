
class Pesanan:

    def __init__(self, daftarmen):
        self.pilih = daftarmen

    def menu(self):
        print("1. soto")
        print("2. bakso")
        print("3. mie ayam")

    def tampil(self):
        pass



class Pembelian(Pesanan):

    def menu(self):
        print("1. es teh")
        print("2. es kopi")
        print("3. lemon tea")

    def pemesanan(self):
        menu = input("masukan menu : ")
        hrga = int(input("masukan harga : "))
        jumlah = int(input("masukan jumlah"))

        print(f"anda memesaan {jumlah} menu {menu} dengan harga {jumlah*hrga} ")

    def tampil(self):
        pilihan = input("Pilih pesanan  Menu : ")
        if pilihan == "1":
            print(Pesanan.menu(self))
            self.pemesanan()
        elif pilihan == "2":
            print(Pembelian.menu(self))
            self.pemesanan()


pesanan1 = Pembelian(Pesanan.tampil(self=Pesanan))
pesanan1.tampil()