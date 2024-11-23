print('\n===== No 1 =====')

nama = "Mulandari Putri"
nim = "0110124132"
rombel = "SI05"
no_telp = "+628889749840"
alamat = "Dramaga, Kab. Bogor"

print(f"Perkenalkan nama saya {nama} \nnim {nim}")
print("Saya dari rombel", rombel)
print("No. Telepon:", no_telp)
print("Alamat:", alamat)

print('\n===== No 2 =====')

nama = "Shelfia Anatasya Dwi Artha"
nim = "0110124019"
rombel = "SI05"
no_telp = "+6285810341491"
alamat = "Kab. Bogor, Jawa Barat"

print(f"Perkenalkan nama teman saya {nama} \nnim {nim}")
print("Teman saya dari rombel", rombel)
print("No. Telepon:", no_telp)
print("Alamat:", alamat)

print('\n===== No 3 =====')

print("Menghitung Berat Badan Ideal Perempuan")
TB = int(input('Masukan Tinggi Badan: '))
bb_ideal = (TB - 100) - (TB - 100) * 0.15

print("Berat badan idealnya adalah:", bb_ideal)

print('\n===== No 4 =====')

print("Mengkonversi suhu celcius ke fahreinheit")
celcius = int(input("Masukan Suhu Celcius: "))
fahreinheit = int(celcius*9/5)+32

print(celcius, "derajat celcius", "dalam suhu fahreinheit adalah", fahreinheit, "derajat fahreinheit.")

print('\n===== No 5 =====')

print("Menghitung luas dan keliling Tabung")
JariJari = int(input("Masukan Jari jari: "))
Tinggi = int(input("Masukan Tinggi: "))
Phi = 22/7
Keliling = int(2*Phi*JariJari)
Luas_Permukaan = int(2*Phi*JariJari*(JariJari+Tinggi)) #int untuk menghilangkan .0

print("Luas Tabung adalah", Luas_Permukaan)
print("Keliling tabung adalah", Keliling)