# Program Analisis dan Konversi Sistem Bilangan

## Identitas Mahasiswa

- **Nama:** Shadine Ahdania Sofyan
- **NIM:** 2225250205
- **Kelas:** 3B
- **Mata Kuliah:** Algoritma dan Pemrograman

## 1. Deskripsi Proyek

Program Analisis dan Konversi Sistem Bilangan merupakan program sederhana berbasis Python yang digunakan untuk mengonversi bilangan desimal ke sistem bilangan biner, oktal, dan heksadesimal.

Program ini juga menyediakan analisis sederhana untuk menentukan apakah bilangan yang dimasukkan termasuk bilangan ganjil atau genap. Program dirancang sebagai media bantu belajar bagi siswa, mahasiswa, dan guru matematika dalam memahami konsep sistem bilangan.

## 2. Latar Belakang

Sistem bilangan merupakan salah satu materi yang dipelajari dalam matematika dan ilmu komputer. Banyak siswa mengalami kesulitan dalam melakukan konversi bilangan dari sistem desimal ke sistem biner, oktal, dan heksadesimal secara manual. Kesalahan perhitungan sering terjadi karena proses konversi memerlukan beberapa langkah yang cukup panjang dan teliti.

Oleh karena itu, diperlukan sebuah program sederhana yang dapat membantu pengguna melakukan konversi bilangan secara cepat, akurat, dan mudah dipahami. Program ini juga memberikan analisis sederhana terhadap bilangan yang dimasukkan sehingga dapat digunakan sebagai media bantu belajar.

## 3. Tujuan dan Pengguna

### Tujuan

1. Membantu pengguna mengonversi bilangan desimal ke biner.
2. Membantu pengguna mengonversi bilangan desimal ke oktal.
3. Membantu pengguna mengonversi bilangan desimal ke heksadesimal.
4. Membantu pengguna memeriksa hasil konversi secara cepat.
5. Memberikan analisis sederhana terhadap bilangan yang dimasukkan.

### Pengguna

- Siswa.
- Mahasiswa.
- Guru matematika.

## 4. Fitur Program

### Fitur Wajib

- Menerima input bilangan desimal.
- Memvalidasi input pengguna.
- Mengonversi bilangan desimal ke biner.
- Mengonversi bilangan desimal ke oktal.
- Mengonversi bilangan desimal ke heksadesimal.
- Menampilkan hasil konversi.

### Fitur Tambahan

- Menentukan apakah bilangan termasuk ganjil atau genap.
- Menampilkan jumlah digit hasil konversi.

## 5. Analisis Pengguna dan Kebutuhan

### User Story

**Sebagai siswa**, saya ingin memasukkan sebuah bilangan desimal agar dapat mengetahui hasil konversi ke sistem biner, oktal, dan heksadesimal secara cepat dan akurat.

**Sebagai guru matematika**, saya ingin menggunakan program ini untuk membantu menjelaskan konsep sistem bilangan sehingga siswa dapat memeriksa hasil konversi yang telah mereka kerjakan.

### Kebutuhan Fungsional

| ID | Kebutuhan | Prioritas |
|---|---|---|
| F01 | Program menerima input bilangan desimal | Wajib |
| F02 | Program memvalidasi input pengguna | Wajib |
| F03 | Program mengonversi bilangan ke biner | Wajib |
| F04 | Program mengonversi bilangan ke oktal | Wajib |
| F05 | Program mengonversi bilangan ke heksadesimal | Wajib |
| F06 | Program menampilkan hasil konversi | Wajib |
| F07 | Program menentukan bilangan ganjil atau genap | Tambahan |

### Kebutuhan Nonfungsional

- Program mudah dijalankan melalui terminal VS Code.
- Pesan kesalahan mudah dipahami pengguna.
- Tampilan output mudah dibaca.
- Program dapat diuji menggunakan test case yang sama.

## 6. Spesifikasi Input, Proses, dan Output (IPO)

| Komponen | Deskripsi |
|---|---|
| Input | Bilangan desimal |
| Proses | Validasi input, konversi sistem bilangan, dan analisis bilangan |
| Output | Hasil konversi biner, oktal, heksadesimal, dan status ganjil/genap |

### Tabel IPO

| Input | Proses | Output |
|---|---|---|
| Bilangan desimal | Validasi input | Pesan kesalahan jika input tidak valid |
| Bilangan desimal valid | Konversi ke biner | Hasil biner |
| Bilangan desimal valid | Konversi ke oktal | Hasil oktal |
| Bilangan desimal valid | Konversi ke heksadesimal | Hasil heksadesimal |
| Bilangan desimal valid | Analisis bilangan | Status ganjil atau genap |

## 7. Algoritma dan Pseudocode

```text
MULAI

Input bilangan desimal

Jika input bukan bilangan bulat:
    Tampilkan pesan kesalahan
    Selesai

Jika bilangan tidak memenuhi validasi:
    Tampilkan pesan validasi
    Selesai

Konversi bilangan ke biner
Konversi bilangan ke oktal
Konversi bilangan ke heksadesimal

Tentukan apakah bilangan ganjil atau genap
Hitung jumlah digit setiap hasil konversi

Tampilkan seluruh hasil analisis

SELESAI
```

