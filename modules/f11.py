import modules.common as common
import modules.globalvars as globalvars

def sort_laporan():
    # Prosedur mengurutkan kritik_dan_saran berdasarkan ID secara alfabetis
    for Pass in range (globalvars.kritik_count-1):
        indexMin = Pass
        for i in range(Pass+1,globalvars.kritik_count):
            if globalvars.kritik_dan_saran[i][2]<globalvars.kritik_dan_saran[indexMin][2]:
                indexMin=i
        Temp=globalvars.kritik_dan_saran[indexMin]
        globalvars.kritik_dan_saran[indexMin]=globalvars.kritik_dan_saran[Pass]
        globalvars.kritik_dan_saran[Pass]=Temp
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
