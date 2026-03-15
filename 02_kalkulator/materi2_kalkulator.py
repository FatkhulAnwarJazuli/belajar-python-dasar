# Mengambil input angka
print("=== PROGRAM KALKULATOR TAMBAH ===")
angka_pertama = input("Masukkan angka ke-1 = ")
angka_kedua = input("Masukkan angka ke-2 = ")

# 2. Proses Konversi & Penjumlahan
# ingat: input() menghasilkan teks, jadi harus diubah ke int()
tambah = int(angka_pertama) + int(angka_kedua)
kali = int(angka_pertama) * int(angka_kedua)

# 3. Menampilkan hasil(Output)
print("\n--- HASIL PERHITUNGAN ---")
print(f"Hasil dari {angka_pertama} + {angka_kedua} adalah: {tambah}")
print(f"Hasil dari {angka_pertama} x {angka_kedua} adalah: {kali}")

