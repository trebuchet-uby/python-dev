class Buku:
    jumlah = 0

    def __init__(self, inputJenis, inputStok):
        self.jenis  = inputJenis
        self.stock  = inputStok
    
    def keterangan(self):
        print(10*"="+" Keterangan Buku "+10*"=")
        print("Jenis Buku   : ", self.jenis)
        print("Stock        : ", self.stock)

class Buku_umum(Buku):
    judul = input("Masukkan Judul : ")
    harga = input("Masukkan Harga : ")
    pengarang = input("Masukkan Pengarang : ")

    def data_buku(self):
        print(10*"="+" Data Buku "+10*"=")
        print("Judul Buku : ", self.judul)
        print("Harga Buku : ", self.harga)
        print("Pengarang Buku : ", self.pengarang)


#buku1 = Buku(input("Masukkan Jenis Buku : "), 
#   input("Masukkan Stock Buku : "))

#buku1.keterangan()

buku2 = Buku_umum(input("Masukkan Jenis Buku : "), 
    input("Masukkan Stock Buku :"))

buku2.data_buku()
buku2.keterangan()