class Registrasi:

    def __init__(self,
                 inputUser,
                 inputPassword,
                 inputValidasi,
                 inputEmail,
                 ):

        self.username   = inputUser
        self.__password = inputPassword
        self.validasi   = inputValidasi
        if self.validasi == self.__password:
            print("Password Cocok")
        else:
            print("Password Salah")
        self.email      = inputEmail

    def Tampil(self):
        print("\n")
        print("======= DATA SAYA =======")
        print("Username Anda    : ", self.username)
        print("Password Anda    : ", self.__password)
        print("Email anda       : ", self.email)

    def EditPassword(self):
        print("======= EDIT PASSWORD =======")
        self.__password = input("Masukkan Password Baru : ")

    def editBiodata(self):
        print("\n")
        print("======= EDIT BIODATA =======")
        self.email    = input("Masukkan Email Baru : ")
        self.username = input("Masukkan Username Baru : ")

class Biodata(Registrasi):
    nama    = input("Masukkan Nama Anda :")
    alamat  = input("Masukkan Alamat Anda :")
    usia    = input("Masukkan Usia Anda :")

    def DataUser(self):
        print("\n")
        print("======= DATA DIRI =======")
        print("Nama anda    : ", Biodata.nama)
        print("Alamat Anda  : ", Biodata.alamat)
        print("Usia Anda    : ", Biodata.usia)

akun1 = Biodata(
    input("Masukkan Username    : "),
    input("Masukkan Password    : "),
    input("Masukkan Validasi    : "),
    input("Masukkan Email       : ")
)

akun1.EditPassword()
akun1.editBiodata()
akun1.Tampil()
akun1.DataUser()
