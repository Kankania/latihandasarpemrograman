# Deskriftif
# membuat variabel nama barang
# membuat variabel harga barang 
# membuat variabel persen harga
# input nama barang
# input harga barang 
# menghitung harga barang
# harga barang * persen / 100
# print harga barang bersama nama barang

modal_keseluruhan = 0
laba_keseluruhan = 0

while(True):
    nama_barang = input("Masukan nama barang :")
    harga_barang1 =input("Masukan harga barang :")
    persen = input('masukan persen barang')
    barang_terjual = int(input('Masukan jumlah barang terjual'))

    harga_keuntungan = int(harga_barang) * int(persen) / 100
    harga_jual = int(harga_barang) + harga_keuntungan

    # Menghitung modal
    modal = harga_barang1 + barang_terjual
    print(nama_barang,'dijual dengan: ',harga_jual)
    modal_keseluruhan = modal_keseluruhan + Modal

    # Menghitung laba
    laba = keuntungan_persen * barang_terjual
    # Menghitung laba keseluruhan
    laba_keseluruhan = laba_keseluruhan + laba

    print('barang', nama_barang)
    print('harga barang', harga_barang)
    print('keuntungan per barang', keuntungan persen)
    print('dijual dengan harga', harga_jual)
    print('terjual', barang_terjual)
    print('modal', modal)
    print('laba', laba)

    ApakahLanjut = input("apakah ingin input barang lain? Y lanjut : ")
    if(ApakahLanjut != 'Y'):
        break

print('...............')
print('modal keseluruhan',modal_keseluruhan)
print('laba keseluruhan', laba_keseluruhan)