import modules.globalvars as globalvars

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
  i = 0
  wahana_found = False
  while not wahana_found and i < globalvars.list_wahana_count:
    if globalvars.list_wahana[i][0] == wahana_id: wahana_found = True
    else: i += 1
  return wahana_found

def has_enough_tickets(wahana_id, jml_tiket):
  """Menentukan apakah pemain memiliki tiket cukup untuk bermain di wahana
  Parameters:
  ---
  wahana_id: string
    ID Wahana yang akan dimainkan
  jml_tiket: int
    Jumlah tiket yang digunakan
  Return: bool
  ---
  True jika cukup, False jika tidak
  """
  i = 0
  has_ticket = 0
  enough_ticket = False
  found = False
  while not found and i < globalvars.kepemilikan_count:
    if globalvars.kepemilikan_tiket[i][0] == globalvars.current_login[3] and\
      globalvars.kepemilikan_tiket[i][1] == wahana_id:
        found = True
        has_ticket = globalvars.kepemilikan_tiket[i][2]
  found = False
  i = 0
  enough_ticket = has_ticket >= jml_tiket
  return enough_ticket

def use_ticket():
  id_wahana = input('Masukkan ID Wahana: ')
  tggl_skrg = input('Masukkan tanggal hari ini: ')
  jml_tiket = int(input('Jumlah tiket yang digunakan: '))
  if wahana_exists(id_wahana) and has_enough_tickets(id_wahana, jml_tiket):
    globalvars.penggunaan_tiket[globalvars.penggunaan_count] =\
      [globalvars.current_login[3], tggl_skrg, id_wahana, jml_tiket]
    globalvars.penggunaan_count += 1
    kepemilikan_found = False
    i = 0
    while not kepemilikan_found and i < globalvars.kepemilikan_count:
      curr = globalvars.kepemilikan_tiket[i]
      if curr[0] == globalvars.current_login[3] and curr[1] == id_wahana:
        globalvars.kepemilikan_tiket[i][2] -= jml_tiket
        kepemilikan_found = True
      else: i+=1
    print('Terimakasih telah bermain.')
  else:
    print(globalvars.NOT_VALID_TICKET_ERROR)
  pass