import modules.common as common
import modules.globalvars as globalvars

def kritik_saran():
    #Prosedur menerima kritik dan saran
    current_id_wahana = input('Masukkan ID Wahana: ')
    current_tanggal = input('Masukkan tanggal pelaporan: ')
    report = input('Kritik/saran Anda: ')
    # Update ke database kritik_dan_saran
    # Asumsikan ada array sementara dengan indeks lebih 1 dari array sebelumnya
    # Array tersebut dapat diinisialisasi dalam Temp
    Temp = [0 for i in range(globalvars.kritik_count+1)]
    for i in range(globalvars.kritik_count):
        Temp[i]=globalvars.kritik_dan_saran[i]
    Temp[globalvars.kritik_count]=(globalvars.current_login[2],current_tanggal,current_id_wahana,report)
    globalvars.kritik_dan_saran=Temp
    # Setelah laporan diterima dan update pada database
    print("Kritik dan saran Anda kami terima.")
