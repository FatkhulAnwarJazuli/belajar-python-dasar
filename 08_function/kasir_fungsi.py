# # Fungsi untuk mengecek bonus 
# def cek_bonus(total_barang):
#     if total_barang >=5:
#         return "Selamat! Anda dapat kupon undian"
#     else:
#         return "Maaf, belum dapat bonus."
    
# # Program utama
# daftar_belanja = ["Sabun", "Beras", "Minyak", "Gula", "Kopi"]
# total = len(daftar_belanja)

# # Memanggil fungsi dan menyimpan hasilnya di dalam variabel 'pesan'
# pesan = cek_bonus(total)

# print(f"Total barang: {total}")
# print(F"Status bonus: {pesan}")


# Latihan Mandiri
def hitung_diskon(total_belanja):
    if total_belanja > 100000:
        return 0.1
    else:
        return 0
    
# PROGRAM LATIHAN MANDIRI
daftar_harga = [50000, 70000, 150000, 200000]

# hitung total harga
def hitung_total_belanja(list_harga):
    total=0 #Mulai dari 0
    for harga in list_harga:
        total = total + harga # Tambahkan tiap angka ke dalam total
    return total

# Panggil fungsinuya
hasil_total = hitung_total_belanja(daftar_harga)
print(f"Total belanjaan kamu: Rp.{hasil_total}")

#panggil diskon
diskon_persen = hitung_diskon(hasil_total)

# hitung potongan harganya
potongan = hasil_total * diskon_persen
total_bayar = hasil_total - potongan

print(f"Diskon yang didapat: {diskon_persen * 100}")
print(f"Total yang harus dibayar: Rp.{total_bayar:.0f}")