# Mengambil input nilai
print("=== PROGRAM CEK KELULUSAN ===")
nilai_str = input("Masukkan nilai kamu : ")
nilai = int(nilai_str)

# Logika Percabangan
if nilai == 100:
    print("Luar biasa!!! Sempurna!")
elif nilai >= 75:
    print("Selamat kamu lulus")
    print("Pertahankan prestasimu")
else:
    print("Maaf kamu harus remedial")
    print("Jangan menyerah, coba lagi")

print("\nProgram Selesai.")