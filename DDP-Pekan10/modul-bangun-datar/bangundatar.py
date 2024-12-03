import math

def lk_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas Persegi {sisi} * {sisi} = {luas}')
    print(f'Keliling Perseginya adalah {keliling}')

def lk_p_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * panjang * lebar
    print('Luas Persegi Panjang', panjang, 'X', lebar, "=", luas)
    print('Keliling Persegi Panjangnya adalah', 2, 'X', panjang, 'X', lebar, "=", luas)

def l_segitiga(alas, tinggi):
    luas = 1/2 * alas * tinggi
    print(f'Luas Segitiga {1/2} * {alas} * {tinggi} = {luas}')

def l_lingkaran(r1, r2):
    luas = 3.14 * r1 * r2
    print(f'Luas Lingkarannya adalah {3.14} * {r1} * {r2} = {luas}')

def lk_j_genjang(alas, tinggi):
    luas = alas * tinggi
    keliling = 2 * alas + tinggi
    print(f'Luas Jajar Genjang {alas} * {tinggi} = {luas}')
    print(f'Keliling Jajar Genjangnya adalah {2} * {alas} + {tinggi}')
