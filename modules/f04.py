import modules.globalvars as globalvars
import modules.b01 as b01
import modules.common as common

# F04 - Sign Up User

def sign_up():
    """Program dilakukan oleh admin untuk menambah data pengguna baru
    ---
    Parameter : -
    Output : Penambahan data pada database
    ---
    """
    if common.is_admin():
        input_nama = input("Masukkan nama pemain: ")
        input_ttl = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
        input_tinggi = input("Masukkan tinggi badan pemain (cm): ")
        input_user = input("Masukkan username pemain: ")
        input_pass = input("Masukkan password pemain: ")
        print()

        hashed_pass = b01.hashpassword(input_pass)

        user_found = False
        i = 0
        while not user_found and  i < globalvars.users_count:
            if input_user == globalvars.users[i][3]:
                user_found = True
                print(input_nama, "telah terdaftar sebagai pemain, Silahkan Login dan Selamat Bermain.")
            else: i+=1

        if user_found == False:
            globalvars.users[globalvars.users_count] = [input_nama,input_ttl,int(input_tinggi),input_user,hashed_pass,'Pemain',0,'default']
            globalvars.users_count += 1

            print("Selamat menjadi pemain, " + input_nama + ". Selamat bermain.")
    else:
        print(globalvars.NOT_ADMIN_MESSAGE)
