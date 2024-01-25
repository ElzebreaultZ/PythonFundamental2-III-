"""
Program Perulangan Membaca Buku
"""
jumlah_buku = 10
jumlah_buku_yang_telah_dibaca = 0
print(f'jumlah buku yang telah dibaca {jumlah_buku_yang_telah_dibaca}')

print('Ibu memberi perintah: "Baca Semua Bukumu"')
for jumlah_buku_yang_telah_dibaca in range(1,jumlah_buku+1):
    print(f'buku ke-{jumlah_buku_yang_telah_dibaca} sudah dibaca')

print(f'jumlah buku yang telah dibaca {jumlah_buku_yang_telah_dibaca}')

#Tanpa For
print('Membaca buku ke-1')
print('Membaca buku ke-2')
print('Membaca buku ke-3')
print('Membaca buku ke-4')
print('Membaca buku ke-5')
print('Membaca buku ke-6')
print('Membaca buku ke-7')
print('Membaca buku ke-8')
print('Membaca buku ke-9')
print('Membaca buku ke-10')
#dll