import math

def kubus(sisi):
    luas = 6 * sisi * sisi
    volume = sisi * sisi * sisi
    print(f'Luas permukaan kubus  {6} * {sisi} * {sisi} = {luas}')
    print(f'Volume Kubusnya  {sisi} * {sisi} * {sisi} = {volume}')

def balok(panjang, lebar, tinggi):
    luas = 2 * panjang * lebar + panjang * tinggi + lebar * tinggi
    volume = panjang * lebar * tinggi
    print(f'luas Permukaan Balok {2} * {panjang} * {lebar} + {panjang} * {tinggi} + {lebar} * {tinggi} = {luas}')
    print(f'Volume Baloknya {panjang} * {lebar} * {tinggi} = {volume}')

def bola(jarijari):
    luas = 4 * 3.14 * jarijari * jarijari
    volume = 4/3 * 3.14 * jarijari * jarijari * jarijari
    print(f'Luas Permukaan Bola {4} * {3.14} * {jarijari} * {jarijari} = {luas}')
    print(f'Volume Bola {4/3} * {3.14} * {jarijari} * {jarijari} * {jarijari} = {volume}')

def prisma(l_alas, keliling_alas, tinggi ):
    luas = 2 * l_alas + keliling_alas * tinggi
    volume = l_alas * tinggi
    print(f'Luas Permukaan Prisma {2} * {l_alas} + {keliling_alas} * {tinggi} = {luas}')
    print(f'Volume Prisma {l_alas} * {tinggi} = {volume}')

def tabung(jarijari, tinggi):
    luas = 2 * 3.14 * jarijari * tinggi + 2 * 3.14 * jarijari * jarijari
    volume = 3.14 * jarijari * jarijari * tinggi 
    print(f'Luas Permukaan Tabung {2} * {3.14} * {jarijari} * {tinggi} + {2} * {3.14} * {jarijari} * {jarijari} = {luas}')
    print(f'Volume Tabung {3.14} * {jarijari} * {jarijari} * {tinggi} = {volume}')