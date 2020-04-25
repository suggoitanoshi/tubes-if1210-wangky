#F01 - Save File

import csv
import modules.globalvars as globalvars

#KAMUS

def save():
    #User
    f_user=input('Masukkan nama File User: ')    
    with open('external_files/'+f_user,mode='w',newline='') as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        writer = csv.writer(csv_file, delimiter=',')
        #menginput data ke csv
        for i in range(globalvars.users_count):
            writer.writerow(globalvars.users[i])

    #Daftar Wahana
    f_user=input('Masukkan nama File Daftar Wahana: ')    
    with open('external_files/'+f_user,mode='w',newline='') as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        writer = csv.writer(csv_file, delimiter=',')
        #menginput data ke csv
        for i in range(globalvars.list_wahana_count):
            writer.writerow(globalvars.list_wahana[i])

    #Pembelian Tiket
    f_user=input('Masukkan nama File Pembelian Tiket: ')    
    with open('external_files/'+f_user,mode='w',newline='') as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        writer = csv.writer(csv_file, delimiter=',')
        #menginput data ke csv
        for i in range(globalvars.pembelian_count):
            writer.writerow(globalvars.pembelian_tiket[i])

    #Penggunaan Tiket
    f_user=input('Masukkan nama File Penggunaan Tiket: ')    
    with open('external_files/'+f_user,mode='w',newline='') as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        writer = csv.writer(csv_file, delimiter=',')
        #menginput data ke csv
        for i in range(globalvars.penggunaan_count):
            writer.writerow(globalvars.penggunaan_tiket[i])

    #Kepemilikan Tiket
    f_user=input('Masukkan nama File Kepemilikan Tiket: ')    
    with open('external_files/'+f_user,mode='w',newline='') as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        writer = csv.writer(csv_file, delimiter=',')
        #menginput data ke csv
        for i in range(globalvars.kepemilikan_count):
            writer.writerow(globalvars.kepemilikan_tiket[i])

    #Refund Tiket
    f_user=input('Masukkan nama File Refund Tiket: ')
    with open('external_files/'+f_user,mode='w',newline='') as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        writer = csv.writer(csv_file, delimiter=',')
        #menginput data ke csv
        for i in range(globalvars.refund_count):
            writer.writerow(globalvars.refund_tiket[i])

    #Kritik dan Saran
    f_user=input('Masukkan nama File Kritik dan Saran: ')    
    with open('external_files/'+f_user,mode='w',newline='') as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        writer = csv.writer(csv_file, delimiter=',')
        #menginput data ke csv
        for i in range(globalvars.kritik_count):
            writer.writerow(globalvars.kritik_dan_saran[i])

    #Kehilangan Tiket
    f_user=input('Masukkan nama File Kehilangan Tiket: ')    
    with open('external_files/'+f_user,mode='w',newline='') as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        writer = csv.writer(csv_file, delimiter=',')
        #menginput data ke csv
        for i in range(globalvars.kehilangan_count):
            writer.writerow(globalvars.kehilangan_tiket[i])
            
    print()
    print("Data Berhasil Disimpan!")
    print()
