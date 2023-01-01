class DataMahasiswa:
    
    def inputDataMahasiswa(self):
        nama = input("Nama mahasiswa: ")
        NIM = input("NIM Mahasiswa: ")
        Prodi = input("Prodi Mahasiswa: ")
        print("\n")

        print(f"Nama Mahasiswa {nama}")
        print(f"NIM Mahasiswa {NIM}")
        print(f"Prodi Mahasiswa {Prodi}")
        print("\n")

class NilaiMahasiswa:

    def inputNilaiMahasiswa(self):
        nilaiResponsi = int(input("Nilai Responsi: "))
        if nilaiResponsi >= 80:
            print("Nilai Mahasiswa : A")
        elif nilaiResponsi >= 70:
            print("Nilai Mahasiswa : B")
        elif nilaiResponsi >= 60:
            print("Nilai Mahasiswa : C")
        elif nilaiResponsi >= 50:
            print("Nilai Mahasiswa : D")
        else :
            print("Nilai Mahasiswa : E")
    
class tampilData(DataMahasiswa, NilaiMahasiswa):
    
    def tampil(self):
        self.inputDataMahasiswa()
        self.inputNilaiMahasiswa()

data1 = tampilData()
data1.tampil()
