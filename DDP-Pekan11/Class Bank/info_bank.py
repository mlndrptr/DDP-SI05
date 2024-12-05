from Bank import *

#ciptakan object
mulan = Bank('001','uland',5000000)
mingyu = Bank('002','Kim Mingyu',7000000)
leo = Bank('003','Leo',8000000)
tasya = Bank('004','Shelfia anatasya', 11000000)

#use member class
mulan.nabung(3000000)
leo.nabung(1000000)
mingyu.tarik(2000000)
leo.tarik(6000000)
print(Bank.BANK,
"\n==========================")
mulan.cetak()
mingyu.cetak()
leo.cetak()
tasya.cetak()
print("Jumlah Nasabah: %i orang" %Bank.jmlNasabah)