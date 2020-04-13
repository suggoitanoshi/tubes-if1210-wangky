import modules.globalvars as globalvars

import modules.f06 as f06
import modules.f07 as f07
import modules.f08 as f08

# Main Program variables
terminate = False
prompt = '$ '

# Main Loop
while not terminate:
  command = input(prompt)
  if command == 'cari':
    f06.search_wahana()
  if command == 'beli_tiket':
    f07.buy_ticket()
  if command == 'main':
    f08.use_ticket()
  if command == 'exit':
    # TODO: add save prompt
    terminate = True
  # TODO: add basic commands