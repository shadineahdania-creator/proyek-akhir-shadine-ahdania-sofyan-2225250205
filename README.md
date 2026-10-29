# Program Analisis dan Konversi Sistem Bilangan

## Identitas Mahasiswa

- **Nama:** Shadine Ahdania Sofyan
- **NIM:** 2225250205
- **Kelas:** 3B
- **Mata Kuliah:** Algoritma dan Pemrograman



## Deskripsi

Program sederhana berbasis Python untuk mengonversi bilangan desimal ke sistem bilangan biner, oktal, dan heksadesimal. Program juga menampilkan analisis sederhana berupa informasi apakah bilangan yang dimasukkan termasuk bilangan ganjil atau genap.

## Tujuan

- Mengonversi bilangan desimal ke biner.
- Mengonversi bilangan desimal ke oktal.
- Mengonversi bilangan desimal ke heksadesimal.
- Menentukan apakah bilangan ganjil atau genap.
- Membantu pembelajaran materi sistem bilangan.

## Fitur

- Input bilangan desimal.
- Validasi input pengguna.
- Konversi ke biner.
- Konversi ke oktal.
- Konversi ke heksadesimal.
- Analisis ganjil atau genap.

## Struktur Folder

```text
proyek-konversi-bilangan/
│
├── README.md
├── proposal.md
├── .gitignore
│
├── data/
│   └── contoh_data.txt
│
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
│
├── tests/
│   └── test_case.md
│
└── output/
    └── .gitkeep
```

## Teknologi

- Python 3.x
- Visual Studio Code
- Git dan GitHub

## Cara Menjalankan

Buka terminal pada folder proyek kemudian jalankan:

```bash
python src/main.py
```

Jika menggunakan Windows:

```bash
py src/main.py
```

## Test Case

| ID | Kategori | Input | Expected Result |
|----|----------|--------|----------------|
| TC01 | Normal | 10 | Biner = 1010, Oktal = 12, Hex = A |
| TC02 | Normal | 25 | Biner = 11001, Oktal = 31, Hex = 19 |
| TC03 | Batas | 0 | Biner = 0, Oktal = 0, Hex = 0 |
| TC04 | Invalid | -5 | Menampilkan pesan validasi |
| TC05 | Invalid | abc | Menampilkan pesan kesalahan |


