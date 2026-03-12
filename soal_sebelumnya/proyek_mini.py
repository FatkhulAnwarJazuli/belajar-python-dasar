backpack = ["Pedang", "Potion", "Peta"]
print("=" * 30 + " PROYEK MINI " + "=" * 30)
print(f"Isi tas kamu adalah: {backpack}")

barang_baru = input("\nMasukkan nama barang yang kamu temukan: ")
backpack.append(barang_baru)
print(backpack)

barang_dibuang = backpack.pop(0)
print(f"\nKarena tas penuh, saya harus membuang: {barang_dibuang}")
print(f"Sisa isi tas sekarang: {backpack}")

# Mencari item
mencari_barang = input("\nMau cari barang apa di dalam tas? ").lower()
backpack_kecil = [item.lower() for item in backpack]
if mencari_barang in backpack_kecil :
    print("Barang tersedia!")
else:
    print("Barang tidak ada didalam tas.")


#merapikan urutannya
print(f"\nBarang sebelum dirapikan: {backpack}")
backpack.sort()
print(f"Barang setelah dirapikan: {backpack}")

status = len(backpack)
print(f"\nJumlah barang yang ada didalam tas yaitu: {status} buah")