import modules.common as common
import modules.globalvars as globalvars

def can_play(w):
  """Menentukan apakah pengguna dapat bermain di wahana
  Parameter
  ---
  w: wahana
  Return
  ---
  Pemain bisa bermain/tidak di wahana tersebut
  """
  tinggi = 0
  umur = 0
  # TODO: tambah field tinggi di user?
  # tinggi = globalvars.users[i][x]
  umur = 2020 - int(globalvars.current_login[1][6:])
  return (w[3] == 0) or (w[3] == 1 and umur <= 17) or (w[3] == 2 and umur > 17)

def search_wahana(id):
  """Fungsi mencari wahana berdasarkan ID
  Parameters:
  ---
  id: string
    ID_Wahana yang akan dicari
  Return:
  ---
  wahana
    wahana yang dicari
  """
  wahana = globalvars.list_wahana_default
  wahana_found = False
  i = 0
  while not wahana_found and i < globalvars.list_wahana_count:
    if globalvars.list_wahana[i][0] == id:
      wahana_found = True
      wahana = globalvars.list_wahana[i]
    else:
      i += 1
  return wahana

def buy_ticket():
  """Prosedur beli tiket untuk pemain"""
  if not common.has_login():
    print(globalvars.LOGIN_MESSAGE)
  elif not common.is_player():
    print(globalvars.NOT_PLAYER_MESSAGE)
  else:
    current_id_wahana = input('Masukkan ID Wahana: ')
    current_tanggal = input('Masukkan Tanggal hari ini: ')
    buy_amount = int(input('Jumlah tiket yang dibeli: '))
    wahana = search_wahana(current_id_wahana)
    if can_play(wahana):
      if(buy_amount*wahana[2] <= globalvars.current_login[5]):
        nama_wahana = wahana[1]
        # TODO: tambah jumlah tiket pengguna di memori
        print('Selamat bersenang-senang di',nama_wahana)
      else:
        print(globalvars.NOT_ENOUGH_SALDO_MESSAGE)
    else:
      print(globalvars.CANNOT_PLAY_MESSAGE)