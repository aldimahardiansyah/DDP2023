tinggi = int(input("Masukkan tinggi badan Anda: "))

# untuk laki-laki
beratL = (tinggi - 100) - (tinggi - 100) * 0.1

# untuk perempuan
beratP = (tinggi - 100) - (tinggi - 100) * 0.15

print("Berat badan ideal laki-laki: ", beratL, "kg")
print("Berat badan ideal perempuan: ", beratP, "kg")