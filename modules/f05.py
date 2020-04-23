import modules.globalvars as globalvars
import modules.common as common

# F05 - Pencarian Pemain

# KAMUS

def cari_pemain():
    """[program fungsi]
    ---
    Parameter : -
    Output : 
    ---
    """
    if common.is_admin():
        input_user = input("Masukkan username: ")
        input_nama = input("Masukkan nama: ")
        input_tinggi = input("Tinggi Pemain: ")
        input_ttl = input("Tanggal Lahir Pemain: ")

        user_found = False
        i = 0
        while not user_found and  i < globalvars.users_count:
            if input_user == globalvars.users[i][3] and input_nama == globalvars.users[i][0] and\
            input_tinggi == globalvars.users[i][2] and input_ttl == globalvars.users[i][1]:
                user_found = True 
                print(input_nama, "telah terdaftar sebagai pemain, Silahkan Login dan Selamat Bermain.")
            else:
                i+= 1
        if not user_found:
            print(input_nama, "tidak terdaftar dalam sistem kami, Silahkan Sign Up terlebih dahulu")
    else:
        print(globalvars.NOT_ADMIN_MESSAGE)