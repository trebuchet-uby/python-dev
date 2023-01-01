print("Program Data Mahasiswa".center(60,"="))
data_nim    = []
data_nama   = []
data_prodi  = []
data_fak    = []

#lagi = "y"

while True :
    print("\n","Menu Program Data Mahasiswa".center(60,"="),"\n")

    print("1. Tambah Data Mahasiswa")
    print("2. Lihat Data Mahasiswa")
    print("3. Ubah Data Mahasiswa")
    print("4. Hapus Data Mahasiswa")
    print("5. Keluar")


    menu = input("\nPilih menu : ")

    if menu == "1" :
        while True:
            print("\n","Tambah Data Mahasiswa".center(60,"="),"\n")
            nim = input("NIM\t\t: ")
            data_nim.append({'nim':nim})            

            nama = input("Nama\t\t: ")
            data_nama.append({'nama':nama})

            prodi = input("Prodi\t\t: ")
            data_prodi.append({'prodi':prodi})
            
            fakultas = input("Fakultas\t: ")
            data_fak.append({'fakultas':fakultas})
            
            lagi = input("\nAda yang mau ditambah Lagi ? ( Y/N) : ")
            if lagi == "y" or lagi == "Y" : continue
            elif lagi == "n" or lagi == "N" : break
    
    elif menu == "2" :
        print("Data Mahasiswa".center(60,"="))
        print(f" {'NIM':<12} {'NAMA':<20} {'PRODI':<8} {'FAKULTAS':<15}")
        print("-"*60)
  
        for i in range(len(data_nim)):
            
            print(f"{data_nim[i]['nim']:<12} {data_nama[i]['nama']:<20} {data_prodi[i]['prodi']:<8} {data_fak[i]['fakultas']:<15}")
            print("-"*60)                
            
    elif menu == "3" :
        while True:
            print("\n","Ubah Data Mahasiswa".center(60,"="),"\n")
            nim = input("Masukkan NIM Data Mahasiswa yang akan diubah : ")
            for i in range (len(data_nim)):
                if nim == data_nim[i]['nim']:
                  print(i)
            nimb = input("NIM\t\t: ")
            data_nim[i] = {'nim':nimb}     

            namab = input("Nama\t\t: ")
            data_nama[i] = {'nama':namab}

            prodib = input("Prodi\t\t: ")
            data_prodi[i] = {'prodi':prodib}
            
            fakultasb = input("Fakultas\t: ")
            data_fak[i] = {'fakultas':fakultasb}
            print(f"\n data mahasiswa : \n {data_nama} \n {data_nim} \n {data_prodi} \n {data_fak} ")
            
            lagi = input("\nAda yang mau diubah Lagi ? ( Y/N) : ")
            if lagi == "y" or lagi == "Y" : continue
            elif lagi == "n" or lagi == "N" : break

    elif menu == "4" :
        while True:
            print("\n","Hapus Data Mahasiswa".center(60,"="),"\n")
            innim = input("Masukkan NIM Data Mahasiswa yang akan dihapus : ")
            for i in range (len(data_nim)):
                if innim == data_nim[i]['nim']:
                  print(i)                  
                  del data_nim[i]
                  del data_nama[i]
                  del data_prodi[i]
                  del data_fak[i]
            print ("Data Berhasil dihapus\n {data_nama} \n {data_nim} \n {data_prodi} \n {data_fak} ")
            
            lagi = input("\nAda yang mau dihapus Lagi ? ( Y/N) : ")
            if lagi == "y" or lagi == "Y" : continue
            elif lagi == "n" or lagi == "N" : break
    elif menu == "5" :
        print("Program end..")
        raise SystemExit
    
    else : continue

    lagi = input("\nKembali Menu Program Data Mahasiswa? ( Y/N) : ")
    if lagi == "y" or lagi == "Y" : continue
    elif lagi == "n" or lagi == "N" : break