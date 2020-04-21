import modules.globalvars as globalvars

def sort_wahana_by_ticket():
  """Mengurutkan wahana berdasarkan jumlah tiket terjual
  Return: [[string, string, int]]
  ---
  Wahana yang sudah disort
  """
  ret = [[globalvars.list_wahana[i][0],globalvars.list_wahana[i][1],0]
         for i in range(globalvars.list_wahana_count)]
  # Transformasi menjadi array of [string, string, int]
  for i in range(globalvars.penggunaan_count):
    cid = globalvars.penggunaan_tiket[i][2] # ID Wahana
    n = globalvars.penggunaan_tiket[i][3] # Jumlah tiket
    # Mencari elemen wahana yang sesuai, karena unsorted.
    found = False
    j = 0
    while not found and j < globalvars.list_wahana_count:
      if ret[i][0] == cid:
        ret[i][2] += n
        found = True
      else: j += 1
  # Sorting (Insertion)
  for i in range(1, globalvars.list_wahana_count):
    curr = ret[i]
    j = i-1
    while j >= 0 and ret[j][2] > curr[2]:
      ret[j+1] = ret[j]
      j -= 1
    ret[j] = curr
  return ret

def get_top_3_wahana():
  """Mengambil 3 wahana teratas dari list wahana yang sudah disort
  Return [[string, string, int]]
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