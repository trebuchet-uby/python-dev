pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
    Warkop DKI
    List Menu 
 
    ==============================
    1. kapal api : Rp 6.000
    2. good day : Rp 5.000
    3. tora caffe : Rp 8.000
    4. Americano : Rp 10.000
    ==============================
    """)
    print("""
    SETIAP PEMBELIAN MENU LIST 1 DAN 2 DALAM JUMLAH PESAN 5 KE ATAS, DISKON 20% !!
    """)
    
    pesan=str(input("masukkan list angka menu kopi ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "1":
        listnama= "kapal api"
        harga=(6000*jumlahpesan)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "2":
        listnama= "good day"
        harga = (5000*jumlahpesan)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon)
        else:
            diskon =(0)
            totalharga =int(harga)
    elif pesan == "3":
        listnama= "tora caffe"
        harga=int(8000*jumlahpesan)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "4":
        listnama= "Americano"
        harga=int(10000*jumlahpesan)
        diskon=0
        totalharga = int(harga)
    else:
        listnama = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print("--------------------------")
    print("Warkop DKI")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")