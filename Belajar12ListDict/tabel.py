import datetime

mahasiswa1 = {
    'nama':'budi',
    'nim':'TI768899',
    'nilai':80,
    'semester':3,
    'lahir':datetime.datetime(2003,10,9)
}

mahasiswa2 = {
    'nama':'tono',
    'nim':'TI769977',
    'nilai':70,
    'semester':4,
    'lahir':datetime.datetime(2002,7,8)
}

mahasiswa3 = {
    'nama':'agus',
    'nim':'TI897765',
    'nilai':90,
    'semester':2,
    'lahir':datetime.datetime(2001,11,15)
}


data_mahasiswa = {
    'M11001':mahasiswa1,
    'M11002':mahasiswa2,
    'M11003':mahasiswa3
}


print(f"{'KEY':<6} {'Nama':<5} {'Nim':<10} {'Nilai':<8} {'Smt':<4} {'Tgl_lahir':<10}")
print("-"*50)
 
for mahasiswa in data_mahasiswa:

    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    NILAI = data_mahasiswa[KEY]['nilai']
    SMT = data_mahasiswa[KEY]['semester']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<6} {NAMA:<5} {NIM:<10} {NILAI:<8} {SMT:<4} {LAHIR:<10}")
    
    

