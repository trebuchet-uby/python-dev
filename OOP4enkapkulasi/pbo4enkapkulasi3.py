class Sosmed:
    NoAkun=0

    def __init__(self, inputNama, inputRekening, inputPin, inputSaldo):
        self._nama = inputNama
        self._rek = inputRekening
        self.__pin = inputPin
        self.__saldo = inputSaldo

    def tampil(self): #Getter
        print("\n=====Data Nasabah=====\n")
        print("Nama Nasabah        : ", self._nama)
        print("No Rekening Nasabah : ", self._rek)
        print("Pin Nasabah         : ", self.__pin)
        print("Saldo Nasabah       : ", self.__saldo)
        print("No Telp Nasabah     : ", EditData.telpon(self))

        print("\n======================\n")

    def EditPin(self): #Setter
        self.__pin = input("Masukkan Pin Anda : ")

    def TarikSaldo(self): #Setter
        self.__saldo -= int(input("Masukan Nominal Penarikan : "))

class EditData(Sosmed):
    __NoTelp="08123323232334"

    def telpon(self): #Getter
        return self.__NoTelp


class Penarikan(EditData):
    pass


nasabah1 = Penarikan(
    input("Masukkan Nama Anda : "), 
    input("Masukkan Rekening Anda : "),
    input("Masukkan Pin Anda : "), 
    int(input("Masukan Saldo Anda : "))
)

nasabah1.EditPin()
nasabah1.TarikSaldo()
nasabah1.tampil()
