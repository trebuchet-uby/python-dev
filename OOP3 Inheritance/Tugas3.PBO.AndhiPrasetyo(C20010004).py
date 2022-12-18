# Menggunakan Konsep Inheritance Bebas
# Yang Satu Data Barang dan Data Harga
# Atau Seperti Kemarin
# Tugas ini minimal enggunakan 3 Kelas
class Monster:
    jumlah_harta = 0
    
    def __init__(self, inputClan, inputTeam):
        self.clan   = inputClan
        self.team = inputTeam
    
    def tentangClan(self):
        print(10*"="+" Tentang Clan "+10*"=")
        print("Nama Pasukan     : ", self.clan)
        print("Jumlah Team      : ", self.team)   
        
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

Monster1 = Kekuatan(
    input("Nama Clan\t: "),
    int(input("Jumlah Team\t: "))
)

class hartaClan(Monster):
    Monster.jumlah_harta = Kekuatan.harga_pasukan * 1000
    print(10*"="+" Jumlah Harta "+10*"=")
    print("Harta Legion\t: ", Monster.jumlah_harta)

Monster1.tentangClan()
Monster1.tentangKekuatan()
Monster1.biayaSatuan()