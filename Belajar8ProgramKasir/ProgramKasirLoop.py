from datetime import date, datetime as dt

hari_ini = date.today()

now = dt.now()
time = now.strftime("%A, %d %B %Y %H:%M:%S.%f")

judul_program = "Program Kasir".center(60)
judul_menu = "Menu".center(60)
judul_bayar = "Struk Pembayaran".center(60)
terimakasih = "Terima Kasih".center(60)
garis = "=".center(64,"=")

pilihan="y"
while pilihan=="y":

    print(garis)
    print("|",judul_program,"|")
    print(garis,"\n")
    pelanggan=str(input("Masukkan Nama Pelanggan = "))
    print("\n",garis)
    print(judul_menu)
    print(garis,"\n")
    print("""
    List Menu Nasi Goreng 
 
    A. Nasi Goreng original : Rp 11.000
    B. Nasi Goreng Ati      : Rp 12.000
    C. Nasi Goreng Lamongan : Rp 12.000
    D. Nasi Goreng Spesial  : Rp 15.000
   
    """)
    pesan=str(input("Masukkan list menu diatas = "))
    jumlahpesan=int(input("Masukkan jumlah pesanan = "))
    
    if pesan == "a":
        makanan= "Nasi Goreng Original"
        harga=11000
        total=(harga*jumlahpesan)
      
    elif pesan == "b":
        makanan= "Nasi Goreng Ati"
        harga = 12000
        total=(harga*jumlahpesan)
       
    elif pesan == "c":
        makanan= "Nasi Goreng Lamongan"
        harga=11000
        total=(harga*jumlahpesan)
       
    elif pesan == "d":
        makanan= "Nasi Goreng Spesial"
        harga=14000
        total=(harga*jumlahpesan)
       
    else:
        makanan = "-"
        harga = "-"
        total = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
    
    
    print("""
     List Minuman

    1. Teh Panas / Es       : Rp  4.000
    2. Jerus Panas / Es     : Rp  4.500
    3. Lemon Tea Panas / Es : Rp. 5.000 
    """)
    pesan=str(input("Masukkan list menu diatas = "))
    jumlahpesan1=int(input("Masukkan jumlah pesanan = "))
    
    if pesan == "1":
        minuman= "Teh Panas / Es"
        harga1=4000
        total1=(harga*jumlahpesan1)
      
    elif pesan == "2":
        minuman= "Jeruk Panas / Es"
        harga1=4500
        total1=(harga*jumlahpesan1)
       
    elif pesan == "3":
        minuman= "Lemon Tea Panas / Es"
        harga1=5000
        total1=(harga*jumlahpesan1)
    else:
        minuman = "-"
        harga1 = "-"
        total1 = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
    
    print(garis)
    print(f"Menu : {makanan} = {jumlahpesan} Porsi | {minuman} = {jumlahpesan1} Gelas")

    print("Total Harga : Rp ", total+total1)
    bayar=int(input("Bayar = Rp "))


    print(garis)
    print("\n|", judul_bayar,"|\n")
    print(f"Pelanggan \t: {pelanggan} \nTanggal \t: {time}\n")
  
    print(garis)
    print(f"|\t  Menu \t\t \t    harga    jumlah \ttotal\n")
    print(garis)
    print(f"|{makanan}\t\t  Rp {harga}    {jumlahpesan}\t\t{total}")
    print(f"|{minuman}\t\t  Rp {harga1}     {jumlahpesan1}\t\t{total1}")
    print("\n",garis)
    print("| Total \t: Rp ",total+total1)
    print("| Dibayar \t: Rp ",bayar)
    print("| Kembali\t: Rp ",bayar-(total+total1))
    print("\n\n",terimakasih)
    print(garis)
    pilihan=input("apakah anda ingin order kembali Y/N =")