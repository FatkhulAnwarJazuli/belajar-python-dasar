# 1. Minta nama user
nama = input("Masukkan nama anda: ")

# 2. Siapkan list kosong
daftar_belanja=[]

# 3. Looping untuk minta 5 barang
print("Silakan masukkan 5 barang belanjaan: ")
for i in range(5):
    barang = input(f"Barang ke-{i+1}: ")
    # Tulis kode .append disini biar masuk ke list 
    daftar_belanja.append(barang)

# 4. Header struk
# .upper() biar nama user jadi huruf besar semua
print(f"\n--- STRUK BELANJA {nama.upper()} ---")

#5. Hitung jumlah total data didalam list pakai len()
total = len(daftar_belanja)
print(f"Total barang: {total}")

# 6. Logika if untuk bonus
if total >= 5:
    print("Selamat! Anda mendapatkan kupon undian. ")

# 7. looping untuk membongkar isi list dan menampilkannya 1 per-1
print("Daftar Barang: ")
for item in daftar_belanja:
    print(f"-{item}")

print("--------------------------------------")