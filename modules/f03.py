import modules.globalvars as globalvars

# F04 - Sign Up User

# KAMUS

def sign_up():
    """[program fungsi]
    ---
    Parameter : -
    Output : 
    ---
    """
    input_nama = input("Masukkan nama pemain: ")
    input_ttl = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
    input_tinggi = input("Masukkan tinggi badan pemain (cm): ")
    input_user = input("Masukkan username pemain: ")
    input_pass = input("Masukkan password pemain: ")
    print()

    globalvars.users[globalvars.users_count] = [input_nama,input_ttl,int(input_tinggi),input_user,input_pass,'Pemain',0]
    globalvars.users_count += 1
    
    print("Selamat menjadi pemain, " + input_nama + ". Selamat bermain.")