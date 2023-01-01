class Toko:
    def __init__(self, inputJudul, inputJenis):
        self.judul = inputJudul
        self.jenis = inputJenis
    
    def judul_program(self):
        print(" Toko Buku ".center(30,"=")+("\n"))

        print("1. Komik")
        print("2. Novel")
        print("3. Majalah\n")

        print(30*"=")