## 8. Struktur Program

| Fungsi | Tanggung Jawab |
|---|---|
| `validasi_input()` | Memeriksa validitas input pengguna |
| `konversi_biner()` | Mengubah desimal menjadi biner |
| `konversi_oktal()` | Mengubah desimal menjadi oktal |
| `konversi_heksadesimal()` | Mengubah desimal menjadi heksadesimal |
| `analisis_bilangan()` | Menentukan ganjil atau genap |
| `main()` | Mengatur alur utama program |

### Struktur Folder

```text
proyek-konversi-bilangan/
│
├── README.md
├── proposal.md
├── .gitignore
│
├── src/
│   ├── main.py
│   ├── konversi.py
│   └── validasi.py
│
├── tests/
│   └── test_case.md
│
└── output/
```

## 9. Struktur Data

| Data | Tipe Data | Keterangan |
|---|---|---|
| Bilangan input | Integer | Menyimpan bilangan desimal |
| Hasil konversi | String | Menyimpan hasil biner, oktal, dan heksadesimal |
| Status bilangan | String | Menyimpan keterangan ganjil atau genap |

## 10. Test Case

Test case digunakan untuk memeriksa apakah program menghasilkan keluaran sesuai dengan hasil yang diharapkan.

| ID | Kategori | Input | Expected Result |
|---|---|---|---|
| TC01 | Normal | `10` | Biner = `1010`, Oktal = `12`, Hex = `A` |
| TC02 | Normal | `25` | Biner = `11001`, Oktal = `31`, Hex = `19` |
| TC03 | Batas | `0` | Biner = `0`, Oktal = `0`, Hex = `0` |
| TC04 | Invalid | `-5` | Menampilkan pesan validasi |
| TC05 | Invalid | `abc` | Menampilkan pesan kesalahan |

### Kriteria Pengujian

- Input valid menghasilkan konversi yang benar.
- Input tidak valid ditangani dengan pesan kesalahan yang mudah dipahami.
- Hasil konversi sesuai dengan expected result.
- Fitur analisis ganjil/genap menghasilkan status yang benar.
- Program tidak berhenti secara tidak terkendali ketika menerima input yang tidak valid.

**Catatan:** Hasil aktual dan status PASS/FAIL dicatat setelah program selesai diimplementasikan dan diuji.

## 11. Cara Menjalankan Program

### Persiapan

1. Pastikan Python sudah terpasang.
2. Buka folder proyek `proyek-konversi-bilangan` di VS Code.
3. Pastikan struktur folder dan file Python sudah sesuai.
4. Buka terminal melalui menu **Terminal → New Terminal**.

### Menjalankan Program

Jalankan perintah berikut dari folder utama proyek:

```bash
python src/main.py
```

Jika perintah tersebut tidak berfungsi di Windows, coba:

```bash
py src/main.py
```

Pada lingkungan yang menggunakan perintah Python 3, gunakan:

```bash
python3 src/main.py
```

**Catatan:** Perintah tersebut dapat digunakan setelah file `src/main.py` dibuat dan implementasi program tersedia.

## 12. Contoh Penggunaan

Contoh berikut menunjukkan hasil yang diharapkan jika pengguna memasukkan bilangan desimal `10`.

```text
=== PROGRAM ANALISIS DAN KONVERSI SISTEM BILANGAN ===

Masukkan bilangan desimal: 10

Hasil Konversi:
Biner         : 1010
Oktal         : 12
Heksadesimal  : A

Analisis Bilangan:
Status        : Genap
```

Contoh tersebut merupakan ilustrasi keluaran yang diharapkan, bukan hasil eksekusi program yang telah diverifikasi.

## 13. Pembagian Tugas

| Tugas | Penanggung Jawab |
|---|---|
| Penyusunan proposal | Shadine |
| Perancangan program | Shadine |
| Pembuatan test case | Shadine |
| Implementasi program | Shadine |
| Dokumentasi dan GitHub | Shadine |

## 14. Jadwal Pengerjaan

| Tahap | Target |
|---|---|
| Pertemuan 14 | Penyusunan proposal dan test case |
| Sebelum Pertemuan 15 | Implementasi program |
| Pertemuan 15 | Testing dan debugging |
| Pertemuan 16 | Presentasi proyek |


## 15. Kesimpulan

Program Analisis dan Konversi Sistem Bilangan dirancang untuk membantu pengguna mengonversi bilangan desimal ke sistem biner, oktal, dan heksadesimal. Program juga direncanakan memiliki fitur validasi input dan analisis ganjil atau genap.

Melalui proyek ini, konsep sistem bilangan dapat dipelajari dengan bantuan program Python. Pengujian menggunakan test case dilakukan untuk memastikan hasil konversi sesuai dengan hasil yang diharapkan serta membantu menemukan dan memperbaiki kesalahan program.