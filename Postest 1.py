#Login sederhana
nama = input('Masukkan Nama anda:')
input('Masukkan nim anda:')
print(F'Selamat datang di perhitungan segitiga pythagoras sederhana {nama}!!!')

#Masukkan sisi yang ingin di pilih
print('SEGITIGA PYTHAGORAS')
print('Pilihlah sisi yang ingin anda hitung :')
print('1. Alas')
print('2. Sisi Tegak')
print('3. Sisi Miring')
sisi = int(input('Masukkan pilihan (1/2/3):'))

if sisi == 1:
#menghitung panjang alas
    Sisi_tegak = float(input('Masukkan panjang sisi tegak:'))
    Sisi_miring = float(input('Masukkan panjang sisi miring:'))
    Alas = (Sisi_miring**2 - Sisi_tegak**2)**0.5
    print(F'Panjang sisi Alas adalah: {Alas} CM')

elif sisi == 2:
#menghitung panjang sisi tegak
    Alas = float(input('Masukkan panjang Alas:'))
    Sisi_miring = float(input('Masukkan panjang sisi miring:'))
    Sisi_tegak = (Sisi_miring**2 - Alas**2)**0.5
    print(F'Panjang sisi Alas adalah: {Sisi_tegak} CM')

elif sisi == 3:
#menghitung panjang sisi miring
    Alas = float(input('Masukkan panjang Alas:'))
    Sisi_tegak = float(input('Masukkan panjang sisi tegak:'))
    Sisi_miring = (Sisi_tegak**2 + Alas**2)**0.5
    print(F'Panjang Sisi Miring adalah: {Sisi_miring} CM')

else:
    print("Tidak ada pilihan ini, coba masukkan sisi 1,2 atau 3")