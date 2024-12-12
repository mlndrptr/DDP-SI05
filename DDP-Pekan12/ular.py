from animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ular = warna_ular
        self.jenis_ular = jenis_ular
    
    def cetak_ular(self):
        super().cetak()
        print(f'Warna ular ini adalah warna {self.warna_ular} dan hewan ini berjenis ular {self.jenis_ular}')

print("\n-----Cetak Ular 1-----")
ular = Ular('ular piton', 'daging', 'semak belukar', 'bertelur', 'coklat, hitam, abu abu', 'berbisa')
ular.cetak_ular()

print("\n-----Cetak Ular 2-----")
ular = Ular('ular kobra', 'daging', 'rawa rawa', 'bertelur', 'abu abu kehitaman', 'berbisa')
ular.cetak_ular()

print("\n-----Cetak Ular 3-----")
ular = Ular('ular sawah', 'reptil', 'sawah', 'bertelur', 'hijau', 'tidak berbisa')
ular.cetak_ular()