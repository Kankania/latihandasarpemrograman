# Deskriptif
# membuat Variabel nama barang
# membuat Variabel harga barang
# membuat Variabel persen barang
# input nama barang
# input harga Barangbarang
# menghitung harga barang
# harga barang * barang / 100
# print harga barang beserta nama barang

namabarang1 = input("\nMasukan nama barang : ")
hargabarang1 = int(input("\nMasukan harga barang : Rp. "))

namabarang2 = input("\nMasukan nama barang : ")
hargabarang2 = int(input("\nMasukan harga barang : Rp. "))

namabarang3 = input("\nMasukan nama barang : ")
hargabarang3 = int(input("\nMasukan harga barang : Rp. "))
laba = int(input('masukan laba (%): '))

Modal = int(input('masukan modal awal : Rp. '))

nilailaba1 = hargabarang1 * (laba/100)
nilailaba2 = hargabarang2 * (laba/100)
nilailaba3 = hargabarang3 * (laba/100)
keuntungan1 = int(hargabarang1) * laba / 100
keuntungan2 = int(hargabarang2) * laba / 100
keuntungan3 = int(hargabarang3) * laba / 100

harga1 = hargabarang1 + nilailaba1
harga2 = hargabarang2 + nilailaba2
harga3 = hargabarang3 + nilailaba3
Total = harga1+harga2+harga3
Totalk = keuntungan1 + keuntungan2 + keuntungan3
Totalakhir = Modal - Totalk

print(namabarang1, 'dijual dengan harga Rp. ' , harga1, 'dengan laba 10% senilai ',keuntungan1 )
print(namabarang2, 'dijual dengan harga Rp. ' , harga2, 'dengan laba 10% senilai ',keuntungan2 )
print(namabarang3, 'dijual dengan harga Rp. ' , harga3, 'dengan laba 10% senilai ',keuntungan3 )
print('Total harga Jual     : Rp. ',Total)
print('Modal yang dikeluarkan : Rp. ', Modal)
print('Total Keuntungan    : Rp. ',Totalk)
print('Total uang : Rp.', Totalakhir)