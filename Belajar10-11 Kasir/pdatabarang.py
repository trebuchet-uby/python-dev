print("Program Inventaris Barang".center(30,"=")+"\n")
data_barang=[]
# lagi = "y"

while True :
    print("Menu Program".center(30,"=")+"\n")

    print("1. Tambah Barang")
    print("2. Hapus Barang\n")

    menu = input("Masukan Menu Program : ")

    if menu == "1" :
        input_barang = input("Masukan barang yang akan ditambahkan : ")
        data_barang.append(input_barang)
        print(f"\n data barang : \n {data_barang}\n")
        
        

    elif menu == "2" :
        hapus_barang = input("Masukan barang ang akan dihapus : ")
        data_barang.remove(hapus_barang)
        print(f"\n data barang : \n {data_barang}")
        
    else : continue

    lagi = input("Apakah anda akan menghapus/menambah barang lagi (Y/N) : ")
    if lagi == "n" or lagi == "N" : break
    elif lagi == "y" or lagi == "Y" : continue


quit("end program......")


    
        
        
    
   
    



    

    
    
        





