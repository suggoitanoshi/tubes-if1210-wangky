"""Global Variables used by program"""
# Database stuff
# kepemilikan_tiket: Array of pemilik_tiket (Username, ID_Wahana, Jumlah_Tiket)
kepemilikan_tiket = []
kepemilikan_default = ['','',0]
kepemilikan_count = 0
# kritik_dan_saran: Array of kritik (Username, Tanggal_Kritik, ID_Wahana, Isi_Kritik)
kritik_dan_saran = []
kritik_default = ['','','','']
kritik_count = 0
# pembelian_tiket: Array of beli_tiket (Username, Tanggal_Pembelian, ID_Wahana, Jumlah_Tiket)
pembelian_tiket = []
pembelian_default = ['','','',0]
pembelian_count = 0
# penggunaan_tiket: Array of pengguna_tiket (Username, Tanggal_Penggunaan, ID_Wahana, Jumlah_Tiket)
penggunaan_tiket = []
penggunaan_default = ['','','',0]
penggunaan_count = 0
# refund_tiket: Array of refund (Username, Tanggal_Refund, ID_Wahana, Jumlah_Tiket)
refund_tiket = []
refund_default = ['','','',0]
refund_count = 0
# users: Array of user (Nama, Tanggal_Lahir, Username, Password, Role, Saldo)
users = []
users_default = ['','','','','',0]
users_count = 0
# list_wahana: Array of wahana (ID_Wahana, Nama_Wahana, Harga_Tiket, Batasan_Umur, Batasan_Tinggi)
list_wahana = []
list_wahana_default = ['','',0,0,False]
list_wahana_count = 0

# Global vars
current_login = users_default

# Global message const
LOGIN_MESSAGE = 'Anda belum login. Silahkan login dulu!'
NOT_PLAYER_MESSAGE = 'Anda bukan pemain, tidak bisa membeli tiket.'
NOT_ENOUGH_SALDO_MESSAGE = 'Saldo anda tidak cukup. Silakan mengisi saldo anda.'
CANNOT_PLAY_MESSAGE = '''Anda tidak memenuhi persyaratan untuk memainkan wahana ini.
      Silakan menggunakan wahana lain yang tersedia.'''