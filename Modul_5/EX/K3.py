import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10  # Misalnya interval ukuran per 10 sentimeter

# Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def kelompokkan_ke_interval(tinggi_badan, interval_size):
    return [(tinggi // interval_size) * interval_size for tinggi in tinggi_badan]

# Menghitung frekuensi tinggi badan dalam interval
def hitung_frekuensi(tinggi_badan_interval):
    frekuensi = {}
    for tinggi in tinggi_badan_interval:
        frekuensi[tinggi] = frekuensi.get(tinggi, 0) + 1
    return frekuensi

# Visualisasi data dalam bentuk histogram
# def visualisasi_histogram(frekuensi, interval_size):
#     tinggi = list(frekuensi.keys())
#     frekuensi_tinggi = list(frekuensi.values())

#     plt.bar(tinggi, frekuensi_tinggi, width=interval_size, edgecolor='None')  # Set edgecolor menjadi 'None'
#     plt.xlabel('Tinggi Badan (cm)')
#     plt.ylabel('Frekuensi')
#     plt.title('Histogram Tinggi Badan')
#     plt.show()

# Menambahkan kurva pdf pada hasil visualisasi data
def visualisasi_histogram_dan_pdf(tinggi_badan, interval_size):
    tinggi_badan_interval = kelompokkan_ke_interval(tinggi_badan, interval_size)
    frekuensi = hitung_frekuensi(tinggi_badan_interval)

    tinggi = np.arange(min(tinggi_badan), max(tinggi_badan) + interval_size, interval_size)
    pdf = norm.pdf(tinggi, np.mean(tinggi_badan), np.std(tinggi_badan))

    plt.bar(tinggi, list(frekuensi.values()), width=interval_size, edgecolor='None', alpha=0.7, label='Histogram')
    plt.plot(tinggi, pdf * len(tinggi_badan) * interval_size, color='red', label='PDF (Distribusi Normal)')
    
    plt.xlabel('Tinggi Badan (cm)')
    plt.ylabel('Frekuensi / PDF')
    plt.title('Histogram dan Kurva PDF Tinggi Badan')
    plt.legend(loc='lower left')
    plt.show()

# Panggil fungsi untuk visualisasi histogram dan kurva PDF
visualisasi_histogram_dan_pdf(tinggi_badan, interval_size)
