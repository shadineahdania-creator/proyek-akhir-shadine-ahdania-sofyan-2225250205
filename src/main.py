from data_io import baca_input
from analisis import (
    konversi_biner,
    konversi_oktal,
    konversi_heksadesimal,
    jenis_bilangan,
)
from utilitas import validasi_input


def main():
    data = baca_input()

    angka = validasi_input(data)

    if angka is None:
        print("Input tidak valid")
        return

    print("\n=== HASIL ANALISIS DAN KONVERSI ===")
    print("Desimal      :", angka)
    print("Biner        :", konversi_biner(angka))
    print("Oktal        :", konversi_oktal(angka))
    print("Heksadesimal :", konversi_heksadesimal(angka))
    print("Jenis        :", jenis_bilangan(angka))


if __name__ == "__main__":
    main()