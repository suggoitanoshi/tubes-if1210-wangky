import modules.common as common
import modules.globalvars as globalvars

def sort_laporan():
    # Prosedur mengurutkan kritik_dan_saran berdasarkan ID secara alfabetis
    Temp=[0 for i in range(globalvars.kritik_count)]
    Max=globalvars.kritik_dan_saran[0][2]
    for i in range(globalvars.kritik_count):
        # String dapat diurutkan layaknya bilangan dengan operator berdasarkan urutannya dari A-Z
        if globalvars.kritik_dan_saran[i][2]<Max:
            Temp[i]=globalvars.kritik_dan_saran[i]
        else:
            Max=globalvars.kritik_count[1][2]
    globalvars.kritik_dan_saran=Temp
    return

def lihat_laporan():
    # Prosedur untuk admin yang ingin melihat kritik dan saran
    if not common.has_login():
        print(globalvars.LOGIN_MESSAGE)
    elif common.is_player():
        print("Anda bukan admin, tidak bisa melihat laporan.")
    else:
        sort_laporan()
        print("Kritik dan saran:")
        for i in range(globalvars.kritik_count):
            print(globalvars.kritik_dan_saran[i][2]+" | "+globalvars.kritik_dan_saran[i][1]+" | "+globalvars.kritik_dan_saran[i][0]+" | "+globalvars.kritik_dan_saran[i][3])
