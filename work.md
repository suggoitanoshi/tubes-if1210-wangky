# Fitur dan Implementasinya
## Checklist Kerjaan:
| Fitur | Sudah? | Desainer | Coder | Keterangan Tambahan |
|-------|--------|----------|-------|---------------------|
| F01 - Load | - | 16519047 | 16519047 | - |
| F02 - Save | - | 16519047 | 16519047 | - |
| F03 - Sign up | - | 16519447 | 16519447 | - |
| F04 - Login | - | 16519447 | 16519447 | - |
| F05 - Cari Pemain | - | 16519447 | 16519447 | - |
| F06 - Cari Wahana | - | 16519187 | 16519187 | - |
| F07 - Beli Tiket | - | 16519187 | 16519187 | - |
| F08 - Pakai Tiket | - | 16519187 | 16519187 | - |
| F09 - Refund | - | 16519317 | 16519317 | - |
| F10 - Krisar | - | 16519317 | 16519317 | - |
| F11 - Lihat Krisar | - | 16519317 | 16519317 | - |
| F12 - Tambah Wahana | - | 16519047 | 16519047 | - |
| F13 - Topup Saldo | - |16519187 | 16519187| - |
| F14 - Riwayat | - | 16519047| 16519047 | - |
| F15 - Lihat tiket | - | 16519447 | 16519447 | - |
| F16 - Exit | - | 16519317 | 16519317 | - |
| B01 - Password | - | 16519047 | 16519047 | - |
| B02 - Golden Account | - | 16519447 | 16519447 | - |
| B03 - Best Wahana | - | 16519187 | 16519187 | - |
| B04 - Kehilangan Tiket | - | 16519317 | 16519317 | - |

## Implementasi Fitur
### F01 - Load
- procedure load_file
### F02 - Save
- procedure save_file
### F03 - Sign up
- procedure sign_up
### F04 - Login
- procedure login
### F05 - Cari Pemain
- procedure search_player
### F06 - Cari Wahana
- function filter_umur
- function filter_tinggi
- procedure search_wahana
### F07 - Beli Tiket
- function has_login
- function is_player
- function search_wahana
- function can_play
- procedure buy_ticket
### F08 - Pakai Tiket
- function has_login
- function is_player
- function has_enough_ticket
- function wahana_exists
- procedure use_ticket
### F09 - Refund
- procedure refund
- function has_login
- function valid_ticket
### F10 - Krisar
- procedure report
### F11 - Lihat Krisar
- procedure sort_id
- procedure see_report
### F12 - Tambah Wahana
- procedure add_wahana
### F13 - Topup Saldo
- function is_admin
- function get_initial_saldo
- procedure topup_saldo
### F14 - Riwayat
- function is_admin
- procedure display_wahana_history
### F15 - Lihat Tiket
- procedure player_ticket
### F16 - Exit
- procedure exit
### B01 - Password
- function hash_password
### B02 - Golden Account
- function is_gold
### B03 - Best Wahana
- function sort_wahana_by_ticket
- function get_top_3_wahana
- procedure best_wahana
### B04 - Kehilangan Tiket
- procedure lost_ticket
- function is_lost