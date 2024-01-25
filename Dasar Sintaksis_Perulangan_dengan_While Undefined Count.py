"""
Program Perulangan Membaca Buku dengan While Sampai Paham
"""
jumlah_buku = 10
print('Ibu memberi perintah: "Baca Semua Bukumu dan pahami"')
total_jumlah_baca = 0

jumlah_buku_yang_telah_dibaca_dan_dipahami = 0
print(f'jumlah buku yang telah dibaca dan dipahami {jumlah_buku_yang_telah_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca +1
    if jumlah_buku_yang_telah_dibaca_dan_dipahami == 9:
        print(f'buku ke {jumlah_buku_yang_telah_dibaca_dan_dipahami + 1} belum paham')
    else:
        jumlah_buku_yang_telah_dibaca_dan_dipahami = jumlah_buku_yang_telah_dibaca_dan_dipahami + 1
        print(f'Buku ke {jumlah_buku_yang_telah_dibaca_dan_dipahami} telah dibaca dan dipahami')



print(f'jumlah buku yang telah dibaca dan dipahami {jumlah_buku_yang_telah_dibaca_dan_dipahami}')
if jumlah_buku_yang_telah_dibaca_dan_dipahami == jumlah_buku:
    print('Bu, semua buku sudah dibaca dan dipahami')
else:
    print(f'Maaf bu tidak semua buku tidak saya pahami. '
          f'Saya hanya bisa memahami {jumlah_buku_yang_telah_dibaca_dan_dipahami} buku')