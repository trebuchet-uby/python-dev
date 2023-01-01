class Data:
    def Data_mahasiswa(self):
        print("Nama : Luqman Athariq")

class NIM:
    def Nim_mahasiswa(self):
        print("NIM  : C20010016")

class Prodi(Data, NIM):
    def Prodi_mahasiswa(self):
        print("Prodi : Teknik Informatika")
    
data1=Prodi()
data1.Data_mahasiswa()
data1.Nim_mahasiswa()
data1.Prodi_mahasiswa()

