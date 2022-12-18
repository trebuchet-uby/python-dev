from datetime import date, datetime as dt

today = dt.now()
time = today.strftime("%A, %d %B %Y %H:%M:%S.%f")

line = "=".center(56,"=")
name_shop = "Berkah Shop".center(52)
login = "Login".center(50)

print(line)
print("|",name_shop,"|")
print(line,"\n")
print(">>",login,"<<")
user_name = input("\n Username : ")
password = input("Password : ")

print("\n")

msg_success1 = f"Welcome {user_name}".center(50)
msg_success2 = f"Your last login was on \n{time}".center(50)

if user_name == None or user_name == "" :
    quit("Username cannot be blank!")

elif user_name.count(" ") > 0 : 
    quit("Username cannot contain spaces")

elif user_name != "ida" or password !="p@ssw0rd" :
     quit("Incorrect username or password")

else : 
    print("\n")
    print(">>",msg_success1,"<<")
    print(">>",msg_success2,"<<")
    print(line)

prices = [5000, 8000, 12000, 25000, 3500]
items = ["Aqua", "Fanta", "Chips", "Kitkat", "Oreo"]

list_title = "List".center(50)
print(">>",list_title,"<<")
print("\n 1. Aqua \t: Rp 5.000,- \n")
print(" 2. Fanta \t: Rp 8.000,- \n")
print(" 3. Chips \t: Rp 12.000,- \n")
print(" 4. Kitkat \t: Rp 25.000,- \n")
print(" 5. Oreo \t: Rp 3.500,- \n")

buy = int(input("Enter what you want to buy \t\t: "))
amount = int(input("Enter how many you want to buy : "))

if buy == 1 :
    item = items[0]
    price = prices[0]
    total = prices[0]*amount
elif buy == 2 :
    item = items[1]
    price = prices[1]
    total = prices[1]*amount
elif buy == 3 :
    item = items[2]
    price = prices[2]
    total = prices[2]*amount
elif buy == 4 :
    item = items[3]
    price = prices[3]
    total = prices[3]*amount
elif buy == 5 :
    item = items[4]
    price = prices[4]
    total = prices[4]*amount
else :
    quit("Incorrect input list !!!")

print(line)
detail="Detail".center(50)

print(">>",detail,"<<\n")
print(f"Item \t: {item}, Jumlah \t: {amount}, Harga \t: {price}")
print("\nTotal money you must pay is : Rp", total, ",-\n")

pay_title = "Payment".center(50)

print(line)
print(">>", pay_title,"<<\n")
print(f"Admin \t: {user_name} \nDate \t: {time}\n")

payment=int(input("Payment \t: Rp "))
print("Cashback \t: Rp",payment-total)

print(line)
thank="Thank You".center(50)
print(">>",thank,"<<")
print(line)

