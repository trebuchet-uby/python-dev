print("MENU".center(30,"="))

harga_mkn = ["5k","10k","15k","20k"]
menu = 0

for harga in harga_mkn:
    menu += 1
    print(f"Harga Menu {menu} adalah {harga} ")


makanan = input("Masukan Menu Pilihan Anda :")
jumlah = int(input("Masukan Jumlah Pesanan :"))

if makanan == "1" : 
    print(f"Harga Total Pesanan Anda Adalah Rp.{5000*jumlah}")
elif makanan == "2" : 
    print(f"Harga Total Pesanan Anda Adalah Rp.{10000*jumlah}")
elif makanan == "3" : 
    print(f"Harga Total Pesanan Anda Adalah Rp.{15000*jumlah}")
elif makanan == "4" : 
    print(f"Harga Total Pesanan Anda Adalah Rp.{20000*jumlah}")
else : print("Input Salah!!!!!1")

quit ("program end.....")