import modules.globalvars as globalvars

def sort_wahana_by_ticket():
  """Mengurutkan wahana berdasarkan jumlah tiket terjual
  Return: (string, string, int)
  ---
  Wahana yang sudah disort
  """
  # TODO: transformasi list wahana menjadi tuple seperti pada return
  # TODO: implementasi sorting
  # TODO: keluarkan tuple sesuai spek

def get_top_3_wahana():
  """Mengambil 3 wahana teratas dari list wahana yang sudah disort
  Return
  ---
  3 Wahana sebagai list
  """
  return sort_wahana_by_ticket()[:3]

def best_wahana():
  """Prosedur best wahana"""
  # TODO: implementasi
  top_3 = get_top_3_wahana()
  for i in range(3):
    print('%d | %s | %s | %d' % (i+1,top_3[i][0], top_3[i][1], top_3[i][2]))