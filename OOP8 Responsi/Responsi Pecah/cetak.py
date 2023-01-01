from data import DataMahasiswa
from nilai import NilaiMahasiswa

class tampilData(DataMahasiswa, NilaiMahasiswa):
    
    def tampil(self):
        self.inputDataMahasiswa()
        self.inputNilaiMahasiswa()