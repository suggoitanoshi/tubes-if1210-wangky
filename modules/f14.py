#F14 - Melihat Riwayat Penggunaan Wahana

import modules.globalvars as globalvars
import modules.common as common

#KAMUS

def riwayat_wahana():
    #Cek apakah Admin
    if (common.is_admin()): #jika admin
        #ambil ID yang ingin di dilihat riwayatnya
        id=input('Masukkan ID Wahana: ')
        #jumlah
        j=0
        #salin tiket dari globalvars agar pengetikan lebih mudah
        tiket=globalvars.penggunaan_tiket
        for i in range(globalvars.penggunaan_count):
            if(tiket[i][2]==id):
                j=j+1
        #buat array hasil
        hasil=[0 for i in range (j)]
        #siapkan index untuk hasil
        k=0
        for i in range(globalvars.penggunaan_count):
            if(tiket[i][2]==id):
                hasil[k]=tiket[i]
                k=k+1

        #Tampilkan Hasil
        print('Tanggal_Bermain \t | \t Username Pengguna \t | \t Jumlah Tiket')
        for i in range (k):
            print(f'{hasil[i][1]} \t\t | \t {hasil[i][0]} \t\t\t | \t {hasil[i][3]} ')
        
