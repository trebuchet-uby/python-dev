log=("Pusat Administrasi Data".center(50,"+"))
print(log)


data_nim=[]
data_nama=[]
data_prodi=[]
data_semes=[]


print("")
while True:
  print("Pilihan program :")
  print("1.tambah data")
  print("2.ubah data")
  print("3.hapus data")
  print("4.lihat data")
  men=input("silahkan memasukkan pilihan :")
  if men == "1":
    print("TAMBAH DATA")
    nim=input("masukkan NIM Mahasiswa :")
    nama=input("masukkan nama Mahasiswa :")
    prodi=input("masukkan prodi :")
    semes=input("masukkan semester :")
    
    data_nim.append({'NIM':nim})
    data_nama.append({'Nama':nama})
    data_prodi.append({'prodi':prodi})
    data_semes.append({'Semester':semes})
    
    print("program sukses")
    
  elif men == "2":
    print("UBAH DATA")
    data=0
    
    nim=input("masukkan nim :")
    
    for i in range(len(data_nim)):
      if nim == data_nim[i]['NIM']:
        data=i
        nimb=input("masukkan NIM :")
        namab=input("masukkan nama Mahasiswa :")
        prodib=input("masukkan prodi :")
        semesb=input("masukkan semester :")
        
        data_nim[data]={'NIM':nimb}
        data_nama[data]={'Nama':namab}
        data_prodi[data]={'prodi':prodib}
        data_semes[data]={'Semester':semesb}
        
        print("merubah data berhasil")
  
  elif men == "3":
    print("hapus data")
    nim=input("masukkan nim yang dihapus :")
    for i in range(len(data_nim)):
      if nim == data_nim[i]['NIM']:
        del data_nim[i]
        del data_nama[i]
        del data_prodi[i]
        del data_semes[i]
        
      print("program sukses")
      
  elif men == "4":
    print("lihat data")
    
    print(f"{'NIM':<10} {'nama':<14}  {'prodi':<20} {'Semester':<2}")
    
    print("-"*40)
    for i in range(len(data_nim)):
      print(f"{data_nim[i]['NIM']:<10} {data_nama[i]['Nama']:<14} {data_prodi[i]['prodi']:<20} {data_semes[i]['Semester']:<2}")
    
    print("-"*40)
  else:break
  pil=input("apakah ingin lanjut :")
  if pil == "y" or "Y":continue
  elif pil == "n" or "N":break