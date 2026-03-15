# # 1. Kita buat fungsinya dulu (mendefinisikan)
# def sapa_user():
#     print("Halo Bos!")
#     print("Selamat belajar Function!")

# # 2. Kode diatas nggak akan muncul kalau nggak dipanggil
# # cara memanggilnya:
# sapa_user()


# Fungsi dengan return 
def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas #Hasilnya dikirim balik kesini

# simpan hasil fungsi ke dalam variabel baru
hasil_hitung = hitung_luas_persegi(5)

# Kita bisa pakai 'hasil hitung' buat apa saja sekarang
print(f"Hasilnya disimpan di variabel, nilainya: {hasil_hitung}")