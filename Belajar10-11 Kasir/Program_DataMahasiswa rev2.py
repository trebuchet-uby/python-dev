print("Program Data Mahasiswa".center(60,"="))
data_nama   = []
data_nim    = []
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
            
            nama = input("Nama\t\t: ")
            data_nama.append(nama)

            nim = input("NIM\t\t: ")
            data_nim.append(nim)

            prodi = input("Prodi\t\t: ")
            data_prodi.append(prodi)
            
            fakultas = input("Fakultas\t: ")
            data_fak.append(fakultas)
            
            print(f"\n data mahasiswa : \n {data_nama} \n {data_nim} \n {data_prodi} \n {data_fak} ")


            lagi = input("\nAda yang mau ditambah Lagi ? ( Y/N) : ")
            if lagi == "y" or lagi == "Y" : continue
            elif lagi == "n" or lagi == "N" : break
    
    elif menu == "2" :
        print("Data Mahasiswa".center(60,"="))
        no = 0
        for i in range (len(data_nim)) :
            no +=1
            print(f"{no}. {data_nama[i]}\t\t {data_nim[i]} {data_prodi[i]} - {data_fak[i]}")

    elif menu == "3" :
        while True:
            print("\n","Ubah Data Mahasiswa".center(60,"="),"\n")
            i = int(input("Masukkan Data ke berapa yang mau dirubah : "))
            namab = input("Nama\t\t: ")
            data_nama[i-1] = namab

            nimb = input("NIM\t\t: ")
            data_nim[i-1] = nimb

            prodib = input("Prodi\t\t: ")
            data_prodi[i-1] = (prodib)
            
            fakultasb = input("Fakultas\t: ")
            data_fak[i-1] = (fakultasb)
            print(f"\n data mahasiswa : \n {data_nama} \n {data_nim} \n {data_prodi} \n {data_fak} ")
            
            lagi = input("\nAda yang mau diubah Lagi ? ( Y/N) : ")
            if lagi == "y" or lagi == "Y" : continue
            elif lagi == "n" or lagi == "N" : break

    elif menu == "4" :
        while True:
            print("\n","Ubah Data Mahasiswa".center(60,"="),"\n")
            i = int(input("Masukkan Data ke berapa yang mau dihapus : "))
        
            data_nim.remove(data_nim[i-1])
            data_nama.remove(data_nama[i-1])
            data_prodi.remove(data_prodi[i-1])
            data_fak.remove(data_fak[i-1])
            print ("Data Berhasil dihapus\n {data_nama} \n {data_nim} \n {data_prodi} \n {data_fak} ")
            
            lagi = input("\nAda yang mau dihapus Lagi ? ( Y/N) : ")
            if lagi == "y" or lagi == "Y" : continue
            elif lagi == "n" or lagi == "N" : break
    else : continue

    lagi = input("\nKembali Menu Program Data Mahasiswa? ( Y/N) : ")
    if lagi == "y" or lagi == "Y" : continue
    elif lagi == "n" or lagi == "N" : break