"""
Program Perulangan Membaca Buku dengan While
"""
jumlah_buku = 10
print('Ibu memberi perintah: "Baca Semua Bukumu"')
jumlah_buku_yang_telah_dibaca = 0
print(f'jumlah buku yang telah dibaca {jumlah_buku_yang_telah_dibaca}')

while jumlah_buku_yang_telah_dibaca < jumlah_buku:
    jumlah_buku_yang_telah_dibaca = jumlah_buku_yang_telah_dibaca + 1
    print(f'Buku ke {jumlah_buku_yang_telah_dibaca} telah dibaca')


print(f'jumlah buku yang telah dibaca {jumlah_buku_yang_telah_dibaca}')
