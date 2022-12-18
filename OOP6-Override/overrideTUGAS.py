# Tugas : Toko
# Turunannya merk dagang
# Salah satu dikasih diskon, persen harga

class Nilai_Akhir:
    def __init__ (self, judul, inputNama, 
    inputSemester, nilai1, nilai2, nilai3):
        self.judul_program = judul
        self.nama = inputNama
        self.semester = inputSemester
        self.nilai_kehadiran = nilai1
        self.nilai_tugas = nilai2
        self.nilai_ujian = nilai3
    
    def tampil(self):
        pass

class Nilai_smt1(Nilai_Akhir):
    def __init__(self, judul_program, nama):
        super().__init__(judul_program, nama, 1, 
            float(input("Masukkan Nilai Kehadiran : ")),
            float(input("Input Nilai Tugas : ")),
            float(input("Input Nilai Ujian : "))
            )
    
    #Override
    def tampil(self):
        ipk = (self.nilai_kehadiran + self.nilai_tugas + self.nilai_ujian) / 3

        if ipk >= 80:
            print("\n" + "Nilai Akhir Semester 1".center(30,"=") + "\n"
            f"Nama Mahasiswa    : {self.nama}\n"
            f"Semester          : {self.semester}\n"
            f"Nilai Kehadiran   : {self.nilai_kehadiran}\n"
            f"Nilai Tugas       : {self.nilai_tugas}\n"
            f"Nilai Ujian       : {self.nilai_ujian}\n\n"
            f"Nilai IPK         : {round(ipk,2)} (A)"
            )
        elif ipk >= 70:
            print("\n" + "Nilai Akhir Semester 1".center(30,"=") + "\n"
            f"Nama Mahasiswa    : {self.nama}\n"
            f"Semester          : {self.semester}\n"
            f"Nilai Kehadiran   : {self.nilai_kehadiran}\n"
            f"Nilai Tugas       : {self.nilai_tugas}\n"
            f"Nilai Ujian       : {self.nilai_ujian}\n\n"
            f"Nilai IPK         : {round(ipk,2)} (B)"
            )
        elif ipk >= 60:
            print("\n" + "Nilai Akhir Semester 1".center(30,"=") + "\n"
            f"Nama Mahasiswa    : {self.nama}\n"
            f"Semester          : {self.semester}\n"
            f"Nilai Kehadiran   : {self.nilai_kehadiran}\n"
            f"Nilai Tugas       : {self.nilai_tugas}\n"
            f"Nilai Ujian       : {self.nilai_ujian}\n\n"
            f"Nilai IPK         : {round(ipk,2)} (C)"
            )
        elif ipk >= 50:
            print("\n" + "Nilai Akhir Semester 1".center(30,"=") + "\n"
            f"Nama Mahasiswa    : {self.nama}\n"
            f"Semester          : {self.semester}\n"
            f"Nilai Kehadiran   : {self.nilai_kehadiran}\n"
            f"Nilai Tugas       : {self.nilai_tugas}\n"
            f"Nilai Ujian       : {self.nilai_ujian}\n\n"
            f"Nilai IPK         : {round(ipk,2)} (D)"
            )
        elif ipk < 50:
            print("\n" + "Nilai Akhir Semester 1".center(30,"=") + "\n"
            f"Nama Mahasiswa    : {self.nama}\n"
            f"Semester          : {self.semester}\n"
            f"Nilai Kehadiran   : {self.nilai_kehadiran}\n"
            f"Nilai Tugas       : {self.nilai_tugas}\n"
            f"Nilai Ujian       : {self.nilai_ujian}\n\n"
            f"Nilai IPK         : {round(ipk,2)} (E)"
            )

smt1 = Nilai_smt1(print("Program Nilai".center(30,("="))), 
    input("Masukkan Nama Mahasiswa : "), 
    )

smt1.tampil()

