#Soal1
angka = int(input("Masukkan angkanya: "))

# cek pakai modulo'
if angka % 2 ==0:
    print("Ini angka genap")
else:
    print("Ini angka ganjil")


#Soal2
harga_tiket = 50000
umur = int(input("Berapa umur anda? "))

if umur <= 12:
    harga_tiket = 25000
elif umur >= 60:
    harga_tiket = 30000

print(f"Harga tiket untuk anda adalah: {harga_tiket}")


#Soal3
users = ["admin", "anwar", "cyber"]
username_input = input("Masukkan username: ")

if username_input in users:
    print("Akses diterima, selamat!!!")
else:
    print("Akses ditolak! Username tidak ditemukan.")


#Soal4
berat_badan = float(input("Berapa berat badan kamu? "))
tinggi_badan = float(input("Berapa tinggi badan kamu? "))
bmi = berat_badan/(tinggi_badan ** 2)

if bmi <18.5 :
    print("Kamu kurus")
elif 18.5 <= bmi < 25:
    print("Kamu ideal")
elif bmi >= 25:
    print("Kamu gemuk")

#Soal5
stok_hp = ["iphone", "samsung", "oppo"]
print(f"Stok saat ini adalah: {stok_hp}")

index = int(input("Ganti nomor berapa? (0/1/2): "))
hp_baru = input("Masukkan hp baru: ")

stok_hp[index] = hp_baru

print(f"Stok terbaru adalah: {stok_hp}")


#Soal6
keranjang = ["Apel", "Mangga"]
print(f"Isi keranjang awal: {keranjang}")

buah_baru = input("Mau tambah buah apa? ")
keranjang.append(buah_baru)
print(f"Keranjang baru: {keranjang}")


#Soal 7 - Menghapus barang
keranjang = ["Apel", "Mangga", "Jeruk"]
print(f"Isi keranjang awal: {keranjang}")

barang_dibuang = keranjang.pop(1)

print(f"Barang yang dibuang: {barang_dibuang}")
print(f"Isi keranjang terbaru: {keranjang}")


#Soal8
keranjang = ["apel",  "anggur", "mangga"]
cari_buah = input("Mau cari buah apa? ")

if cari_buah.lower() in keranjang :
    print("Iya, buah itu ada!")
else:
    print("Yahh, buah itu nggak ada...")


#Soal9
keranjang = ["Mangga", "Apel", "Jeruk", "Duku"]
print(f"Sebelum diurutkan: {keranjang}")

keranjang.sort()
print(f"Sesudah diurutkan: {keranjang}")


#Soal10
keranjang = ["Apel", "Mangga", "Jeruk", "Duku", "Salak"]

jumlah = len(keranjang)

print(f"Jumlah barang di keranjang: {jumlah}")