# Diketahui
luas_ABCD = 600
luas_ABFE = 300
luas_ADHE = 200

"""
    Jadi kita ketahui di sini
    ada p -> panjang, l -> lebar, t -> tinggi
    p * l = 600
    l = 600 / p
    p * t = 300
    l * t = 200
    t = 200 / l

    untuk mendapatkan p (panjang) kita harus menghitung
    akar dari luas_ABCD * luas_ABFE / luas_ADHE
"""
p = (luas_ABCD * luas_ABFE / luas_ADHE) ** 0.5

# Menggunakan panjang (p) untuk mencari lebar (l)
l = luas_ABCD / p

# Menggunakan lebar (l) untuk mencari tinggi (t)
t = luas_ADHE / l

# Output hasil
print(f"Panjang (p): {p} cm")
print(f"Lebar (l): {l} cm")
print(f"Tinggi (t): {t} cm")

"""
    Balok memiliki 12 rusuk yang masing masing adalah 4 panjang, 4 lebar, dan 4 tinggi
    jadi untuk menjumlahkan seluruh rusuk yang ada, kita perlu mengkalikan p, l, t
    dengan 4

    hasil = (p*4) + (l*4) + (t*4)
"""

hasil = (p*4) + (l*4) + (t*4)
print(hasil)