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
    
    # masukin fungsi untuk nambahin data ke array
    print("Selamat menjadi pemain, " + input_nama + ". Selamat bermain.")