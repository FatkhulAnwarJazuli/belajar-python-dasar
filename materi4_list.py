# # PEMBELAJARAN
# # 1. Membuat List (Gunakan kurung siku [ ])
# buah = ["Apel", "Jeruk", "Mangga", "Pisang"]

# # 2. Menampilkan semua isi list
# print(f"Isi keranjang: {buah}")

# # 3. Mengambil satu data saja (Mulai hitung dari 0!)
# print(f"Buah pertama: {buah[0]}")
# print(f"Buah kedua: {buah[1]}")

# # 4. Menambah data baru ke dalam list
# buah.append("Semangka")
# print(f"Setelah ditambah: {buah}")

# # 5. Menghapus data
# buah.remove("Jeruk")
# print(f"Setelah dihapus: {buah}")


# #Soal
# teman = ["Aan", "Anwar", "Udin"]

# print(f"Teman kedua: {teman[1]}")

# cek_nama = input("Cari nama teman: ")
# if cek_nama in teman:
#     print(f"Iya, {cek_nama} ada didalam daftar temanmu!")
# else:
#     print(f"Maaf, {cek_nama} tidak ditemukan.")

# total = len(teman)
# print(f"kamu punya {total} teman")

# #Cara mengganti isi list
# teman[2] = "Udin Sedunia"

# print(f"Daftar teman terbaru: {teman}")

# #Soal2
# makanan = ["Nasi", "Ayam"]
# print(f"Daftar makanan yaitu: {makanan}")
# print(f"Makanan pertama: {makanan[0]}")
# print(f"Makanan kedua: {makanan[1]}")

# makanan.append("Es Teh")
# print(f"Makanan setelah ditambah: {makanan}")
# makanan[0] = "Nasi Goreng"
# print(f"Makanan setelah diganti: {makanan}")

# #Soal3
# antrean = ["Budi", "Santi"]
# print(f"Antrean sekarang yaitu: {antrean}")
# antrean.append("Agus")
# print(f"Orang pertama dalam antrean adalah {antrean[0]}")

# selesai = input("Siapa yang sudah selesai? ")
# antrean.remove(selesai)
# print(f"Sisa antrean sekarang: {antrean}")

#Soal4
gudang = ["Meja", "Kursi", "Lampu"]
print(f"Isi gudang sekarang adalah: {gudang}")

barang_masuk = input("\nMasukkan nama barang baru: ")
gudang.append(barang_masuk)
print(f"\nIsi gudang setelah barang masuk: {gudang} ")

total = len(gudang)
print(f"\nTotal barang sekarang ada: {total}")

cek_barang = input("Cek stok barang apa? ")
if cek_barang in gudang:
    print(f"\nStok {cek_barang} masih tersedia!")
else:
    print("\nMaaf, barang tersebut belum masuk gudang")