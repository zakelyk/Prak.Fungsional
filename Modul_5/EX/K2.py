import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk = list(map(lambda x: x[1], data_transaksi))
jumlah_terjual = list(map(lambda x: x[2], data_transaksi))

# Hitung total pendapatan untuk setiap produk
pendapatan_produk = list(map(lambda x: x[1] * x[2], data_transaksi))

# Ekstrak label produk
produk_labels = list(map(lambda x: x[0], data_transaksi))

# Buat subplot dengan ukuran 1x2 (satu baris, dua kolom)
plt.figure(figsize=(12, 5))

# Scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.subplot(1, 2, 1)
plt.scatter(harga_produk, jumlah_terjual)
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')
plt.title('Hubungan Harga dan Jumlah Terjual')

# Bar chart untuk menyajikan pendapatan produk
plt.subplot(1, 2, 2)
plt.bar(produk_labels, pendapatan_produk, alpha=0.7)
plt.xlabel('Produk')
plt.ylabel('Pendapatan Produk')
plt.title('Pendapatan Produk')

# Menampilkan subplot
plt.tight_layout()
plt.show()
