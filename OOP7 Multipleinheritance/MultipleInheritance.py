class A:
    def tampilA(self):
        print("ini kelas A")

class B:
    def tampilB(self):
        print("ini kelas B")

class Coba(A, B):
    pass

coba1 = Coba()

coba1.tampilA
coba1.tampilB
