nama_pembeli = input("Masukan Nama Pembeli:")
nomor_telepon = input("Masukan Nomor Telephon:")
menu = input("Pesan Menu apa?(Makanan atau Minuman):")
match menu :
    case "Makanan":
        print("Nasi Goreng - Rp. 15000")
        print("Mie Goreng - Rp. 12000")
        print("Ayam Geprek - Rp. 18000")
    case "Minuman":
        print("Aneka Jus - Rp. 15000")
        print("Soft Drink - Rp. 10000")
        print("Sweet Ice Tea - Rp. 5000")   
pesanan = input("Pesan Menu apa? : ")

# Makanan dan Minuman
if pesanan == "Nasi Goreng":
    harga = 15000
elif pesanan == "Mie Goreng":
    harga = 12000
elif pesanan == "Ayam Geprek":
    harga = 18000
elif pesanan == "Aneka Jus": 
    harga = 15000
elif pesanan == "Soft Drink":
    harga = 10000
elif pesanan == "Sweet Ice Tea":
    harga = 5000 
else :
    print("Makanan yang anda masukan tidak valid!")         
Jumlah_pesanan = int(input("Masukan Jumlah Pesanan:"))
Total_harga = harga * Jumlah_pesanan 

print("=" * 50)
print("Nama Pembeli\t\t:",nama_pembeli)
print("Nomor Telephon Pembeli\t:",nomor_telepon)
print("Menu yang dipesan\t:",pesanan)
print("Jumlah Pesanan\t\t:",Jumlah_pesanan)
print("Total Harga\t\t:",Total_harga)
print("=" * 50)