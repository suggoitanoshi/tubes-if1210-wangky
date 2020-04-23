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
        #hitung baris yang ada dalam file masukkan ke variabel jmlbrs
        jmlbrs=0
        for i in csv_reader:
            jmlbrs=jmlbrs+1
        #Replace semua isi Global Array dengan isi file
        globalvars.users_count = jmlbrs
        csv_file.seek(0)
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #membuat array untuk array global
        globalvars.users=[i for i in range (jmlbrs)]
        #memasukkan data ke array global
        for i in range (jmlbrs):
            a=next(csv_reader)
            isi=[a[0],a[1],int(a[2]),a[3],a[4],a[5],int(a[6])]
            globalvars.users[i]=isi

    #Daftar Wahana
    f_user=input('Masukkan nama File Daftar Wahana: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #hitung baris yang ada dalam file masukkan ke variabel jmlbrs
        jmlbrs=0
        for i in csv_reader:
            jmlbrs=jmlbrs+1
        #Replace semua isi Global Array dengan isi file
        globalvars.list_wahana_count = jmlbrs
        #baca isi file, masukkan ke variabel csv_reader
        csv_file.seek(0)
        #membuat array untuk array global
        globalvars.list_wahana=[i for i in range (jmlbrs)]
        #memasukkan data ke array global
        for i in range (jmlbrs):
            a=next(csv_reader)
            isi=[a[0],a[1],int(a[2]),int(a[3]),bool(a[4])]
            globalvars.list_wahana[i]=isi

    #Pembelian Tiket
    f_user=input('Masukkan nama File Pembelian Tiket: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #hitung baris yang ada dalam file masukkan ke variabel jmlbrs
        jmlbrs=0
        for i in csv_reader:
            jmlbrs=jmlbrs+1
        #Replace semua isi Global Array dengan isi file
        globalvars.pembelian_count = jmlbrs
        csv_file.seek(0)
        #baca isi file, masukkan ke variabel csv_reader        csv_reader = csv.reader(csv_file, delimiter=',')
        #membuat array untuk array global
        globalvars.pembelian_tiket=[i for i in range (jmlbrs)]
        #memasukkan data ke array global
        for i in range (jmlbrs):
            a=next(csv_reader)
            isi=[a[0],a[1],a[2],int(a[3])]
            globalvars.pembelian_tiket[i]=isi

    #Penggunaan Tiket
    f_user=input('Masukkan nama File Penggunaan Tiket: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #hitung baris yang ada dalam file masukkan ke variabel jmlbrs
        jmlbrs=0
        for i in csv_reader:
            jmlbrs=jmlbrs+1
        #Replace semua isi Global Array dengan isi file
        globalvars.penggunaan_count = jmlbrs
        csv_file.seek(0)
        #baca isi file, masukkan ke variabel csv_reader
        #membuat array untuk array global
        globalvars.penggunaan_tiket=[i for i in range (jmlbrs)]
        #memasukkan data ke array global
        for i in range (jmlbrs):
            a=next(csv_reader)
            isi=[a[0],a[1],a[2],int(a[3])]
            globalvars.penggunaan_tiket[i]=isi

    #Kepemilikan Tiket
    f_user=input('Masukkan nama File Kepemilikan Tiket: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #hitung baris yang ada dalam file masukkan ke variabel jmlbrs
        jmlbrs=0
        for i in csv_reader:
            jmlbrs=jmlbrs+1
        #Replace semua isi Global Array dengan isi file
        globalvars.kepemilikan_count = jmlbrs
        #baca isi file, masukkan ke variabel csv_reader
        csv_file.seek(0)
        #membuat array untuk array global
        globalvars.kepemilikan_tiket=[i for i in range (jmlbrs)]
        #memasukkan data ke array global
        for i in range (jmlbrs):
            a=next(csv_reader)
            isi=[a[0],a[1],int(a[2])]
            globalvars.kepemilikan_tiket[i]=isi

    #Refund Tiket
    f_user=input('Masukkan nama File Refund Tiket: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #hitung baris yang ada dalam file masukkan ke variabel jmlbrs
        jmlbrs=0
        for i in csv_reader:
            jmlbrs=jmlbrs+1
        #Replace semua isi Global Array dengan isi file
        globalvars.refund_count = jmlbrs
        csv_file.seek(0)
        #baca isi file, masukkan ke variabel csv_reader
        #membuat array untuk array global
        globalvars.refund_tiket=[i for i in range (jmlbrs)]
        #memasukkan data ke array global
        for i in range (jmlbrs):
            a=next(csv_reader)
            isi=[a[0],a[1],a[2],int(a[3])]
            globalvars.refund_tiket[i]=isi

    #Kritik dan Saran
    f_user=input('Masukkan nama File Kritik dan Saran: ')    
    with open('external_files/'+f_user) as csv_file:
        #baca isi file, masukkan ke variabel csv_reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        #hitung baris yang ada dalam file masukkan ke variabel jmlbrs
        jmlbrs=0
        for i in csv_reader:
            jmlbrs=jmlbrs+1
        #Replace semua isi Global Array dengan isi file
        globalvars.kritik_count = jmlbrs
        csv_file.seek(0)
        #baca isi file, masukkan ke variabel csv_reader
        #membuat array untuk array global
        globalvars.kritik_dan_saran=[i for i in range (jmlbrs)]
        #memasukkan data ke array global
        for i in range (jmlbrs):
            a=next(csv_reader)
            isi=[a[0],a[1],a[2],a[3]]
            globalvars.kritik_dan_saran[i]=isi

    print()
    print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")
    print()
