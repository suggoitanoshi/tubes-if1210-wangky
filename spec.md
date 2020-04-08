# Spesifikasi Program

### F01 - Load File
Program pertama kali akan menjalankan fungsi load.
```
$ load
Masukkan nama File User: user.csv
Masukkan nama File Daftar Wahana: wahana.csv
Masukkan nama File Pembelian Tiket: pembelian.csv
Masukkan nama File Penggunaan Tiket: penggunaan.csv
Masukkan nama File Kepemilikan Tiket: tiket.csv
Masukkan nama File Refund Tiket: refund.csv
Masukkan nama File Kritik dan Saran: kritiksaran.csv 
 
File perusahaan Willy Wangky’s Chocolate Factory telah di-load. 
```
Dapat diasumsikan nama file valid dan struktur data file sesuai definisi.

### F02 - Save File
User bisa menjalankan penyimpanan data dengan menjalankan fungsi save.
```
$ save
Masukkan nama File User: user.csv
Masukkan nama File Daftar Wahana: wahana.csv
Masukkan nama File Pembelian Tiket: pembelian.csv
Masukkan nama File Penggunaan Tiket: penggunaan.csv
Masukkan nama File Kepemilikan Tiket: tiket.csv
Masukkan nama File Refund Tiket: refund.csv
Masukkan nama File Kritik dan Saran: kritiksaran.csv 
 
Data berhasil disimpan!
```

### F03 - Sign Up User
Pendaftaran pemain hanya bisa dilakukan oleh `Admin` dan tidak diizinkan
memasukkan username yang sudah terdaftar.
```
> signup
Masukkan nama pemain: Willy Wangky
Masukkan tanggal lahir pemain (DD/MM/YYYY): 30/06/1971
Masukkan tinggi badan pemain (cm): 178
Masukkan username pemain: wangkypro
Masukkan password pemain: coklatenakno1 
 
Selamat menjadi pemain, Willy Wangky. Selamat bermain.
```


### F04 - Login User
Login dapat dilakukan baik oleh `Pemain` maupun `Admin`. Hanya dapat dilakukan
jika pengguna belum login.
```
$ login
Masukkan username: wangkypro
Masukkan password: coklatenakno1

Selamat bersenang-senang, Willy Wangky!
```
Bila login gagal (username tidak ditemukan, password tidak sesuai) maka pesan
kesalahan akan muncul.
```
$ login
Masukkan username: wangkypro
Masukkan password: coklatenakno2 
 
Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi! 
```

### F05 - Pencarian Pemain
`Admin` bisa menjalankan fungsi untuk mencari data diri pemain wahana.
Jika username tidak ditemukan, tampilkan pesan error.
```
$ cari_pemain
Masukkan username: wangkypro
Nama Pemain: Willy Wangky
Tinggi Pemain: 178 cm
Tanggal Lahir Pemain: 30/06/1971
```

### F06 - Pencarian Wahana
Data wahana dapat dicari berdasarkan beberapa filter, yaitu
*batasan umur (Anak-anak/Dewasa/Semua Umur)* dan
*Tinggi Badan (>=170/tanpa batas)*.
Faktor ditampilkan dalam list dan pengguna memilih angka dari list.
```
$ cari
Jenis batasan umur:
1. Anak-anak (<17 tahun)
2. Dewasa (>=17 tahun)
3. Semua umur 
 
Jenis batasan tinggi badan:
1. Lebih dari 170 cm
2. Tanpa batasan 
 
Batasan umur pemain: 1
Batasan tinggi badan: 2 
 
Hasil pencarian:
AFQ107 | Cocoa Rain | 70000
NVD011 | Hazelnut River | 10000
```
Perlu dilakukan validasi terhadap input user. Asumsikan user dapat memasukkan karakter apapun.
```
$ cari
Jenis batasan umur:
1. Anak-anak (<17 tahun)
2. Dewasa (>=17 tahun)
3. Semua umur 
 
Jenis batasan tinggi badan:
1. Lebih dari 170 cm
2. Tanpa batasan 
 
Batasan umur pemain: 4
Batasan umur tidak valid!
Batasan umur pemain: 1
Batasan tinggi badan: &
Batasan tinggi badan tidak valid!
Batasan tinggi badan: 1 
 
Hasil pencarian: Tidak ada wahana yang sesuai dengan pencarian kamu.
```

### F07 - Pembelian Tiket
Hanya dapat dilakukan oleh `Pemain` yang telah terdaftar dan login.
```
$ beli_tiket
Masukkan ID wahana: IKR106
Masukkan tanggal hari ini: 07/04/2020
Jumlah tiket yang dibeli: 2 
 
Selamat bersenang-senang di Almond’s Charm.
```
`Pemain` bisa saja tidak cukup umur atau tidak cukup tinggi.
```
$ beli_tiket
Masukkan ID wahana: IKR106
Masukkan tanggal hari ini: 07/04/2020
Jumlah tiket yang dibeli: 2 
 
Anda tidak memenuhi persyaratan untuk memainkan wahana ini. Silakan menggunakan
wahana lain yang tersedia. 
```
`Pemain` juga bisa tidak memiliki saldo cukup. Prioritaskan tampilan
persyaratan tinggi dan umur.
```
$ beli_tiket
Masukkan ID wahana: IKR106
Masukkan tanggal hari ini: 07/04/2020
Jumlah tiket yang dibeli: 2 
 
Saldo Anda tidak cukup Silakan mengisi saldo Anda
```

