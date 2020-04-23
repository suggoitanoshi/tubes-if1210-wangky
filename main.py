import modules.globalvars as globalvars
import modules.common as common

import modules.f01 as f01
import modules.f02 as f02
import modules.f03 as f03
import modules.f04 as f04
import modules.f05 as f05
import modules.f06 as f06
import modules.f07 as f07
import modules.f08 as f08
import modules.f09 as f09
import modules.f10 as f10
import modules.f11 as f11
import modules.f12 as f12
import modules.f13 as f13
import modules.f14 as f14
import modules.f15 as f15
import modules.f16 as f16

#import modules.b02 as b02
import modules.b03 as b03
import modules.b04 as b04

# Main Program variables
terminate = False
prompt = '$ '

# Main Loop
while not terminate:
  command = input(prompt)
  if command == 'load':
    f01.load()
  elif globalvars.loaded:
    if command == 'login':
      f04.login()
    elif common.has_login():
      if command == 'signup':
        f03.sign_up()
      elif command == 'cari_pemain':
        f05.cari_pemain()
      elif command == 'cari':
        f06.search_wahana()
      elif command == 'beli_tiket':
        f07.buy_ticket()
      elif command == 'main':
        f08.use_ticket()
      elif command == 'refund':
        f09.refund()
      elif command == 'kritik_saran':
        f10.kritik_saran()
      elif command == 'lihat_laporan':
        f11.lihat_laporan()
      elif command == 'tambah_wahana':
        f12.tambah_wahana()
      elif command == 'topup':
        f13.topup_saldo()
      elif command == 'riwayat_wahana':
        f14.riwayat_wahana()
      elif command == 'tiket_pemain':
        f15.tiket_pemain()
      elif command == 'exit':
        f16.exit()
        terminate = True
      elif command == 'best_wahana':
        b03.best_wahana()
      elif command == 'tiket_hilang':
        b04.tiket_hilang()
    else:
      print(globalvars.LOGIN_MESSAGE)
  elif command == 'save':
    f02.save()
  else:
    print(globalvars.NOT_LOADED)