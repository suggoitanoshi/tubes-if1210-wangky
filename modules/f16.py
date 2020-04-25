import modules.common as common
import modules.globalvars as globalvars
import modules.f03 as f03

def exit():
    is_Exit=input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")
    if is_Exit=="Y" or is_Exit == 'y':
        f03.save()
    
