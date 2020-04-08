# Struktur data file eksternal:

### User
| Field | Tipe | Keterangan |
|-------|------|------------|
|`Nama`| String | Nama pengguna |
|`Tanggal_Lahir`| String | Tanggal* lahir |
|`Username`| String | Username pengguna |
|`Password`| String | Password pengguna |
|`Role`| String | Role pengguna (`Pemain`/`Admin`) untuk menentukan akses |
|`Saldo`| int | Saldo yang dimiliki pengguna, default 0 untuk `Admin` |

### Wahana
| Field | Tipe | Keterangan |
|-------|------|------------|
|`ID_Wahana`| String | Identitas wahana** | D  
|`Nama_Wahana`| String | Nama dari wahana |
|`Harga_Tiket`| int | Harga satu tiket wahana |
|`Batasan_Umur`| int | `0`: Semua umur <br> `1`: Anak-anak <br> `2`: Dewasa |
|`Batasan_Tinggi`| boolean | `true`: untuk tinggi >= 170cm <br> `false`: untuk semua tinggi |

### Pembelian Tiket
| Field | Tipe | Keterangan |
|-------|------|------------|
|`Username`| String | Username akun yang membeli tiket |
|`Tanggal_Pembelian`| String | Tanggal* pembelian tiket wahana |
|`ID_Wahana`| String | Identitas wahana** yang tiketnya dibeli |
|`Jumlah_Tiket`| int | Jumlah tiket yang dibeli untuk wahana terkait |

### Penggunaan Tiket
| Field | Tipe | Keterangan |
|-------|------|------------|
|`Username`| String | Username akun yang menggunakan tiket |
|`Tanggal_Penggunaan`| String | Tanggal* tiket digunakan |
|`ID_Wahana`| String | Identitas wahana** yang tiketnya digunakan |
|`Jumlah_Tiket`| int | Jumlah tiket yang digunakan untuk wahana terkait |

### Kepemilikan Tiket
| Field | Tipe | Keterangan |
|-------|------|------------|
|`Username`| String | Username yang memiliki tiket |
|`ID_Wahana`| String | Identitas wahana* yang tiketnya dimiliki |
|`Jumlah_Tiket`| int | Jumlah tiket yang dimiliki |

### Refund Tiket
| Field | Tipe | Keterangan |
|-------|------|------------|
|`Username`| String | Username yang merefund |
|`Tanggal_Refund`| String | Tanggal* refund |
|`ID_Wahana`| String | Identitas wahana** yang di-refund tiketnya |
|`Jumlah_Tiket`| int | Jumlah tiket yang di-refund |

### Kritik dan Saran
| Field | Tipe | Keterangan |
|-------|------|------------|
|`Username`| String | Username yang memberi kritik dan saran |
|`Tanggal_Kritik`| String | Tanggal* pengguna memberikan kritik dan saran |
|`ID_Wahana`| String | Identitas wahana** yang diberikan kritik dan saran |
|`Isi_Kritik`| String | Pesan kritik dari pemain. |


### Catatan Tambahan
*: Format tanggal menggunakan `DD/MM/YYYY`  
**: Format ID Wahana menggunakan format `AAANNN`, dimana `AAA` adalah kode alfabetik huruf kapital dan `NNN` adalah kode numerik.

