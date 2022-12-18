line = "=".center(56,"=")
name_shop = "Soto Mbak Ida".center(52)
menu = "Daftar Menu".center(50)
detail_order = "Rincian Pemesanan".center(50)
no = 1
thanks = "Terimakasih".center(52)

print(line)
print("|",name_shop,"|")
print(line)
print(">>",menu,"<<")
print("1. Soto Ayam     6. Kerupuk")
print("2. Soto Sapi     7. Teh Anget")
print("3. Sate Usus     8. Jeruk Anget")
print("4. Sate Ati      9. Es Teh")
print("5. Gorengan      10. Es Jeruk")

list_menu = ["Soto Ayam", "Soto Sapi", "Sate Usus", "Sate Ati", "Gorengan", "Kerupuk", "Teh Anget", "Jeruk Anget", "Es Teh", "Es Jeruk"]
list_price = [8000, 10000, 2.500, 3000, 1000, 1000, 2000, 2500, 2000, 2500]
list_order = []
list_amount = []

choose=input("Apakah anda ingin memesan? Y/N : ")

while choose == "y" or choose == "Y":
    order = input("Masukkan pesanan : ")
    quantity = input("Masukkan jumlah pesanan : ")
    
    list_order.append(order)
    list_amount.append(quantity)

    choose=input("Apakah anda ingin memesan lagi? Y/N : ")
else :
    if choose == "n" or choose == "N" :
        print(line)
        print(">>",total,"<<")
		
		#Get length list order for looping
        length_order = len(list_order)
        total_payment = 0
        
        for x in range (length_order):
            #For get order
            idx_order = list_order[x]
            idx = int(idx_order)
            ordered = list_menu[idx-1]
            
            #For calculation amount
            order_amount = list_amount[x]
            amount = int(order_amount)
            price = list_price[idx-1]
            total = amount * price 
          
            print(f"{no}. {ordered} >> {amount} : {total}")
            
            no += 1
            
            # To calculate the entire order
            total_payment = total_payment + total
            
    else :
        quit("Inputan Salah !!!")
        
    print("Total yang harus anda bayar : ", total_payment)
    
    payment = int(input("Masukkan pembayaran : "))
    cashback = payment - total_payment
    
    if(cashback < 0) :
        print("Maaf uang anda kurang !!!")
    elif (cashback >= 0) :
        print("Kembalian anda : ", cashback)
        print(line)
        print("|",thanks,"|")
        print(line)
    else :
        quit("Inputan Salah !!!")
    
    
