import modules.globalvars as globalvars
# F15 - Melihat Jumlah Tiket Pemain

# KAMUS

def tiket_pemain():
  """[program fungsi]
  ---
  Parameter : -
  Output : 
  ---
  """
  input_user = input("Masukkan username: ")
  tiket_user = [['','',0] for _ in range(globalvars.list_wahana_count)]
  tiket_user_count = 0
  i = 0
  while i < globalvars.pembelian_count:
    current = globalvars.pembelian_tiket[i]
    if current[0] == input_user:
      j = 0
      found = False
      while not found and j < tiket_user_count:
        if tiket_user[j][0] == current[2]:
          found = True
          tiket_user[j][2] += current[3]
      if not found:
        j = 0
        wahana_found = False
        wahana_name = ''
        while not wahana_found and j < globalvars.list_wahana_count:
          if globalvars.list_wahana[j][0] == current[2]:
            wahana_name = globalvars.list_wahana[j][1]
            wahana_found = True
          else:
            j += 1
        tiket_user[tiket_user_count] = [current[2], wahana_name, current[3]]
        tiket_user_count += 1
    
  print("Riwayat: ")
  for i in range(tiket_user_count):
    print('%s|%s|%d' % (tiket_user[i][0], tiket_user[i][1], tiket_user[i][2]))