class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak (self):
        print(f'Hewan {self.nama} ini memakan {self.makanan}. Hewan ini juga, hidup di {self.hidup} dan berkembang biak dengan cara {self.berkembang_biak}')
        
C1 = Animal('Buaya', 'daging', 'perairan tawar', 'bertelur')
C1.cetak()

C2 = Animal('Kucing', 'whiskas', 'darat', 'melahirkan')
C2.cetak()

C3 = Animal('Jerapah', 'daun', 'darat', 'melahirkan')
C3.cetak()

