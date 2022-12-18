class Akun:

    def __init__(self, inputUsername, inputPassword, inputEmail):
        self.user       = inputUsername
        self.__password   = inputPassword
        self.email      = inputEmail
    
    def tampil(self):
        print("===== Data Akun =====")
        print("Username\t: ", self.user)
        print("Password\t: ", self.__password)
        print("Email\t: ", self.email)
        print("=====================")
    
    def editPass(self): # setter
        self.__password = EditData.newPass(self)

class EditData(Akun):
    def editPass(self): # Setter
       return input("Masukkan Password Baru : ")

akun1 = EditData(
    input("Masukkan Username : "),
    input("Masukkan Password : "),
    input("Masukkan Email : ")
)

akun1.editPass()
akun1.tampil()