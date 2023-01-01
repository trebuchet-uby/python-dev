print("Kasir".center(30,"=")+"\n")

print("Menu".center(30,"=")+"\n")

list_harga = ["5k","6k","8k"]
no_menu = 0

for harga in list_harga :
    no_menu += 1

    print(f"menu {no_menu} Rp.{harga}")

print("Minuman".center(30,"=")+"\n")

harga_minum = ["2k","3k","4k"]
no_mnm = 0

for harga_mnm in list_harga :
    no_mnm += 1

    print(f"menu {no_mnm} Rp.{harga_mnm}")


while True:
    menu = input("\nMasukan pilihan menu anda : ")
    jumlah = int(input("Masukan jumlah pesanan anda : "))

    if menu== "1" :
        total_mkn = jumlah*5000
        print(f"Anda membeli {jumlah} menu {menu} \n" +
        f"seharga {total_mkn}\n")
    elif menu== "2" :
        total_mkn = jumlah*6000
        print(f"Anda membeli {jumlah} menu {menu} \n" +
        f"seharga {total_mkn}\n")
    elif menu== "3" :
        total_mkn = jumlah*8000
        print(f"Anda membeli {jumlah} menu {menu} \n" +
        f"seharga {total_mkn}\n")
    else : continue

    pesan_minum = input("\nApakah anda akan memesan minuman (Y/N) :")
    if pesan_minum == "n" or pesan_minum == "N" : break
    elif pesan_minum == "y"or pesan_minum == "Y":
        minuman = input("masukan pesanan minuman anda : ")
        jumlah_mnm = int(input("masukan jumlah peasanan anda : "))
    
    else : continue

    if minuman== "1" :
        total_mnm = jumlah_mnm*2000
        print(f"Anda membeli {jumlah_mnm} minuman {minuman} \n" +
        f"seharga {total_mnm}\n")
    elif minuman== "2" :
        total_mnm = jumlah_mnm*3000
        print(f"Anda membeli {jumlah_mnm} minuman {minuman} \n" +
        f"seharga {total_mnm}\n")
    elif minuman== "3" :
        total_mnm = jumlah_mnm*4000
        print(f"Anda membeli {jumlah_mnm} minuman {minuman} \n" +
        f"seharga {total_mnm}\n")
    else : continue

    print("Total Harga".center(30,"="))

    print(f"Total Pesanan anda adalah Rp.{total_mkn+total_mnm}")

    pesan_lagi = input("Apakah Anda Akan Memesan Lagi ? (Y/N) : ")
    if pesan_lagi == "N" or pesan_lagi=="n" : break
    elif pesan_lagi == "Y" or pesan_lagi=="y": continue



quit ("program end.....")



















    

