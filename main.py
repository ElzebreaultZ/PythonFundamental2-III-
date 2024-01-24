"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial = Langkah berurutan
2. Percabangan= Langkan melompat jika kondisi terpenuhi
3. Perulangan = Mengulang langkah yang sama berkali kali sampai kondisi terpenuhi
"""

# Sekuensial
print('ibu berkata, "pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di Toko ?"')
print('ibu menjawab. "Beli satu botol susu, jika ada telur, beli 6"')
print('maka Budi berangkat ke toko')
print('Dan Mulai Berbelanja')

# Percabangan
jumlah_botol_susu = 10
jumlah_telur = 6
jumlah_uang_yang_diberikan = 100.000
print('Ibu memberi perintah kepada anaknya agar anaknya belanja ke toko')
print('Ibu: "Nak Tolong belikan 1 bbotol susu, jika ada telur, beli 6. Ini uang 100.000 untuk membeli botol susu dan telur')
print('"Anak: Baik, Ibu!!!"')
print('Kemudian anak tersebut pergi ke toko untuk belanja')
print('Anak Mengecek apakah persediaan botol susunya ada ??')
if jumlah_botol_susu >0:
    print('Ternyata botol tersebut tersedia untuk dibeli dengan harga 20.000')
    if jumlah_uang_yang_diberikan >20.000:
       print ('Anak membeli satu botol susu tersebut')
    else:
        print('sehingga uang anak tidak cukup untuk membeli botol susu tersebut')
else:
    print('Ternyata tidak ada botol susu yang tersedia untuk dibeli')
print('Kemudian, anak tersebut juga mencari 6 telur yang disuruh ibunya')
if jumlah_telur ==0:
    print('Ternyata tidak ada telur yang tersedia sehingga anak tersebut tidak membeli telur')
if jumlah_telur <6 and jumlah_telur >0:
    print('Ternyata hanya terdapat beberapa telur kurang dari 6 butir sehingga anak tersebut membeli seadanya')
if jumlah_telur >5:
    print('Ternyata 6 telur tersebut tersedia dengan harga 80.000')
    if jumlah_uang_yang_diberikan >79.999:
        print('Karena uangnya cukup Anak tersebut membeli 6 telurnya')
    else:
        print("anak tersebut tidak jadi membeli telur karena uang tidak cukup")
print('Kemudian, anak tersebut pulang ')
# Bisa juga diletakkan disini (bukan yang di indentasi) dengan comman print budi pulang - menyerahkan kepada ibu