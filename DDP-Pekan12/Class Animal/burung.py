from animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f'Hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')

print("-----Cetak Burung 1-----")
beo = Burung('Burung Beo', 'biji bijian', 'udara', 'bertelur', 'biru dan orange', 'cukurukuk')
beo.cetak_burung()

print("\n-----Cetak Burung 2-----")
hantu = Burung('Burung Hantu', 'daging', 'pohon', 'bertelur', 'Coklat', 'wuf wuf wuf hooooo')
hantu.cetak_burung()

print("\n-----Cetak Burung 3-----")
flamingo = Burung('Burung flamingo', 'biji bijian', 'danau', 'bertelur', 'pink', 'ang ang ang')
flamingo.cetak_burung()