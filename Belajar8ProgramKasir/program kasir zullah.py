pilihan = "y" or "Y"
while pilihan == "y" or "Y":
        pembeli = input("Masukkan nama Pembeli: ")
        print ("Nama Pembeli :", pembeli)

        print("DAFRTAR MENU MAKANAN".center(50,"="))
        print("1. Kakap bakar")
        print("2. Lele bakar")
        print("3. Ayam bakar")
        print("4. FrencFries")
        print("5. Pisang Coklat")

        print("----------------------------------------")
        print("DAFTAR MENU MINUMAN".center(50,"="))
        print("1. Teh/ Es Teh") 
        print("2. Jeruk/ Es Jeruk")
        print("3. Es Kelapa Muda")
        print("4. Es Buah")

        print("Harga Makanan".center(50,"="))
        harga = ["18k","10k","15k","8k","8k"]
        Makan = 0
        for i in harga :
            Makan += 1
            print(f"Menu {Makan} dengan harga {i}")

        print("Harga Minuman".center(50,"="))
        harga1 = ["3k","4k","5k","8k"]
        Minum = 0
        for a in harga1 :
            Minum += 1
            print(f"Nomor {Minum} dengan harga {a}")
            
        Pesan = input("Makan/Minum? : ")
        if Pesan == "Makan" :
            Pesanan = int(input("Masukan Nomor Menu Makanan Pilihan Anda: "))
            Jumlah = int(input("Masukan Jumlah Pesanan Anda: "))
            if Pesanan == 1 :
                print(f"Menu 1 : Kakap bakar\nHarga : Rp.18.000\nTotal Pembayaran : Rp. {Jumlah*18000}\n")
            elif Pesanan == 2 :
                print(f"Menu 2 : Lele bakar\nHarga : Rp.10.000\nTotal Pembayaran : Rp. {Jumlah*10000}\n")
            elif Pesanan == 3 :
                print(f"Menu 3 : Ayam bakar\nHarga : Rp.15.000\nTotal Pembayaran : Rp. {Jumlah*15000}\n")
            elif Pesanan == 4 :
                print(f"Menu 4 : FrencFries\nHarga : Rp. 8.000\nTotal Pembayaran : Rp. {Jumlah*8000}\n")
            elif Pesanan == 5 :
                print(f"Menu 5 : Pisang Coklat\nHarga : Rp. 8.000\nTotal Pembayaran : Rp. {Jumlah*10000}\n")
            else: print("Pesanan Salah!")
            
        if Pesan == "Minum" :
            Pesanan = int(input("Masukan Nomor Menu Minuman Pilihan Anda: "))
            Jumlah = int(input("Masukan Jumlah Pesanan Anda: "))
            if Pesanan == 1 :
                print(f"Minum 1 : Teh / Es Teh\nHarga : Rp.3.000\nTotal Pembayaran : Rp. {Jumlah*3000}\n")
            elif Pesanan == 2 :
                print(f"Minum 2 : Jeruk / Es Jeruk\nHarga : Rp.4.000\nTotal Pembayaran : Rp. {Jumlah*4000}\n")
            elif Pesanan == 3 :
                print(f"Minum 3 : Es Kelapa Muda\nHarga : Rp.3.000\nTotal Pembayaran : Rp. {Jumlah*5000}\n")
            elif Pesanan == 4 :
                print(f"Minum 4 : Es Buah\nHarga : Rp. 8.000\nTotal Pembayaran : Rp. {Jumlah*8000}\n")    
            else: print("Pesanan Salah!")
            
        pilihan=input("Apakah anda ingin pesan kembali?? Y/N =")