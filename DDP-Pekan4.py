print('\n===== No 1:  =====')

angka = int(input("Masukkan bilangan: "))
ganjil = "Bilangan Ganjil"
genap = "Bilangan Genap"

if angka % 2 == 0:
    print(genap)
#elif (angka % 2 != 0):
#    print(ganjil)
else:
    print(ganjil)

print('\n===== No 2: Nilai Ujian =====')

nilai_ujian = int(input("Masukkan Nilai Ujian: "))

if nilai_ujian >= 75:
    print("Selamat, kamu lulus!")
else:
    print("Kamu Tidak Lulus")

print('\n===== No 3: Cek Usia dan Status =====')

usia = int(input("Masukkan Usia Anda: "))

if usia >= 18:
    print("Dewasa")
elif usia < 18 and usia > 13:
    print("Remaja")
else:
    print("Anak-anak")

print('\n===== No 4: Cek Keanggotaan =====')

keanggotaan = input("Masukkan Status Keanggotan: ") # Gold, Silver, Bronze

if keanggotaan == "Gold" or keanggotaan == "Silver":
    print("Selamat! Anda mendapatkan diskon.")
elif keanggotaan == "Bronze":
    print("Maaf, Anda belum bisa mendapat diskon.")
else:
    print("Input tidak valid! (gunakan huruf kapital diawal)")

print('\n===== No 5: Pembelian Diskon =====')

jumlah_pembelian = int(input("Masukkan Jumlah Pembelian: "))
harga_item = 1000
harga_diskon = harga_item * jumlah_pembelian * (10/100)
harga_total = harga_item * jumlah_pembelian
total_dengan_diskon = harga_total - harga_diskon

print (f"Anda mendapat diskon 10%, harga per item {harga_item} jadi, total yang harus dibayar {total_dengan_diskon}" if jumlah_pembelian > 100 else print(f"Harga per item {harga_item}, jadi total yang harus dibayar adalah {harga_total}"))
