# UTS PBO - Andhi Prasetyo - C20010004

class Biodata: # Nama Class
    
    def __init__(self, # Constructor
        namaBiodata,
        NIMBiodata,
        alamatBiodata,
        fakultasBiodata,
        prodiBiodata,    
    ):

        self.nama       = namaBiodata
        self.NIM        = NIMBiodata
        self.alamat     = alamatBiodata
        self.fakultas   = fakultasBiodata
        self.prodi      = prodiBiodata

    def Tampil(self): # Function Tampil
        print("\n")
        print("===== MENAMPILKAN BIODATA =====")
        print("Nama Mahasiswa\t: ",     self.nama)
        print("NIM Mahasiswa\t: ",      self.NIM)
        print("Alamat Asal\t: ",        self.alamat)
        print("Asal Mahasiswa\t: ",     self.fakultas)
        print("Prodi Mahasiswa\t: ",    self.prodi)
        print("\n")


print("\n")
print("=== PROGRAM INPUT BIODATA ===")
# Object Data 1
data1 = Biodata(
    input("Nama Mahasiswa\t: "),
    input("NIM Mahasiswa\t: "),
    input("Alamat Asal\t: "),
    input("Asal Fakultas\t: "),
    input("Prodi Mahasiswa\t: ")
)

data1.Tampil()