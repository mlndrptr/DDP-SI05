#

print('\n--- 1. celcius ke fahrenheit ---')

def celcius_ke_fahrenheit(celcius):
    print(celcius* 9/5 + 32)

celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

print('\n--- 2. Mencari Bilangan genap ---')
def is_genap(genap):
    print(genap %2 == 0) 
is_genap(4)
is_genap(7)

print('\n--- 3. Keterangan lulus dan tidak lulus ---')
def skor(nilai):
    if nilai >= 80:
        print('Lulus')
    else:
        print('Gagal')
skor(80)
skor(60)

print('\n--- 4. Mencetak bilangan ganjil ---')
def bil_ganjil(ganjil):
    for m in range (1,ganjil+1, 2):
        print(m, end=' ')
bil_ganjil(20)