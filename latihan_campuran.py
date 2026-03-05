menu = ["Nasi", "Ayam", "Teh"]

harga_nasi = 5000
harga_ayam = 10000
harga_teh = 3000

nama = input("Nama pembeli: ")
beli = input("Mau beli apa? (Nasi/Ayam/Teh): ")

if beli in menu :
    jumlah = int(input(f"Mau beli berapa porsi {beli}? "))

    if beli == "Nasi" :
        total = jumlah * harga_nasi
    elif beli == "Ayam" :
        total = jumlah * harga_ayam
    elif beli == "Teh" :
        total = jumlah * harga_teh
    
    print("-" * 30)
    print(f"Total belanja {nama} adalah Rp {total}")
    print("Terimakasih sudah mampir")
    print("-" * 30)

else:
    print(f"\nMaaf {nama}, menu '{beli}' tidak tersedia di warung kami.")

print("=" * 30)
nilai = int(input("Masukkan nilai kamu: "))

if nilai >= 90:
    print("Grade A: Luar biasa!")
elif nilai >= 70:
    print("Grade B: Bagus!")
else:
    print("Grade C Belajar lagi yaa!")

print("=" * 30)