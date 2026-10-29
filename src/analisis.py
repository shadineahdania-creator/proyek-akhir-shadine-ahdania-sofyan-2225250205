def konversi_biner(angka):
    return bin(angka)[2:]


def konversi_oktal(angka):
    return oct(angka)[2:]


def konversi_heksadesimal(angka):
    return hex(angka)[2:].upper()


def jenis_bilangan(angka):
    if angka % 2 == 0:
        return "Genap"
    return "Ganjil"
