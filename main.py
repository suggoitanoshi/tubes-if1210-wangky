LOGIN_MESSAGE = 'Anda belum login. Silahkan login dulu!'
NOT_PLAYER_MESSAGE = 'Anda bukan pemain, tidak bisa membeli tiket.'

current_username = ''
current_role = ''

# Common functions
def has_login():
  """Menentukan apakah pengguna sudah login dalam sesi ini"""
  return current_username != ''
def is_player():
  """Menentukan apakah pengguna yang login adalah player atau bukan"""
  return current_role == 'Pemain'
def wahana_exists(wahana_id):
  """Menentukan apakah wahana ada di database
  Parameters:
  ---
  wahana_id: string
  ID Wahana yang akan dicek
  Return: bool
  ---
  True jika ada, False jika tidak
  """
  # TODO: buat implementasi
  return True
def has_enough_tickets(wahana_id):
  """Menentukan apakah pemain memiliki tiket cukup untuk bermain di wahana
  Parameters:
  ---
  wahana_id: string
    ID Wahana yang akan dimainkan
  Return: bool
  ---
  True jika cukup, False jika tidak
  """
  # TODO: buat implementasi
  return True
def can_play():
  """Menentukan apakah pengguna dapat bermain di wahana"""
  # TODO: buat implementasi berdasarkan struktur data wahana di memori
  return True
def filter_umur(f):
  """Mengembalikan wahana yang difilter berdasarkan umur
  
  Parameters:
  ----------
  f: int
    Filter umur yang digunakan
    0: Semua umur
    1: Anak-anak
    2: Dewasa
  Return
  ---
  wahana yang sudah difilter
  """
  # TODO: buat implementasi berdasarkan struktur data wahana di memori
  pass
def filter_tinggi(f):
  """Mengembalikan wahana yang difilter berdasarkan tinggi
  Parameters:
  ---
  f: bool
    Filter tinggi yang digunakan
    true: tinggi >= 170cm
    false: semua tinggi
  Return
  ---
  wahana yang sudah difilter
  """
  # TODO: buat implementasi berdasarkan struktur data wahana di memori
  # mengembalikan 
  pass

# Procedure implementations
def search_wahana():
  """Mencari wahana di memori sesuai ketentuan"""
  pass
def buy_ticket():
  """Fungsi beli tiket untuk pemain"""
  if not has_login():
    print(LOGIN_MESSAGE)
  elif not is_player():
    print(NOT_PLAYER_MESSAGE)
  else:
    current_id_wahana = input('Masukkan ID Wahana: ')
    current_tanggal = input('Masukkan Tanggal hari ini: ')
    buy_amount = int(input('Jumlah tiket yang dibeli: '))
    if can_play():
      nama_wahana = '' # TODO: cari wahana
      # TODO: tambah jumlah tiket pengguna di memori
      print('Selamat bersenang-senang di',nama_wahana)
    else:
      print('''Anda tidak memenuhi persyaratan untuk memainkan wahana ini.
      Silakan menggunakan wahana lain yang tersedia.''')

def use_ticket():
  # TODO: actual implementation
  pass

# Main Program variables
terminate = False
prompt = '$ '
# Main Loop
while not terminate:
  command = input(prompt)
  if command == 'cari':
    search_wahana()
  if command == 'beli_tiket':
    buy_ticket()
  if command == 'main':
    use_ticket()
  # TODO: add basic commands
  # TODO: add exit command (important!)