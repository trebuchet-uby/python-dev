class Nasabah:
    NoNasabah=0

    def __init__(self,
    inputNama, inputRekening, 
    inputPin, inputSaldo
    ):
        self.nama   = inputNama
        self.rek    = inputRekening
        self.pin    = inputPin
        self.saldo  = inputSaldo
    
    def tampil(self):
        print("======= DATA NASABAH =======")
        print("Nama Nasabah\t: ", self.nama)
        print("No Rek Nasabah\t: ", self.rek)
        print("PIN  Nasabah\t: ", self.pin)
        print("Saldo Nasabah\t: ", self.saldo)
        print("============================")

class EditData(Nasabah):
    def EditNama(self):
        self.nama = input("Masukkan Nama Anda: ")

nasabah1 = EditData(input("Masukkan Nama Anda: "),
    input("Masukkan Rekening Anda: "),
    input("Masukkan PIN anda: "),
    input("Masukkan Saldo Anda: ")
)


nasabah1.editNama()
nasabah1.tampil()