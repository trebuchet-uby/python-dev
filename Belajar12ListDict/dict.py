data = {
    'nama':'budi',
    'nim':'TI9087766',
    'nilai':90

}

print(data)

#mengambil data berdasarkan key
print(data['nilai'])
print(data.get('sks'))

#mengganti data 
data['nilai'] = 80
print(data['nilai'])
data['sks'] = 70
data.update({'nama':'tono'})
print(data)
print(data['sks'])

#menghapus data

del data['sks']
print(data)


# loop dictionary

for value in data.values():
    print(value)

for key in data.keys():
    print(data.get(key))

for key,value in data.items():
    print(f"{key} Mahasiswa adalah {value}")





