# 1. Mengambil Data (input)
# kita gunakan fungsi input(). hasilnya akan disimpan didalam variabel.
print("--- PROGRAM BIODATA SEDERHANA---")
nama = input("Siapa namamu? ")
umur = input("Berapa Umurmu? ")
hobi = input("Apa hobimu? ")

# 2. Mengolah data (Opsional)
# Karena input() selalu menghasilkan teks (string), kita bisa hitung
# umur kamu 5 tahun lagi (perlu diubah keangka dulu dengan int())
umur_nanti = int(umur) + 5

# 3. Menampilkan data (Output)
#Kita gunakan 'f-string' agar memasukkan variabel ke dalam teks jadi mudah
print("\n--- HASIL PROSES ---")
print(f"Halo {nama}!")
print(f"Kamu sekarang berumur {umur} tahun dan hobimu adalah {hobi}.")
print(f"Wah, 5 tahun lagi kamu bakal berumur {umur_nanti} tahun!")