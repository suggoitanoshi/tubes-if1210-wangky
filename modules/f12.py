#F12 - Menambahkan Wahana Baru

import modules.globalvars as globalvars

#KAMUS

def tambah_wahana():
    baru=['*','*',0,0,False]
    print('Masukkan Informasi Wahana yang ditambahkan:')
    baru[0]=str(input('Masukkan ID Wahana: '))
    baru[1]=str(input('Masukkan Nama Wahana: '))
    baru[2]=int(input('Masukkan Harga Tiket: '))
    baru[3]=input('Batasan Umur: ')
    baru[4]=input('Batasan Tinggi Badan: ')

    #mengganti format jawaban dari batas umur jika input string
    if(baru[3]=='Semua umur'):
        baru[3]=0
    elif(baru[3]=='Anak-anak'):
        baru[3]=1
    elif(baru[3]=='Dewasa'):
        baru[3]=2
    else:
        baru[3]=baru[3]
        #tidak berubah/format dianggap sudah menggunakan angka

    #mengganti format jawaban dari batas tinggi jika input string
    if(baru[4]=='>= 170cm'):
        baru[4]=True
    elif(baru[4]=='tanpa batasan'):
        baru[4]=False
    else:
        baru[4]=baru[4]
        #tidak berubah/format dianggap sudah menggunakan Boolean
    copy=[0 for i in range(globalvars.list_wahana_count+1)]
    for i in range (globalvars.list_wahana_count):
        copy[i]=globalvars.list_wahana[i]
    copy[globalvars.list_wahana_count]=baru
    globalvars.list_wahana=copy
    globalvars.list_wahana_count=globalvars.list_wahana_count+1
    print()
    print('Info Wahana telah ditambahkan')
    print()
