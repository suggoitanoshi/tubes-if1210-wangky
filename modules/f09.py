import modules.common as common
import modules.globalvars as globalvars

def check_ticket(id,jml):
    '''Fungsi memeriksa kepemilikan tiket berdasarkan ID
    Parameters:
    ---
    id: string
         ID_Wahana akan dicari
    jml: integer
         Jumlah tiket yang ingin direfund user
    Return:
    ---
    True jika jumlah ticket yang dimiliki lebih dari sama dengan tiket yang ingin direfund
    '''
    i = 0
    while i < globalvars.kepemilikan_count:
        if globalvars.kepemilikan_tiket[i][0] == globalvars.current_login[2] and globalvars.kepemilikan_tiket[i][1] == id:
            if globalvars.kepemilikan_tiket[i][2]>= jml:
                return True
            else:
                return False
        else:
            i+=1
    return False

def refund():
    # Prosedur mengembalikan uang
    # Asumsikan semua input dari user sudah valid
    # Uang yang dikembalikan hanya 50% harga tiket semula
    if not common.has_login():
        print(globalvars.LOGIN_MESSAGE)
    elif not common.is_player():
        print(globalvars.NOT_PLAYER_MESSAGE)
    else:
        current_id_wahana = input('Masukkan ID Wahana: ')
        current_tanggal = input('Masukkan Tanggal Refund: ')
        refund_amount = int(input('Jumlah tiket yang di-refund: '))
        if check_ticket(current_id_wahana, refund_amount) :
            # Update saldo
            j = 0
            wahanaFound = False
            while not wahanaFound and j < globalvars.list_wahana_count:
                if current_id_wahana == globalvars.list_wahana[j][0]:
                    wahanaFound = True
                else: j += 1
            globalvars.current_login[5]+=0.5*refund_amount*globalvars.list_wahana[j][2]
            # Update data kepemilikan
            i=0
            while i<globalvars.kepemilikan_count:
                if globalvars.kepemilikan_tiket[i][0] == globalvars.current_login[2]:
                    globalvars.kepemilikan_tiket[i][2]-=refund_amount
                else:
                    i+=1
            # Masukkan data refund ke array
            # Asumsikan ada array sementara dengan indeks lebih 1 dari array sebelumnya
            # Array tersebut dapat diinisialisasi dalam Temp
            Temp = [0 for i in range(globalvars.refund_count+1)]
            for i in range(globalvars.refund_count):
                Temp[i]=globalvars.refund_tiket[i]
            Temp[globalvars.refund_count]=(globalvars.current_login[2],current_tanggal,current_id_wahana,refund_amount)
            globalvars.refund_tiket=Temp
            globalvars.refund_count+=1
            # Setelah uang dikembalikan ke saldo dan update pada database
            print("Uang refund sudah kami berikan pada akun Anda.")
        else:
            print("Anda tidak memiliki tiket terkait.")
        
