#F01 - Load File

import csv
import modules.globalvars as globalvars

#KAMUS

def load():
    #User
    f_user=input('Masukkan nama File User: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #Masukkan data ke array global, catat jumlah data
        jmlbrs=0
        for item in csv_reader:
            globalvars.users[jmlbrs] = [item[0],item[1],int(item[2]),item[3],item[4],item[5],int(item[6])]
            jmlbrs += 1
        globalvars.users_count = jmlbrs
        
    #Daftar Wahana
    f_user=input('Masukkan nama File Daftar Wahana: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #Masukkan data ke array global, catat jumlah data
        jmlbrs=0
        for item in csv_reader:
            globalvars.list_wahana[jmlbrs] = [item[0], item[1], int(item[2]), int(item[3]), bool(item[4])]
            jmlbrs += 1
        globalvars.wahana_count = jmlbrs

    #Pembelian Tiket
    f_user=input('Masukkan nama File Pembelian Tiket: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #Masukkan data ke array global, catat jumlah data
        jmlbrs=0
        for item in csv_reader:
            globalvars.pembelian_tiket[jmlbrs] = [item[0], item[1], item[2], int(item[3])]
            jmlbrs += 1
        globalvars.pembelian_count = jmlbrs

    #Penggunaan Tiket
    f_user=input('Masukkan nama File Penggunaan Tiket: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #Masukkan data ke array global, catat jumlah data
        jmlbrs=0
        for item in csv_reader:
            globalvars.penggunaan_tiket[jmlbrs] = [item[0], item[1], item[2], int(item[3])]
            jmlbrs += 1
        globalvars.penggunaan_count = jmlbrs

    #Kepemilikan Tiket
    f_user=input('Masukkan nama File Kepemilikan Tiket: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #Masukkan data ke array global, catat jumlah data
        jmlbrs=0
        for item in csv_reader:
            globalvars.kepemilikan_tiket[jmlbrs] = [item[0], item[1], int(item[2])]
            jmlbrs += 1
        globalvars.kepemilikan_count = jmlbrs

    #Refund Tiket
    f_user=input('Masukkan nama File Refund Tiket: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #Masukkan data ke array global, catat jumlah data
        jmlbrs=0
        for item in csv_reader:
            globalvars.refund_tiket[jmlbrs] = [item[0], item[1], item[2], int(item[3])]
            jmlbrs += 1
        globalvars.refund_count = jmlbrs

    #Kritik dan Saran
    f_user=input('Masukkan nama File Kritik dan Saran: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #Masukkan data ke array global, catat jumlah data
        jmlbrs=0
        for item in csv_reader:
            globalvars.kritik_dan_saran[jmlbrs] = [item[0], item[1], item[2], item[3]]
            jmlbrs += 1
        globalvars.kritik_count = jmlbrs

    globalvars.loaded = True
    print()
    print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")
    print()
