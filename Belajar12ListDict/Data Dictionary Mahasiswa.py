line = "=".center(56,"=")
program_name = "Dictionary Data Mahasiswa".center(52)
menu = "Menu Program".center(50)

print(line)
print("|",program_name,"|")
print(line)

list_nim   = []
list_name   = []
list_prodi  = []
list_smt    = []

while True :
    
    menu = "Menu Program".center(50)
    add = "Add Data".center(50)
    edit = "Edit Data".center(50)
    remove = "Remove Data".center(50)
    list = "List Data".center(50)
    
    print(line)
    print(">>",menu,"<<")
    
    print("1. Add Data")
    print("2. Edit Data")
    print("3. Remove Data")
    print("4. List Data\n")
    
    menu = input("Input menu program : ")

    if menu == "1" :
        while True :
            print(line)        
            print(">>",add,"<<")
            
            input_nim =   input("Input nim      : ")
            input_name  = input("Input name     : ")
            input_prodi = input("Input prodi    : ")
            input_smt   = input("Input semester : ")
           
            list_nim.append({'nim':input_nim})
            list_name.append({'name':input_name})
            list_prodi.append({'prodi':input_prodi})
            list_smt.append({'semester':input_smt})
            
            print("\nAdd Successful!!!")
            
            again = input("\nDo you want to add more data ? (Y/N) : ")
            if again == "y" or again == "Y" : 
                continue
            elif again == "n" or again == "N" : 
                break
            else :
                quit("Wrong Input!!!")
                
    elif menu == "2" :
        while True:
            idx = 0
            print(line)        
            print(">>",edit,"<<")
            
            input_nim = input("Input NIM for edit : ")      
            
            for i in range (len(list_nim)):
                if input_nim == list_nim[i]['nim']:
                  idx = i
                  
            input_nim   = input("\nInput nim      : ")
            input_name  = input("Input name     : ")
            input_prodi = input("Input prodi    : ")
            input_smt   = input("Input semester : ")
            
            list_nim[idx] = {'nim':input_nim}
            list_name[idx] = {'name':input_name}
            list_prodi[idx] = {'prodi':input_prodi}
            list_smt[idx] = {'semester':input_smt}
            
            print("\nEdit Successful!!!")
            
            again = input("\nDo you want to edit more data ? (Y/N) : ")
            if again == "y" or again == "Y" : 
                continue
            elif again == "n" or again == "N" : 
                break
            else :
                quit("Wrong Input!!!")
    
    elif menu == "3" :
        while True:
            print(line)        
            print(">>",remove,"<<")
            
            input_nim = input("Input NIM for remove : ")      
            
            for i in range (len(list_nim)):
                if input_nim == list_nim[i]['nim']:
                    del list_nim[i]
                    del list_name[i]
                    del list_prodi[i]
                    del list_smt[i]
                  
            print("\nRemove Successful!!!")
            
            again = input("\nDo you want to remove more data ? (Y/N) : ")
            if again == "y" or again == "Y" : 
                continue
            elif again == "n" or again == "N" : 
                break
            else :
                quit("Wrong Input!!!")
    
    elif menu == "4" :
        print(line)        
        print(">>",list,"<<")
        
        print(f"{'NIM':<15} {'NAMA':<20} {'PRODI':<10} {'SEMESTER':<15}")
        print("-"*56)
  
        for i in range(len(list_nim)):
            print(f"{list_nim[i]['nim']:<15} {list_name[i]['name']:<20} {list_prodi[i]['prodi']:<10} {list_smt[i]['semester']:<15}")
            print("-"*56)                
    else : continue

    again = input("\nDo you want go back to menu ? (Y/N) : ")
    if again == "y" or again == "Y" : 
        continue
    elif again == "n" or again == "N" : 
        break
    else :
        quit("Wrong Input!!!")
    
quit("Program End")