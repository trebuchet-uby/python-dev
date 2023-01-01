line = "=".center(56,"=")
name_program = "Program Data Mahasiswa".center(52)
menu = "Menu Program".center(50)

print(line)
print("|",name_program,"|")
print(line)

nama_mhs = []
nim_mhs = []
smt_mhs = []

while True:
    no = 1
    menu = "Menu Program".center(50)
    add = "Tambah Data".center(50)
    edit = "Ubah Data".center(50)
    remove = "Hapus Data".center(50)
    list = "Daftar Data".center(50)
    
    print(">>",menu,"<<")
    
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Daftar Data\n")
    
    menu = input("Masukkan Menu Program : ")
    
    if menu == "1" :
        print(line)        
        print(">>",add,"<<")
        
        input_nama = input("Masukkan nama     : ")
        input_nim  = input("Masukkan nim      : ")
        input_smt  = input("Masukkan semester : ")
       
        nama_mhs.append(input_nama)
        nim_mhs.append(input_nim)
        smt_mhs.append(input_smt)
        
        print("Data Berhasil Ditambahkan !!!!")
        
    elif menu == "2" :
        print(line)        
        print(">>",list,"<<")
        
        length_data = len(nama_mhs)
        
        for x in range (length_data):
            print(f"Data ke {no} : {nama_mhs[x]}, {nim_mhs[x]}, {smt_mhs[x]}")
            no += 1
            
        print(line)        
        print(">>",edit,"<<")
        
        input_idx = int(input("Data yang ingin anda ubah adalah data ke : "))
        
        input_nama = input("\nMasukkan nama     : ")
        input_nim  = input("Masukkan nim      : ")
        input_smt  = input("Masukkan semester : ")
        
        nama_mhs[input_idx-1] = input_nama
        nim_mhs[input_idx-1] = input_nim
        smt_mhs[input_idx-1] = input_smt
        
        print("Data Berhasil Diubah !!!!")        
    
    elif menu == "3" :
        print(line)        
        print(">>",list,"<<")
        
        length_data = len(nama_mhs)
        
        for x in range (length_data):
            print(f"Data ke {no} : {nama_mhs[x]}, {nim_mhs[x]}, {smt_mhs[x]}")
            no += 1
        
        print(line)        
        print(">>",remove,"<<")
        
        input_idx = int(input("Data yang ingin anda hapus adalah data ke : "))
        
        nama_mhs.pop(input_idx-1)
        nim_mhs.pop(input_idx-1)
        smt_mhs.pop(input_idx-1)
        
        print("Data Berhasil Dihapus !!!!")
        
    elif menu == "4" :
        
        print(line)        
        print(">>",list,"<<")
        
        length_data = len(nama_mhs)
        
        if length_data < 1 :
            print("Data Kosong !!!!")
            print(line)  
            continue        
        else :
            for x in range (length_data):
                print(f"Data ke {no} : {nama_mhs[x]}, {nim_mhs[x]}, {smt_mhs[x]}")
                no += 1
        
    else : continue

    lagi = input("\nApakah anda akan menghapus/menambah lagi (Y/N) : ")
    print(line)
    if lagi == "n" or lagi == "N" :
        break
    elif lagi == "y" or lagi == "Y" :
        continue
    
quit("Program Selesai")