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

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga = list(map(lambda x:x[1],data_transaksi))
terjual = list(map(lambda x:x[2],data_transaksi))
# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.figure(figsize=(12, 5))

plt.subplot(1,2,1)
plt.scatter(harga, terjual)
plt.xlabel("Harga Produk")
plt.ylabel("Jumlah Produk Terjual")
plt.title("Hubungan Harga Produk dan Jumlah Produk Terjual")
# TODO 3: Hitung total pendapatan untuk setiap produk
pendapatan = [x[1] * x[2] for x in data_transaksi]
# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
nama_produk = list(map(lambda x: x[0], data_transaksi))

plt.subplot(1,2,2)
plt.bar(nama_produk, pendapatan,alpha=0.7)
plt.xlabel("Nama Produk")
plt.ylabel("Pendapatan Produk")
plt.title("Pendapatan Produk")


plt.tight_layout()
plt.show()

# PS: Kalian bisa memanfaatkan list comprehension, map, dan lambda
# contoh output: (bebas divariasikan sesuai selera)