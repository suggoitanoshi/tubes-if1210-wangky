import modules.globalvars as globalvars

"""Common function used by program"""

def has_login():
  """Menentukan apakah pengguna sudah login dalam sesi ini"""
  return globalvars.current_login[2] != '' 
def is_player():
  """Menentukan apakah pengguna yang login adalah player atau bukan"""
  return globalvars.current_login[4] == 'Pemain'
