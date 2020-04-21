import modules.globalvars as globalvars
import modules.common as common
def get_initial_saldo(user):
  """Mendapatkan saldo awal pengguna
  Parameter
  ---
  user: user [string, string, int, string, string, string, int]
    user yang akan ditopup saldonya
  Return: int
  ---
  Saldo awal pengguna
  """
  
  return user[6]

def topup_saldo():
  """Prosedur top up saldo"""
  username = input('Masukkan username: ')
  topup = int(input('Masukkan saldo yang di-top up: '))
  found = False
  i = 0
  user = globalvars.users_default
  while not found and i < globalvars.users_count:
    if globalvars.users[i][3] == username:
      found = True
      user = globalvars.users[i]
    else: i += 1
  if found:
    user[6] = get_initial_saldo(user) + topup
    print('Topup berhasil. Saldo %s bertambah menjadi %d' % (user[1], user[6]))
  else:
    print('User tidak ditemukan.')

