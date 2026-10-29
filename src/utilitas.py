def validasi_input(data):
    try:
        angka = int(data)

        if angka < 0:
            return None

        return angka

    except ValueError:
        return None