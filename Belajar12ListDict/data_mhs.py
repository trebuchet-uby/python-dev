judul=("Database Mahasiswa".center(30,"="))
print(judul)

nama_mhs=[]
nim_mhs=[]
prodi_mhs=[]
smt_mhs=[]

while True:
  print("         Menu          ")
  print("1.Tambah Data Mahasiswa")
  print("2.Ubah   Data Mahasiswa")
  print("3.Hapus  Data Mahasiswa")
  print("4.Lihat  Data Mahasiswa")
  menu=input("Pilih Kode Menu :")
  if menu == "1":
    print("TAMBAH DATA MAHASISWA")
    nama=input("Nama Mahasiswa :")
    nim=input("NIM Mahasiswa :")
    prodi=input("Prodi Mahasiswa :")
    smt=input("Semester Mahasiswa :")
    
    nama_mhs.append({'Nama':nama})
    nim_mhs.append({'NIM':nim})
    prodi_mhs.append({'prodi':prodi})
    smt_mhs.append({'Semester':smt})
    
    print("program sukses")
    
  elif menu == "2":
    print("EDIT DATA MAHASISWA")
    data=0
    
    nim=input("Masukkan NIM Mahasiswa Yang akan Di Edit :")
    
    for i in range(len(nim_mhs)):
      if nim == nim_mhs[i]['NIM']:
        data=i
        ubah_nama=input("Masukkan Nama Mahasiswa:")
        ubah_nim=input("masukkan NIM Mahasiswa :")
        ubah_prodi=input("masukkan prodi :")
        ubah_smt=input("masukkan semester :")
        
        nama_mhs[data]={'Nama':ubah_nama}
        nim_mhs[data]={'NIM':ubah_nim}
        prodi_mhs[data]={'prodi':ubah_prodi}
        smt_mhs[data]={'Semester':ubah_smt}
        
        print("Data Berhasil Dirubah")
  
  elif menu == "3":
    print("HAPUS DATA MAHASISWA")
    nim=input("Masukkan NIM Mahasiswa Yang Akan Di Hapus :")
    for i in range(len(nim_mhs)):
      if nim == nim_mhs[i]['NIM']:
        del nama_mhs[i]
        del nim_mhs[i]
        del prodi_mhs[i]
        del smt_mhs[i]
        
      print("sukses")
      
  elif menu == "4":
    print("lihat data")
    
    print(f"{'NIM':<10} {'nama':<14}  {'prodi':<20} {'Semester':<2}")
    
    print("_"*55)
    for i in range(len(nim_mhs)):
      print(f"{nim_mhs[i]['NIM']:<10} {nama_mhs[i]['Nama']:<14} {prodi_mhs[i]['prodi']:<20} {smt_mhs[i]['Semester']:<2}")
    
    print("_"*55)
  else:break
  pilihan=input("lanjutkan program lagi ?, ketik y untuk lanjut, ketik n untuk keluar:")
  if pilihan == "y" :continue
  elif pilihan == "n" :break