import modules.common as common
import modules.globalvars as globalvars

def tiket_hilang():
'''Prosedur untuk menerima laporan tiket yang hilang kemudian
   mengurangi jumlah kepemilikan tiket sesuai jumlah tiket yang hilang'''
    if not common.has_login():
        print(globalvars.LOGIN_MESSAGE)
    elif not common.is_player():
        print(globalvars.NOT_PLAYER_MESSAGE)
    else:
        current_username = input("Masukkan username: ")
        current_tanggal = input('Tanggal kehilangan tiket: ')
        current_id_wahana = input('ID wahana: ')
        lost_count = input('Jumlah tiket yang dihilangkan: ')
        #Mengurangi kepemilikan tiket sesuai dengan jumlah tiket yang hilang
        i = 0
        #Mencari username yang kehilangan tiket dan tiket untuk wahana apa
        while i < globalvars.list_kepemilikan_count:
            if globalvars.kepemilikan_tiket[i][0] == current_username and globalvars.kepemilikan_tiket[i][1] == current_id_wahana:
                globalvars.kepemilikan_tiket[i][2]-=lost_count
            else:
                i+=1
        # Untuk update database kehilangan_tiket
        # Asumsikan ada array sementara dengan indeks lebih 1 dari array sebelumnya
        # Array tersebut dapat diinisialisasi dalam Temp
        Temp = [0 for i in range(globalvars.kehilangan_count+1)]
        for i in range(globalvars.kehilangan_count):
            Temp[i]=globalvars.kehilangan_tiket[i]
        Temp[globalvars.kehilangan_count]=(current_username,current_tanggal,current_id_wahana,lost_count)
        globalvars.kehilangan_tiket=Temp
        # Setelah laporan diterima dan update pada database
        print("Laporan kehilangan tiket Anda telah direkam.")


