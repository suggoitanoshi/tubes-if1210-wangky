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
  tinggi = globalvars.current_login[2]
  umur = 2020 - int(globalvars.current_login[1][6:])
  kondisi = (w[3] == 0) or (w[3] == 1 and umur > 17) or (w[3] == 2 and umur <= 17)
  kondisi = kondisi and ((w[4] and tinggi >= 170) or (not w[4]))
  return kondisi

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
      if(buy_amount*wahana[2] <= globalvars.current_login[6]):
        nama_wahana = wahana[1]
        username = globalvars.current_login[3]
        globalvars.current_login[6] -= wahana[2]
        globalvars.kepemilikan_count += 1
        globalvars.kepemilikan_tiket[globalvars.kepemilikan_count-1] =\
          [username,wahana[0], buy_amount]
        globalvars.pembelian_count += 1
        globalvars.pembelian_tiket[globalvars.pembelian_count-1] =\
          [username,current_tanggal,wahana[0],buy_amount]
        print('Selamat bersenang-senang di',nama_wahana)
      else:
        print(globalvars.NOT_ENOUGH_SALDO_MESSAGE)
    else:
      print(globalvars.CANNOT_PLAY_MESSAGE)