from animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan
    
    def cetak_ikan(self):
        super().cetak()
        print(f'Warna ikan ini adalah warna {self.warna_ikan} dan hewan ini berjenis ikan {self.jenis_ikan}')

print("-----Cetak Ikan 1-----")
ikan = Ikan('Ikan badut', 'Plankton', 'air', 'bertelur', 'orange', 'air laut')
ikan.cetak_ikan()

print("\n-----Cetak Ikan 2-----")
ikan = Ikan('Ikan hiu', 'tomat', 'air', 'bertelur atau melahirkan', 'abu - abu', 'air laut')
ikan.cetak_ikan()

print("\n-----Cetak Ikan 3-----")
ikan = Ikan('Ikan tongkol', 'ikan kecil kecil', 'air', 'bertelur', 'biru gelap metalik', 'air laut')
ikan.cetak_ikan()