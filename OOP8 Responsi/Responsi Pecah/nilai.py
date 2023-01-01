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