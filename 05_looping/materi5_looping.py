daftar_belanja = ["Gula", "Tepung", "Mie", "Telur", "Air Mineral"]
barang_panjang = []

for barang in daftar_belanja:
    print(f"Isi daftar belanjanya yaitu: {barang}")

    if len(barang) > 5:
        barang_panjang.append(barang)

hasil_rapi = " dan ".join(barang_panjang)
print(f"\nBarang yang lebih dari 5 huruf  adalah: {hasil_rapi}")