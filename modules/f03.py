import modules.globalvars as globalvars
import modules.b01 as b01

# F04 - Sign Up User

def sign_up():
    """Program dilakukan oleh admin untuk menambah data pengguna baru
    ---
    Parameter : -
    Output : Penambahan data pada database
    ---
    """
    input_nama = input("Masukkan nama pemain: ")
    input_ttl = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
    input_tinggi = input("Masukkan tinggi badan pemain (cm): ")
    input_user = input("Masukkan username pemain: ")
    input_pass = input("Masukkan password pemain: ")
    print()

    hashed_pass = b01.hashpassword(input_pass)

    globalvars.users[globalvars.users_count] = [input_nama,input_ttl,int(input_tinggi),input_user,hashed_pass,'Pemain',0,'default']
    globalvars.users_count += 1

    print("Selamat menjadi pemain, " + input_nama + ". Selamat bermain.")
