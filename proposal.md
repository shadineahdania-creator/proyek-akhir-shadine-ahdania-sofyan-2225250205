# Proposal Proyek

## Nama
Shadine Ahdania Sofyan

## NIM
2225250205

## Kelas
3B

# 1. Judul Proyek

Program Analisis dan Konversi Sistem Bilangan

# 2. Latar Belakang

Sistem bilangan merupakan salah satu materi yang dipelajari dalam matematika dan ilmu komputer. Banyak siswa mengalami kesulitan dalam melakukan konversi bilangan dari sistem desimal ke sistem biner, oktal, dan heksadesimal secara manual. Kesalahan perhitungan sering terjadi karena proses konversi memerlukan beberapa langkah yang cukup panjang dan teliti.

Oleh karena itu, diperlukan sebuah program sederhana yang dapat membantu pengguna melakukan konversi bilangan secara cepat, akurat, dan mudah dipahami. Program ini juga memberikan analisis sederhana terhadap bilangan yang dimasukkan sehingga dapat digunakan sebagai media bantu belajar.

# 3. Pengguna dan Tujuan

## Pengguna

- Siswa
- Mahasiswa
- Guru Matematika

## Tujuan

- Membantu pengguna mengonversi bilangan desimal ke biner.
- Membantu pengguna mengonversi bilangan desimal ke oktal.
- Membantu pengguna mengonversi bilangan desimal ke heksadesimal.
- Membantu pengguna memeriksa hasil konversi secara cepat.
- Memberikan analisis sederhana terhadap bilangan yang dimasukkan.

# 4. Ruang Lingkup

## Fitur Wajib

- Input bilangan desimal.
- Konversi ke biner.
- Konversi ke oktal.
- Konversi ke heksadesimal.
- Validasi input pengguna.
- Menampilkan hasil konversi.

## Fitur Tambahan

- Menentukan apakah bilangan ganjil atau genap.
- Menampilkan jumlah digit hasil konversi.

# 5. Analisis Pengguna dan Kebutuhan

## User Story

Sebagai siswa, saya ingin memasukkan sebuah bilangan desimal agar saya dapat mengetahui hasil konversi ke sistem biner, oktal, dan heksadesimal secara cepat dan akurat.

Sebagai guru matematika, saya ingin menggunakan program ini untuk membantu menjelaskan konsep sistem bilangan sehingga siswa dapat memeriksa hasil konversi yang telah mereka kerjakan.

## Kebutuhan Fungsional

| ID | Kebutuhan | Prioritas |
|----|-----------|-----------|
| F01 | Program menerima input bilangan desimal | Wajib |
| F02 | Program memvalidasi input pengguna | Wajib |
| F03 | Program mengonversi bilangan ke biner | Wajib |
| F04 | Program mengonversi bilangan ke oktal | Wajib |
| F05 | Program mengonversi bilangan ke heksadesimal | Wajib |
| F06 | Program menampilkan hasil konversi | Wajib |
| F07 | Program menentukan ganjil atau genap | Tambahan |

## Kebutuhan Nonfungsional

- Program mudah dijalankan melalui terminal VS Code.
- Pesan kesalahan mudah dipahami pengguna.
- Tampilan output mudah dibaca.
- Program dapat diuji menggunakan test case yang sama.

# 6. Spesifikasi Input, Proses, dan Output (IPO)

| Komponen | Deskripsi |
|-----------|-----------|
| Input | Bilangan desimal |
| Proses | Validasi input, konversi ke biner, oktal, dan heksadesimal |
| Output | Hasil konversi dan analisis bilangan |

## Tabel IPO

| Input | Proses | Output |
|---------|---------|---------|
| Bilangan desimal | Validasi → Konversi → Analisis | Biner, Oktal, Heksadesimal, Status Ganjil/Genap |

# 7. Algoritma / Pseudocode

```text
MULAI

Input bilangan desimal

Jika input bukan angka:
    Tampilkan pesan error
    Selesai

Konversi ke biner
Konversi ke oktal
Konversi ke heksadesimal

Tentukan apakah bilangan ganjil atau genap

Tampilkan seluruh hasil

SELESAI
```

# 8. Struktur Program

| Fungsi | Tanggung Jawab |
|----------|---------------|
| validasi_input() | Memeriksa validitas input pengguna |
| konversi_biner() | Mengubah desimal menjadi biner |
| konversi_oktal() | Mengubah desimal menjadi oktal |
| konversi_heksadesimal() | Mengubah desimal menjadi heksadesimal |
| analisis_bilangan() | Menentukan ganjil atau genap |
| main() | Mengatur alur program |

## Struktur Folder

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

# 9. Struktur Data

| Data | Struktur |
|---------|---------|
| Bilangan input | Integer |
| Hasil konversi | String |
| Status ganjil/genap | String |

# 10. Test Case

| ID | Kategori | Input | Expected Result |
|----|----------|--------|----------------|
| TC01 | Normal | 10 | Biner = 1010, Oktal = 12, Hex = A |
| TC02 | Normal | 25 | Biner = 11001, Oktal = 31, Hex = 19 |
| TC03 | Batas | 0 | Biner = 0, Oktal = 0, Hex = 0 |
| TC04 | Invalid | -5 | Menampilkan pesan validasi |
| TC05 | Invalid | abc | Menampilkan pesan error |

# 11. Pembagian Tugas

| Tugas | PIC |
|---------|---------|
| Penyusunan Proposal | Shadine |
| Perancangan Program | Shadine |
| Pembuatan Test Case | Shadine |
| Implementasi Program | Shadine |
| Dokumentasi dan GitHub | Shadine |

# 12. Jadwal

| Tahap | Target |
|---------|---------|
| Pertemuan 14 | Penyusunan proposal dan test case |
| Sebelum Pertemuan 15 | Implementasi program |
| Pertemuan 15 | Testing dan debugging |
| Pertemuan 16 | Presentasi proyek |



