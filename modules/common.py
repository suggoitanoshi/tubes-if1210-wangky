import modules.globalvars as globalvars

"""Common function used by program"""

def has_login():
  """Menentukan apakah pengguna sudah login dalam sesi ini"""
  return globalvars.current_login[3] != '' 
def is_player():
  """Menentukan apakah pengguna yang login adalah player atau bukan"""
  return globalvars.current_login[5] == 'Pemain'
def is_admin():
  """Menentukan apakah pengguna yang login adalah admin atau bukan"""
  return globalvars.current_login[5] == 'Admin'
