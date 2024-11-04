# 1. 

kendaraan = ['beat karbu', 'motor', 200, 'hijau', 3]
print(kendaraan)

kendaraan.append('10jt')
print(kendaraan)

kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'honda')
print(kendaraan)

# 2. 

angka_pilihan = int(input("""Masukan pilihan:
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga"""))

match angka_pilihan:
    case 1:
        print("Menghitung Luas Persegi")
        sisi = int(input("Masukan nilai sisi: "))
        Luas_persegi = sisi ** 2
        print(f"Luas Persegi dengan sisi {sisi} cm, adalah {Luas_persegi} cm^2 ")

    case _:
        print("Input tidak valid")