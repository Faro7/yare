try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil pembagian 10 dengan angka yang dimasukkan:", hasil)
    
except ValueError:
    print("Terjadi kesalahan! Input harus berupa angka.")
    
except ZeroDivisionError:
    print("Terjadi kesalahan! Tidak bisa membagi angka dengan nol.")
    
except Exception as e:
    print("Terjadi Kesalahan:",e)
    
else:
    print("Terjadi kesalahan! Program selesai tanpa exception.")
    
finally:
    print("selesai.")