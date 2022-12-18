from encodings import utf_8_sig
from os import umask


print("CEK KELULUSAN\n")


matkul  = input("Masukkan mata kuliah       : ")
tugas   = float(input("Masukan nilai Tugas  : "))
uts     = float(input("Masukan nilai UTS    : "))
uas     = float(input("Masukan nilai UAS    : "))

nilai = (0.3*tugas)+(0.35*uts)+(0.35*uas)

if nilai >= 70.0: print("Anda Lulus mata kuliah", matkul)
if nilai < 70.0: print("Anda Tidak Lulus mata kuliah", matkul)


# jika nilainya diatas 70.0 lulus
# jika nilainya dibawah 70.0 tidak lulus