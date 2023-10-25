print("""
==================================================
Selamat datang di sistem penghitung luas bangun datar!
Silakan pilih bangun datar yang ingin dicari luasnya:

1 = Persegi
2 = Lingkaran
3 = Segitiga
0 = Keluar
""")
while True:
    pilihan = int(input("Masukkan pilihan Anda: "))

    match pilihan:
        case 1:
            sisi = int(input("Masukkan sisi: "))
            print("Luas persegi adalah: ", sisi * sisi)
        case 2:
            jari = int(input("Masukkan jari-jari: "))
            print("Luas lingkaran adalah: ", 0.5 * 3.14 * jari ** 2)
        case 3:
            alas = int(input("Masukkan alas: "))
            tinggi = int(input("Masukkan tinggi: "))
            print("Luas segitiga adalah: ", 0.5 * alas * tinggi)
        case 0:
            print("Terimakasih telah menggunakan sistem ini.")
            break
        case _:
            print("Angka yang Anda pilih tidak valid!")
    print("==================================================")
