print("Kalkulator".center(30,"="))

nilai1 = float(input("Masukan nilai 1 : "))
nilai2 = float(input("Masukan nilai 2 : "))
operator = input("Masukan operator  (+,x,/,-): ")


if operator == "+" :
    hasil = nilai1 + nilai2
    print(f"hasil penjumlahan nilai 1 + nilai 2 adalah : {hasil}")
elif operator == "-" :
    hasil = nilai1 - nilai2
    print(f"hasil pengurangan nilai 1 - nilai 2 adalah : {hasil}")
elif operator == "x" :
    hasil = nilai1 * nilai2
    print(f"hasil perkalian nilai 1 * nilai 2 adalah : {hasil}")
elif operator == "/" :
    hasil = nilai1 / nilai2
    print(f"hasil pembagian nilai 1 / nilai 2 adalah : {hasil}")
else : print("Input anda salah")

quit ("program end")