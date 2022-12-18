# Menggunakan Konsep Inheritance Bebas
# Yang Satu Data Barang dan Data Harga
# Atau Seperti Kemarin
# Tugas ini minimal enggunakan 3 Kelas

class Monster:
    jumlah_harta = 0
    
    def __init__(self, inputClan, inputPasukan):
        self.clan   = inputClan
        self.pasukan = inputPasukan
    
    def tentangClan(self):
        print(10*"="+" Tentang Clan "+10*"=")
        print("Nama Pasukan     : ", self.clan)
        print("Jumlah Pasukan   : ", self.pasukan)     
        
class Kekuatan(Monster):
    senjata = input("Jenis senjata\t: ")
    damage = int(input("Masukkan damage\t: "))
    health = int(input("Masukkan health\t: "))
    
    def tentangKekuatan(self):
        print(10*"="+" Kekuatan "+10*"=")
        print("Nama Senjata     : ", self.senjata)
        print("Jumlah Damage    : ", self.damage)
        print("jumlah Health    : ", self.health)

    harga_senjata   = 30000
    harga_damage    = 7500 * damage
    harga_health    = 10000 * health
    harga_pasukan   = harga_senjata + harga_damage + harga_health
    
    def biayaSatuan(self):
        print(10*"="+" Biaya Per-Pasukan "+10*"=")
        print("Biaya Senjata    : ", self.harga_senjata)
        print("Jumlah Serangan  : ", self.harga_damage)
        print("jumlah Kesehatan : ", self.harga_health)
        print("Biaya PerPasukan : ", self.harga_pasukan)
    
class Skill(Kekuatan):

    def __init__(Kekuatan, dasar1, sedang1, ulti1):
        Kekuatan.dasar  = dasar1
        Kekuatan.sedang = sedang1
        Kekuatan.ulti   = ulti1

    dasar   = input("Skill-Dasar\t: ")
    sedang  = input("Skill-Sedang\t: ")
    ulti    = input("Skill-Ulti\t: ")
    
    def tentangSkill(kekuatan):
        print(10*"="+" Skill "+10*"=")
        print("Skill Dasar      : ", Kekuatan.dasar)
        print("Skill Sedang     : ", Kekuatan.sedang)
        print("Skill Ulti       : ", Kekuatan.ulti)

Monster1 = Kekuatan(
    input("Nama Clan\t: "),
    int(input("Jumlah Pasukan\t: "))
)

Monster1.tentangClan()
Monster1.tentangKekuatan()
Monster1.biayaSatuan()