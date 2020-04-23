import modules.globalvars as globalvars

def filter_umur(w, n, f):
  """Mengembalikan wahana yang difilter berdasarkan umur
  
  Parameters:
  ----------
  w: list wahana [(ID_Wahana, Nama_Wahana, Harga_Tiket, Batasan_Umur, Batasan_Tinggi)]
    list wahana yang akan difilter
  n: int
    jumlah wahana masukan
  f: int
    Filter umur yang digunakan
    0: Semua umur
    1: Dewasa
    2: Anak-anak
  Return: (fw, fn)
  ---
  fw: wahana
    wahana yang sudah difilter
  fn: int
    jumlah wahana yang terfilter
  """
  fw = [globalvars.list_wahana_default for _ in range(n)]
  fn = 0
  for i in range(n):
    if w[i][3] == f:
      fw[fn] = w[i]
      fn += 1
  return (fw, fn)

def filter_tinggi(w, n, f):
  """Mengembalikan wahana yang difilter berdasarkan tinggi
  Parameters:
  ---
  w: list wahana [(ID_Wahana, Nama_Wahana, Harga_Tiket, Batasan_Umur, Batasan_Tinggi)]
  n: int
    jumlah wahana yang akan difilter
  f: bool
    Filter tinggi yang digunakan
    true: tinggi >= 170cm
    false: semua tinggi
  Return: (fw, fn)
  ---
  fw: wahana
    wahana yang sudah difilter
  fn: int
    jumlah wahana yang terfilter
  """
  fw = [globalvars.list_wahana_default for _ in range(n)]
  fn = 0
  for i in range(n):
    if (w[i][4] and f):
      fw[fn] = w[i]
      fn += 1
  return (fw, fn)

def search_wahana():
  """Mencari wahana di memori sesuai ketentuan"""
  print('Jenis batasan umur:')
  print('1. Anak-anak (<17 tahun)')
  print('2. Dewasa (>=17 tahun)')
  print('3. Semua umur')
  print('')
  print('Jenis batasan tinggi badan:')
  print('1. Lebih dari 170 cm')
  print('2. Tanpa batasan')
  print('')
  batasan_umur = int(input('Batasan umur pemain: '))
  batasan_tinggi = int(input('Batasan tinggi badan: '))

  fumur = (3-batasan_umur)
  ftinggi = True if batasan_tinggi == 1 else False

  (hasil_filter, n) = filter_umur(globalvars.list_wahana, globalvars.list_wahana_count, fumur)
  (hasil_filter, n) = filter_tinggi(hasil_filter, n, ftinggi)

  print('Hasil pencarian:')
  for i in range(n):
    print('%s | %s | %d' %(hasil_filter[i][0], hasil_filter[i][1], hasil_filter[i][2]))