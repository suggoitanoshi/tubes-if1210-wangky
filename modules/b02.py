import modules.globalvars as globalvars
import modules.common as common

# B02 - Golden Account

def upgrade_gold():
    """Program melakukan upgrade kepada sebuah akun sehingga mendapat
    potongan harga setiap wahana menjadi setengahnya
    ---
    Parameter : -
    Output : Pesan berhasil upgrade account
    ---
    """
    if common.is_admin():
        upgrade_user = input("Masukkan username yang ingin di-upgrade: ")

        user_found = False
        i = 0
        while not user_found and  i < globalvars.users_count:
            if upgrade_user == globalvars.users[i][3]:
                user_found = True
                globalvars.users[i][7] = "gold"
                print("Akun Anda telah di-upgrade.")
            else:
                i+= 1
        if not user_found:
            print(upgrade_user, "tidak terdaftar dalam sistem kami, Silahkan Sign Up terlebih dahulu")
    else:
        print(globalvars.NOT_ADMIN_MESSAGE)