### F08 - Menggunakan Tiket
`Pemain` dapat menggunakan tiket untuk bermain.
```
$ main
Masukkan ID wahana: IKR106
Masukkan tanggal hari ini: 08/04/2020
Jumlah tiket yang dgunakan: 2 
 
Terima kasih telah bermain.
```
Validasi ID wahana dan jumlah tiket.
```
$ main
Masukkan ID wahana: IKR106
Masukkan tanggal hari ini: 08/04/2020
Jumlah tiket yang dgunakan: 19 
 
Tiket Anda tidak valid dalam sistem kami
```

### F09 - Refund
Refund hanya dapat dilakukan oleh `Pemain` yang telah login dan memiliki tiket
terkait. Jumlah refund harus lebih murah dari harga tiket awal.
```
$ refund
Masukkan ID wahana: DIT025
Jumlah tiket yang di-refund: 2 
 
Uang refund sudah kami berikan pada akun Anda.
```
Validasi jumlah refund dan ID wahana.
```
$ refund
Masukkan ID wahana: DIT025
Jumlah tiket yang di-refund: 100 
 
Anda tidak memiliki tiket terkait.
```

### F10 - Kritik dan Saran
`Pemain` dapat memberikan kritik dan saran untuk suatu wahana.
```
$ kritik_saran
Masukkan ID Wahana: AHR099
Masukkan tanggal pelaporan: 31/03/2020
Kritik/saran Anda: Terjadi kebocoran pipa coklat 
 
Kritik dan saran Anda kami terima.
```
Diasumsikan ID Wahana, tanggal valid.

### F11 - Melihat Kritik dan Saran
`Admin` dapat melihat kritik dan saran yang diberikan oleh `Pemain`.
Diurutkan berdasarkan ID Wahana secara alfabetis.
Format: `ID_Wahana`|`Tanggal Pelaporan`|`Username Pemain`|`Isi Kritik dan Saran`
```
$ lihat_laporan
Kritik dan saran:
AHR007 | 31/03/2020 | stanley | Terjadi kebocoran pipa coklat
AFQ107 | 29/02/2020 | yoels | Kurang menarik 
```

### F12 - Menambahkan Wahana Baru
`Admin` dapat menambahkan wahana baru ke dalam manajemen wahana.
```
$ tambah_wahana
Masukkan Informasi Wahana yang ditambahkan: 
Masukkan ID Wahana: LAB135
Masukkan Nama Wahana: Recursive Cafe
Masukkan Harga Tiket: 135000
Batasan umur: dewasa
Batasan tinggi badan: tanpa batasan 
 
Info wahana telah ditambahkan
```
Dapat diasumsikan semua masukan valid.

### F13 - Top Up Saldo
`Admin` bisa menambahkan saldo `Pemain`
```
$ topup
Masukkan username: wangkypro 
Masukkan saldo yang di-top up: 99000 
 
Top up berhasil. Saldo Willy Wangky bertambah menjadi 169000
```
Pada contoh diatas, Willy Wangky memliki saldo awal 70000.  
Semua masukan dianggap valid.

### F14 - Melihat Riwayat Penggunaan Wahana
`Admin` bisa melihat riwayat penggunaan wahana
Format: `Tanggal_Bermain`|`Username Pengguna`|`Jumlah Tiket`
```
$ riwayat_wahana
Masukkan ID Wahana: AFQ107
Riwayat:
21/03/2020 | wangkypro | 2
30/03/2020 | stanley | 3
12/04/2020 | firastic | 1 
```
Dapat diasumsikan ID Wahana valid.

### F15 - Melihat Jumlah Tiket Pemain
`Admin` bisa melihat jumlah tiket yang dimiliki pemain.
Format: `ID_Wahana`|`Nama_Wahana`|`Jumlah Tiket`
```
$ tiket_pemain
Masukkan username: wangkypro
Riwayat:
AFQ107 | Cocoa Rain | 1
NVD011 | Hazelnut River | 4 
```
Dapat diasumsikan username valid.

### F16 - Exit
Pengguna dapat menjalankan perintah exit. Saat perintah ini dijalankan,
user akan ditanya apakah mereka akan menyimpan data.
```
$ exit
Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? Y  
```

## Spesifikasi Bonus
### B01 - Penyimpanan Password
Gunakan algoritma enkripsi atau hash untuk menyimpan password.
### B02 - Golden Account
Akun gold dapat diberikan oleh `Admin` dengan syarat membayar suatu harga upgrade.
Keuntungan akun gold adalah membeli tiket dengan setengah harga.
Database yang sudah ada boleh dirombak.
```
$ upgrade_gold
Masukkan username yang ingin di-upgrade: wangkypro 
 
Akun Anda telah diupgrade.
```
### B03 - Best Wahana
Berikan 3 wahana terbaik berdasarkan jumlah tiket yang terjual
Format: `Rank`|`ID_Wahana`|`Nama Wahana`|`Jumlah tiket terjual`
```
$ best_wahana
1 | DIT025 | Almond Lava | 129
2 | AFQ107 | Cocoa Rain | 112
3 | WGY091 | Raspberry Pie | 101
```
### B04 - Laporan Kehilangan Tiket
`Pemain` dapat melaporkan kehilangan tiket dengan memasukkan
username, tanggal kehilangan, ID Wahana, dan jumlah hilang.
Diperbolehkan menambah database baru.
```
$ tiket_hilang
Masukkan username: wangkypro
Tanggal kehilangan tiket: 09/04/2020
ID wahana: DIT025 
Jumlah tiket yang dihilangkan: 2 
 
Laporan kehilangan tiket Anda telah direkam.
```
Semua input diasumsikan valid, namun tiket yang hilang harus mengurangi
tiket yang dimiliki `Pemain`.