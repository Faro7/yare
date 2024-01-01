import module_mtk

a = int(input("Masukin angka pertama :"))
b = int(input("Masukin angka kedua :"))

# panggil fungsi-fungsi dari modul
hasil_tambah = module_mtk.tambah(a, b)
hasil_kurang = module_mtk.kurang(a, b)
hasil_kali = module_mtk.kali(a, b)
hasil_bagi = module_mtk.bagi(a, b)

# Tampilkan hasil
print("Hasil Penjumlahan:", hasil_tambah)
print("Hasil Pengurangan:", hasil_kurang)
print("Hasil Perkalian:", hasil_kali)
print("Hasil Pembagian:", hasil_kali)








