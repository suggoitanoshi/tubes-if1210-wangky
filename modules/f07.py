import modules.common as common
import modules.globalvars as globalvars

def can_play():
  """Menentukan apakah pengguna dapat bermain di wahana"""
  # TODO: buat implementasi berdasarkan struktur data wahana di memori
  return True

def buy_ticket():
  """Fungsi beli tiket untuk pemain"""
  if not common.has_login():
    print(globalvars.LOGIN_MESSAGE)
  elif not common.is_player():
    print(globalvars.NOT_PLAYER_MESSAGE)
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