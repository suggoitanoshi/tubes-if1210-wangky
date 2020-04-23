import modules.globalvars as globalvars

# F02 - Login User

# KAMUS

def login():
    """[program fungsi]
    ---
    Parameter : -
    Output : Pesan sukses/ gagal login, akun sudah dapat bermain 
    ---
    """
    input_user = input("Masukkan username: ")
    input_pass = input("Masukkan password: ")
    
    user_found = False
    user_name = ''
    i = 0
    while not user_found and i < globalvars.users_count:
        if input_user == globalvars.users[i][3] and input_pass == globalvars.users[i][4]:
            globalvars.current_login = globalvars.users[i]
            user_name = globalvars.current_login[0]
            user_found = True
            print("Selamat bersenang-senang,", user_name,"!")
        else: i += 1
    if not user_found:
        print(globalvars.FAIL_LOGIN)