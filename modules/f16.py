import modules.common as common
import modules.globalvars as globalvars

def exit():
    is_Exit=input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")
    if is_Exit=="Y":
        save()
    
